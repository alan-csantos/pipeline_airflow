from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator

def comprimentos():
    print("Boas Vindas ao Airflow!")

with DAG(
    "atividade_aula4",
    start_date=days_ago(1),
    schedule_interval="@daily"
) as dag:
    tarefa = PythonOperator(
        task_id="comprimentos",
        python_callable=comprimentos
    )
