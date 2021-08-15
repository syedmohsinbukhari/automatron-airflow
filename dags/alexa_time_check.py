import pytz

from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime as dt
from datetime import timedelta


args = {
    'owner': 'ElCid',
}


def make_time_string():
    return dt.now(
        pytz.timezone('Asia/Karachi')
    ).strftime('%-I %M %p').replace(' 0 ', ' ')


def make_voicemonkey_string():
    url = "https://api.voicemonkey.io/trigger"
    access_token = "{{ var.json.alexa_time_check.access_token }}"
    secret_token = "{{ var.json.alexa_time_check.secret_token }}"
    monkey = "{{ var.json.alexa_time_check.monkey }}"
    announcement = f"The time is {make_time_string()}".replace(' ', '%20')
    return f"curl -X GET -G '{url}' -d 'access_token={access_token}' " \
        + f"-d 'secret_token={secret_token}' -d 'monkey={monkey}' " \
        + f"-d 'announcement={announcement}'"


with DAG(
    dag_id='alexa_time_check',
    default_args=args,
    schedule_interval='* * * * *',
    start_date=dt.now(pytz.timezone('Asia/Karachi')) - timedelta(minutes=1),
    dagrun_timeout=timedelta(seconds=10),
    tags=['alexa', 'voice-monkey'],
    params={},
) as dag:

    voice_monkey_task = BashOperator(
        task_id='alexa_tells_time_using_voicemonkey',
        bash_command=f"{make_voicemonkey_string()}"
    )
