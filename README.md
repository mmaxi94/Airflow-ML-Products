# Airflow-ML-Products

Se construye un simple data pipeline que obtiene las primeras 5 publicaciones de un determinado producto de Mercadolibre y genera un .txt comprimido con dicha informacion.

El producto se debe setear en una variable global de Airflow (ver [variable_global.jpg](https://i.imgur.com/P7hPiFO.jpg) en este caso se desea buscar un samsung s21+) que luego es capturada por la task.
El DAG esta scheduleado para que se ejecute diariamente y contiene 2 tareas: una primer operador de python que obtiene los datos desde la API de Mercadolibre y por ultimo una dependencia con un operador de bash que solo va a comprimir el txt generado previamente.
El archivo de salida es un txt delimitado por pipe que contiene header y se aloja dentro de la carpeta /opt/airflow/plugins/ (ver [archivo_salida.jpg](https://i.imgur.com/SpEXApo.jpeg))
