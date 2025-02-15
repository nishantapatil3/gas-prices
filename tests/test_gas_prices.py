from gas_prices.gas_prices import GasPrices
from gas_prices.config import TEST_URL

def test_gas_prices():
    gas_prices = GasPrices(url=TEST_URL)
    station_id = "1234"
    response = gas_prices.get_gas_prices_by_station_id(station_id)
    assert response is not None