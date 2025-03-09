from dotenv import load_dotenv
load_dotenv(dotenv_path="/home/admin/gas-prices/.env")
from datetime import datetime
from gas_prices.gas_prices import GasPrices
from gas_prices.slack import send_slack_message
from gas_prices.influx_db import write_influxdb

if __name__ == "__main__":
    GasObj = GasPrices()

    slack_str = ""

    loc1_gas_price = GasObj.get_gas_prices_by_station_id("3103")
    loc2_gas_price = GasObj.get_gas_prices_by_station_id("35713")
    loc3_gas_price = GasObj.get_gas_prices_by_station_id("3366")
    print("Gas Prices queried:", datetime.now())

    data = [
        {
            "location": "Pacific Commons",
            "price": loc1_gas_price,
        },
        {
            "location": "Automation",
            "price": loc2_gas_price,
        },
        {
            "location": "Coleman",
            "price": loc3_gas_price,
        },
    ]

    send_slack_message(data)
    print("Gas Prices sent to Slack:", datetime.now())
    write_influxdb(data)
    print("Gas Prices written to InfluxDB:", datetime.now())
