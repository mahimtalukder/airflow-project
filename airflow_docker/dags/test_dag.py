from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'clickSpikes',
    'retries': 5,
    'retry_delay': timedelta(seconds=60)
}
with DAG(
    dag_id = "test_dag",
    default_args = default_args,
    description = "Tesing the project",
    start_date = datetime(2022, 9, 9, 11),
    schedule_interval = "@daily"
) as dag:
    task1 = BashOperator(
        task_id='testing',
        bash_command="echo hello world, this is the first task! Allhamdulilla"
    )

    task1
