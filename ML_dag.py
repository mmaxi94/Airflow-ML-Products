from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from dags.programs.ML_etl import get_products
from airflow.operators.bash import BashOperator


with DAG('ML_dag', start_date=datetime(2022, 1, 1), schedule_interval='@daily', catchup=False) as dag:
    task_a = PythonOperator(
        task_id="task_a",
        python_callable=get_products,
        op_kwargs={
            "producto": "{{ var.value.ML_dag_producto }}"        
        }    
    )

    task_b = BashOperator(
            task_id="task_b",
            bash_command="cd /opt/airflow/plugins/ ; gzip Productos.txt"
    )

    task_a >> task_b