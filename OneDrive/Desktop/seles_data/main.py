from flask import Flask
from google.cloud import bigquery

app = Flask(__name__)

@app.route("/")
def load_data():

    client = bigquery.Client()

    uri = "gs://sale-data-bkt/sales.txt"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True
    )

    load_job = client.load_table_from_uri(
        uri,
        "project-77158318-bf9d-4d5d-bcc.gcp_project.sales_data",
        job_config=job_config
    )

    load_job.result()

    return "Data Loaded Successfully"