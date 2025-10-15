from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'your_name',
    'start_date': datetime(2025, 1, 15),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'bash_operator_dag',
    default_args=default_args,
    description='A simple DAG with BashOperator',   
    catchup=False,
    schedule_interval=None,
) as dag:
  
  print_system_info = BashOperator(
        task_id='print_system_info',
        bash_command='bash {{ params.script_path}}',
        params = {'script_path': '/opt/airflow/dags/data/system_info.sh'},
    )