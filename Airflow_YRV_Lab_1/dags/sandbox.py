from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Define default args applicable to all tasks in the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

# Define the Python callable
def say_hello(name):
    print(f"Hello, {name} – Airflow is orchestrating successfully!")

with DAG(
    dag_id='sandbox_dag',
    default_args=default_args,
    description='A simple sandbox DAG using BashOperator and PythonOperator',
    schedule_interval='0 9 * * *',  # crontab: every day at 9 AM
    start_date=datetime(2025, 10, 19),
    catchup=False,
    tags=['sandbox', 'demo']
) as dag:

    # BashOperator task
    t1 = BashOperator(
        task_id='bash_task',
        bash_command='echo "This is a Bash command running inside Airflow!"'
    )

    # PythonOperator task with params
    t2 = PythonOperator(
        task_id='python_task',
        python_callable=say_hello,
        op_kwargs={'name': 'Yashwanth'}
    )

    # Task dependencies
    t1 >> t2
