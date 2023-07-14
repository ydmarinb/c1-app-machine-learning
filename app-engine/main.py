from fastapi import FastAPI
from pydantic import BaseModel
from google.cloud import storage
import pickle
import os

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Definir el modelo de datos utilizando Pydantic
class Variables(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Ruta POST para la predicción
@app.post('/')
def predict(variables: Variables):
    # Verificar si el archivo pickle del modelo ya está descargado localmente
    local_path = 'model_v1.pkl'
    if not os.path.exists(local_path):
        download_model(local_path)
    
    # Cargar el modelo entrenado desde el archivo pickle descargado
    rf = load_model(local_path)
    
    # Realizar la predicción utilizando el modelo cargado
    prediction = make_prediction(rf, variables)
    
    # Retornar la predicción y el mensaje del evento de Pub/Sub como resultado de la función
    return {'prediction': prediction}


def download_model(local_path):
    # Verificar si se proporcionó un archivo de credenciales JSON
    if 'GOOGLE_APPLICATION_CREDENTIALS' in os.environ:
        # Crear una instancia del cliente de almacenamiento de Cloud Storage con autenticación por credenciales
        client = storage.Client()
    else:
        # Crear una instancia del cliente de almacenamiento de Cloud Storage con autenticación predeterminada
        client = storage.Client.from_service_account_json('credentials.json')  # Reemplazar 'ruta-al-archivo-credenciales.json' con la ruta real del archivo de credenciales JSON
    
    # Obtener el objeto de almacenamiento del archivo pickle desde el bucket
    bucket = client.get_bucket('registry-models')  # Reemplazar 'nombre-del-bucket' con el nombre real del bucket
    blob = bucket.blob('model_v1.pkl')  # Reemplazar 'ruta-al-archivo' con la ruta real del archivo pkl
    
    # Descargar el archivo pickle a una ubicación temporal local
    blob.download_to_filename(local_path)


def load_model(local_path):
    # Cargar el modelo entrenado desde el archivo pickle descargado
    with open(local_path, 'rb') as f:
        rf = pickle.load(f)
    return rf


def make_prediction(model, variables):
    # Crear una lista con las variables ingresadas
    new_variables = [[variables.sepal_length, variables.sepal_width, variables.petal_length, variables.petal_width]]
    
    # Realizar la predicción utilizando el modelo cargado
    prediction = int(model.predict(new_variables)[0])
    return prediction