from fastapi import FastAPI
from pydantic import BaseModel

# Definición del modelo de datos utilizando Pydantic
class Persona(BaseModel):
    nombre: str
    edad: int

# Creación de la aplicación FastAPI
app = FastAPI()

# Ruta de inicio que retorna un saludo
@app.get('/')
def index():
    return 'Hello world'

# Ruta que retorna un mensaje específico
@app.get('/ruta-uno')
def ruta_uno():
    return 'ruta uno'

# Ruta que recibe un parámetro en la URL y lo utiliza en la respuesta
@app.get('/ejemplo-parametro/{parametro}')
def ejemplo_parametro(parametro):
    return {f'ejemplo con {parametro}'}

# Ruta que recibe un parámetro de tipo entero en la URL y lo utiliza en la respuesta
@app.get('/ejemplo-parametro-con-tipo/{parametro}')
def ejemplo_parametro(parametro: int):
    return {f'ejemplo con {parametro}'}

# Ruta que utiliza el método POST para agregar un usuario con los datos proporcionados en el cuerpo de la solicitud
# Se utiliza el modelo Persona definido para validar y deserializar los datos
@app.post('/agregar-usuario')
def add_user(persona: Persona):
    return {'usuario agregado, con nombre: ': persona.nombre, 'y edad: ': persona.edad}

# Punto de entrada para iniciar el servidor
# Ejecutar por consola: uvicorn main:app --reload
# - main: nombre del archivo con la aplicación
# - app: nombre con el que se instanció FastAPI
# - --reload: opción para recargar automáticamente el servidor al hacer cambios
