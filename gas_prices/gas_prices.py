from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from gas_prices.config import URL, QUERY_STATION_ID, QUERY_PRICES

class GasPrices:
    def __init__(self, url=URL):
        transport = AIOHTTPTransport(url=url)
        self.client = Client(transport=transport)

    def get_station_id_by_zip(self, zip_code):
        query = gql(QUERY_STATION_ID)

        variables = {
            "maxAge": 0,
            "zip": zip_code
        }

        response = self.client.execute(query, variable_values=variables)
        return response

    def get_gas_prices_by_station_id(self, station_id):
        query = gql(QUERY_PRICES)

        variables = {
          "id": station_id
        }

        response = self.client.execute(query, variable_values=variables)

        regular_price_today = response["station"]["prices"][0]["credit"]["price"]
        return regular_price_today
