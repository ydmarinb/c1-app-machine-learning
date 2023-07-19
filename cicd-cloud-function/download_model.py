from google.cloud import storage

def download_latest_file(bucket_name):
    # Crea una instancia del cliente de almacenamiento de Cloud Storage
    client = storage.Client()

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



if __name__ == "__main__":
    bucket_name = "registry-models"
    download_latest_file(bucket_name)
