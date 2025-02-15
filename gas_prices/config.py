# config.py
URL = "https://www.gasbuddy.com/graphql/"
TEST_URL = "https://www.gasbuddy.com/graphql/"

QUERY_STATION_ID = """
query LocationBySearchTerm($brandId: Int, $cursor: String, $maxAge: Int, $search: String) {
  locationBySearchTerm(search: $search) {
    stations(brandId: $brandId, cursor: $cursor, maxAge: $maxAge) {
      count
      cursor {
        next
      }
      results {
        address {
          country
          line1
          line2
          locality
          postalCode
          region
        }
        fuels
        id
        name
        prices {
          cash {
            nickname
            postedTime
            price
          }
          credit {
            nickname
            postedTime
            price
          }
        }
      }
    }
    trends {
      areaName
      country
      today
      todayLow
      trend
    }
  }
}
"""

QUERY_PRICES = """
query GetStation($id: ID!) {
  station(id: $id) {
    prices {
      credit {
        nickname
        postedTime
        price
      }
    }
  }
}
"""