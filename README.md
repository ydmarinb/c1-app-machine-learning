|                   | Cloud Functions             | Cloud Run                      | App Engine              |
|-------------------|-----------------------------|--------------------------------|-------------------------|
| Propósito         | Ejecutar funciones pequeñas y basadas en eventos | Ejecutar contenedores sin estado    | Implementar y gestionar aplicaciones |
| Método de implementación | Implementar funciones            | Implementar contenedores               | Implementar aplicaciones     |
| Escalado automático       | Escalado automático basado en eventos | Escalado automático basado en el tráfico | Escalado automático basado en la demanda |
| Facturación           | Pagar solo por las invocaciones de la función | Pagar por el uso del contenedor        | Pagar por horas de instancia  |
| Soporte de lenguaje  | Múltiples opciones de lenguaje   | Cualquier lenguaje dentro de un contenedor | Múltiples opciones de lenguaje |
| Networking        | Acceso limitado a la red      | Acceso completo a la red             | Acceso limitado a la red   |
| Control de tiempo de ejecución   | Control limitado sobre el entorno de tiempo de ejecución | Configuración personalizada del tiempo de ejecución | Control limitado sobre el entorno de tiempo de ejecución |
| Velocidad de implementación  | Implementación extremadamente rápida   | Implementación rápida                 | Implementación rápida         |
| Flexibilidad       | Limitado a la ejecución de funciones | Puede ejecutar cualquier carga de trabajo HTTP sin estado | Implementación flexible de aplicaciones |
| Complejidad        | Más simple de configurar y gestionar | Configuración y gestión más complejas | Complejidad intermedia |
| Casos de uso         | Funciones basadas en eventos sin servidor | API HTTP sin estado y microservicios | Aplicaciones y servicios web |



* python -m pip install scikit-learn==1.2.1



# pip freeze > requirements.txt