from google.cloud import storage
import os



def download_model(local_path, model_name):
    # Verificar si se proporcionó un archivo de credenciales JSON
    if 'GOOGLE_APPLICATION_CREDENTIALS' in os.environ:
        # Crear una instancia del cliente de almacenamiento de Cloud Storage con autenticación por credenciales
        client = storage.Client()
    else:
        # Crear una instancia del cliente de almacenamiento de Cloud Storage con autenticación predeterminada
        client = storage.Client.from_service_account_json('credentials.json')  # Reemplazar 'ruta-al-archivo-credenciales.json' con la ruta real del archivo de credenciales JSON
    
    # Obtener el objeto de almacenamiento del archivo pickle desde el bucket
    bucket = client.get_bucket('registry-models')  # Reemplazar 'nombre-del-bucket' con el nombre real del bucket
    blob = bucket.blob(model_name)  # Reemplazar 'ruta-al-archivo' con la ruta real del archivo pkl
    
    # Descargar el archivo pickle a una ubicación temporal local
    blob.download_to_filename(local_path)

if __name__ == "__main__":
    model_name = 'model_v1.pkl'
    local_path = f'cloud-function/{model_name}'
    download_model(local_path, model_name)