from flask import Flask
from google.cloud import bigquery

app = Flask(__name__)

@app.route("/")
def load_data():

    client = bigquery.Client()

    uri = "gs://sale-data-bkt/sales.txt"
    job = client.load_table_from_uri(
        uri,
        "project-77158318-bf9d-4d5d-bcc.gcp_project.sales_data"
    )

    job.result()

    return "Data Loaded Successfully"