from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")
from datetime import datetime
from gas_prices.gas_prices import GasPrices
from gas_prices.slack import send_slack_message

if __name__ == "__main__":
    GasObj = GasPrices()

    slack_str = ""

    a1_loc = "Costco in Fremont (43621 Pacific Commons Blvd)"
    a1 = GasObj.get_gas_prices_by_station_id("3103")
    resp = a1_loc + " : " + str(a1)
    slack_str += resp + "\n"

    a2_loc = "Costco in San Jose (1709 Automation Pkwy)"
    a2 = GasObj.get_gas_prices_by_station_id("35713")
    resp = a2_loc + " : " + str(a2)
    slack_str += resp + "\n"

    a3_loc = "Costco in Santa Clara (1601 Coleman Ave)"
    a3 = GasObj.get_gas_prices_by_station_id("3366")
    resp = a3_loc + " : " + str(a3)
    slack_str += resp + "\n"

    print("Gas Prices queried:", datetime.now())

    # send_slack_message(slack_str)
    send_slack_message(slack_str)
