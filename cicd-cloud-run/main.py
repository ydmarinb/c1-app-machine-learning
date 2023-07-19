from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from google.cloud import storage
import pickle
import os
import glob

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Definir el modelo de datos utilizando Pydantic
class Variables(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Ruta POST para la predicción
@app.post("/")
def predict(variables: Variables):
    # Verificar si el archivo pickle del modelo ya está descargado localmente
    
    download_model(local_path)

    # Cargar el modelo entrenado desde el archivo pickle descargado
    rf = load_model()

    # Realizar la predicción utilizando el modelo cargado
    prediction = make_prediction(rf, variables)

    # Retornar la predicción como resultado de la función
    return JSONResponse({"prediction": prediction})

# Ruta GET para la información del usuario
@app.get("/user-informacion", response_class=HTMLResponse)
def user_informacion():
    # HTML con la información detallada de la API
    html_content = """
    <html>
    <head>
        <title>Información de la API</title>
    </head>
    <body>
        <h1>API de Predicción de Flores</h1>
        <p>Esta API permite realizar predicciones sobre características de flores utilizando un modelo de aprendizaje automático.</p>
        <h2>Uso de la API</h2>
        <p>Para realizar una predicción, envía una solicitud POST a la siguiente URL: <strong>/</strong></p>
        <p>El cuerpo de la solicitud debe ser un objeto JSON con las siguientes características de la flor:</p>
        <pre>
        {
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        }
        </pre>
        <h2>Respuesta</h2>
        <p>La API devuelve una respuesta JSON con la predicción realizada:</p>
        <pre>
        {
            "prediction": 0
        }
        </pre>
        <p>La predicción es un número que representa la clase de la flor.</p>
    </body>
    </html>
    """
    return html_content

def download_model(local_path):
    # Verificar si se proporcionó un archivo de credenciales JSON
    if "GOOGLE_APPLICATION_CREDENTIALS" in os.environ:
        # Crear una instancia del cliente de almacenamiento de Cloud Storage con autenticación por credenciales
        client = storage.Client()
    else:
        # Crear una instancia del cliente de almacenamiento de Cloud Storage con autenticación predeterminada
        client = storage.Client.from_service_account_json("credentials.json")  # Reemplazar 'ruta-al-archivo-credenciales.json' con la ruta real del archivo de credenciales JSON

    # Obtén el bucket
    bucket = client.get_bucket(bucket_name)

    # Obtén la lista de blobs (archivos) en el bucket
    blobs = list(bucket.list_blobs())

    # Ordena los blobs por fecha de creación de forma descendente
    blobs.sort(key=lambda x: x.time_created, reverse=True) 

    if len(blobs) > 0:
        latest_blob = blobs[0]
        file_name = latest_blob.name

        # Descarga el archivo en la carpeta de destino
        destination_path = f"{file_name}"
        latest_blob.download_to_filename(destination_path)
        print(f"Archivo descargado: {file_name}")
    else:
        print("No se encontraron archivos en el bucket")


def load_model(local_path):
    # Obtener la lista de archivos `pkl` en el directorio
    pkl_files = glob.glob('*.pkl')

    if pkl_files:
        latest_model_file = pkl_files[0]   

        # Cargar el último modelo `pkl`
        with open(latest_model_file, 'rb') as f:
            model = pickle.load(f)

        return model
    else:
        raise Exception("No se encontró ningún archivo pkl en el directorio")


def make_prediction(model, variables):
    # Crear una lista con las variables ingresadas
    new_variables = [[variables.sepal_length, variables.sepal_width, variables.petal_length, variables.petal_width]]

    # Realizar la predicción utilizando el modelo cargado
    prediction = int(model.predict(new_variables)[0])
    return prediction


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)

# pip freeze > requirements.txt
