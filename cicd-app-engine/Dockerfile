# Usa la imagen base de Python 3.11 slim
FROM python:3.11-slim

# Establece el directorio de trabajo para la aplicación
ENV APP_HOME /app
WORKDIR $APP_HOME

# Copia el contenido del directorio actual al contenedor en la ruta especificada
COPY . ./

# Instala las dependencias de Python especificadas en el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8080 para que Cloud Run pueda acceder a la aplicación
EXPOSE 8080

# Especifica el comando que se ejecutará al iniciar el contenedor
CMD uvicorn main:app --host 0.0.0.0 --port 8080
