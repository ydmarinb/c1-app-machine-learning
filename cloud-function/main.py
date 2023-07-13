from fastapi import FastAPI
from pydantic import BaseModel
import pickle

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
    # Cargar el modelo entrenado
    rf = load_model()
    
    # Realizar la predicción utilizando el modelo cargado
    prediction = make_prediction(rf, variables)
    
    # Retornar la predicción como resultado de la función
    return {'prediction': prediction}


def load_model():
    # Cargar el modelo entrenado desde el archivo pickle
    with open('model_v1.pkl', 'rb') as f:
        rf = pickle.load(f)
    return rf


def make_prediction(model, variables):
    # Crear una lista con las variables ingresadas
    new_variables = [[variables.sepal_length, variables.sepal_width, variables.petal_length, variables.petal_width]]
    
    # Realizar la predicción utilizando el modelo cargado
    prediction = int(model.predict(new_variables)[0])
    return prediction

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)