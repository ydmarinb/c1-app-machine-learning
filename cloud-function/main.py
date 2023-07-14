import pickle


def predict(request):
    variables = request.get_json()

    print(variables)
    print(variables['sepal_length'])

    
    # Cargar el modelo desde el almacenamiento local por defecto
    model = load_model_locally()  

    # Realizar la predicción utilizando el modelo cargado
    prediction = make_prediction(model, variables)

    # Retornar la predicción como resultado de la función
    return {'prediction': prediction}

def load_model_locally():
    # Cargar el modelo entrenado desde el archivo pickle local
    
    with open('model_v1.pkl', 'rb') as f:
        model = pickle.load(f)

    return model

def make_prediction(model, variables):
    # Crear una lista con las variables ingresadas
    
    new_variables = [[variables['sepal_length'], variables['sepal_width'], variables['petal_length'], variables['petal_width']]]

    # Realizar la predicción utilizando el modelo cargado
    prediction = int(model.predict(new_variables)[0])
    return prediction

# Entrypoint function for Cloud Function
def entry_point(request):
    return predict(request)


# Correr el modelo desde local
'''
curl -m 70 -X POST https://us-central1-ydmarinb.cloudfunctions.net/app-model-v1 \
-H "Authorization: bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}'
'''

'''
curl -m 70 -X POST https://us-central1-ydmarinb.cloudfunctions.net/app-model-v1 -H "Authorization: bearer $(gcloud auth print-identity-token)" -H "Content-Type: application/json" -d '{
  "sepal_length": 6.1,
  "sepal_width": 2.9,
  "petal_length": 4.7,
  "petal_width": 1.4
}'
'''