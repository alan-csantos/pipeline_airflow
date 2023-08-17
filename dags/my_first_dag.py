from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    'meu_primeiro_dag',
    start_date = days_ago(1),
    schedule_interval = '@daily',
) as dag:
    
    tarefa_1 = EmptyOperator(task_id = 'Tarefa_1')
    tarefa_2 = EmptyOperator(task_id = 'Tarefa_2')
    tarefa_3 = EmptyOperator(task_id = 'Tarefa_3')
    tarefa_4 = BashOperator(task_id = 'cria_pasta',
                            bash_command= 'mkdir -p "/home/alan/repos/pipeline_airflow/dags/pasta_tarefa"')
    
    tarefa_1 >> [tarefa_2, tarefa_3]
    tarefa_3 >> tarefa_4