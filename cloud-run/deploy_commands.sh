
# docker build -t gcr.io/gcp-devops# El comando `docker build` construye una imagen de Docker a partir del directorio actual.
# El argumento `-t` especifica el nombre y la etiqueta de la imagen.
# En este caso, la imagen se llamará `gcr.io/ydmarinb/model_v1`.
docker build -t gcr.io/ydmarinb/modelv1 # ydmarinb -> nombre proyecto, model_v1 -> nombre imagen

# El comando `docker push` sube la imagen de Docker etiquetada a Google Container Registry.
# El argumento `gcr.io/ydmarinb/model_v1` especifica el nombre y la etiqueta de la imagen.
docker push gcr.io/ydmarinb/modelv1



# El comando `gcloud run deploy` crea un servicio de Cloud Run para una imagen de Docker.
gcloud run deploy modelv1 \
    # La bandera `--image` especifica la imagen de Docker que se usará para crear el servicio.
    --image gcr.io/ydmarinb/modelo_v1 \
    # La bandera `--platform` especifica la plataforma en la que se ejecutará el servicio. En este caso, la plataforma es `managed`, que significa que el servicio se ejecutará en Google Cloud Platform.
    --platform managed \
    # La bandera `--allow-unauthenticated` permite que el servicio se invoque sin autenticación.
    --allow-unauthenticated

