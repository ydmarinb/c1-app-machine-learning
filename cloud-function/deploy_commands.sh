#gcloud functions deploy my-fastapi-function \  # Nombre de la función en Cloud Functions
#  --runtime python310 \  # Versión de Python a utilizar
#  --trigger-http \  # Configurar un desencadenador HTTP para la función
#  --allow-unauthenticated \  # Permitir acceso no autenticado a la función
#  --entry-point=predict  \  # Punto de entrada de la aplicación FastAPI
#  --source=.  # Directorio fuente para el despliegue


gcloud functions deploy app-model-v1 \
  --runtime python310 \
  --trigger-http \
  --allow-unauthenticated \
  --source=. \
  --entry-point entry_point 

