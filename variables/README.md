# Variables

Keep JSON variable files for Apache Airflow in this directory.

For example, to keep tokens for `alexa_time_check` DAG. Create a file names `alexa_time_check.json` and add the following as its content. Replace the values as needed.

```json
{
    "alexa_time_check": {
        "access_token": "<access_token>",
        "secret_token": "<secret_token>",
        "monkey": "<voicemonkey_id>"
    }
}
```
