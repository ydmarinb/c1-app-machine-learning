import os
import pickle
import glob

def predict(request):
    variables = request.get_json()

    print(variables)
    print(variables['sepal_length'])

    # Cargar el último modelo desde el almacenamiento local
    model = load_latest_model()  

    # Realizar la predicción utilizando el modelo cargado
    prediction = make_prediction(model, variables)

    # Retornar la predicción como resultado de la función
    return {'prediction': prediction}

def load_latest_model():
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
    new_variables = [[variables['sepal_length'], variables['sepal_width'], variables['petal_length'], variables['petal_width']]]

    # Realizar la predicción utilizando el modelo cargado
    prediction = int(model.predict(new_variables)[0])
    return prediction

# Entrypoint function for Cloud Function
def entry_point(request):
    return predict(request)
