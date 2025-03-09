import os, time
from influxdb_client_3 import InfluxDBClient3, Point

token = os.environ.get("INFLUXDB_TOKEN")
org = os.environ.get("INFLUXDB_ORG")
host = "https://us-east-1-1.aws.cloud2.influxdata.com"

def write_influxdb(data):
    client = InfluxDBClient3(host=host, token=token, org=org)

    database="gas_prices"

    # write all data in a single point
    point = (
        Point("gas_prices")
        .field(data[0]["location"] , data[0]["price"])
        .field(data[1]["location"] , data[1]["price"])
        .field(data[2]["location"] , data[2]["price"])
        .time(time.time_ns())
    )
    
    client.write(database=database, record=point)
