from secrets import fetch_url, api_key
from processor import industries
import requests

class Fetcher():
    def __init__(self):
        self.url = fetch_url
        self.api_key = api_key
        self.headers = {
    'x-api-key': self.api_key
    }


    def get_data(data):
        for index in range(len(data)):
            try:
                for key in (data[index]):
                    stock = data[index]["shortName"]
                    stock_price = data[index]["regularMarketPrice"]
                    stock_eps_current = data[index]["epsCurrentYear"]
                    stock_eps_forward = data[index]["epsForward"]
                    stock_eps_trailing = data[index]["epsTrailingTwelveMonths"]
                    stock_forward_price_earnings = data[index]["forwardPE"]
                    stock_200_day_avg_change_percent = data[index]["twoHundredDayAverageChangePercent"]
                    stock_pe_ratio = (stock_price / stock_eps_trailing)
                    stock_forward_pe_ratio = (stock_price / stock_eps_current)
                    stock_eps_percent_change = ((stock_eps_forward - stock_eps_current) / (
                            (stock_eps_forward + stock_eps_current) / 2)) * 100
                    stock_peg_ratio = stock_pe_ratio / stock_eps_percent_change

                if 0 < stock_peg_ratio < 2 and 0 < stock_pe_ratio < 5 and stock_eps_percent_change > 10:
                    print(
                        f"{stock} is currently at {stock_price} per share.\nCurrent EPS {stock_eps_current} -1y:"
                        f" {stock_eps_trailing} +1y: {stock_eps_forward} +1y % change prediction: "
                        f"{stock_eps_percent_change}\nP/E Ratio (Lower the Better): {stock_pe_ratio} P"
                        f"EG Ratio (Lower the Better): {stock_peg_ratio}\n\n\n\n")
            except:
                pass

    def fetch(self):
        for industry in industries:
            sp500_list = {"symbols": industry}
            response_sp500 = requests.request("GET", self.fetch_url, headers=self.headers, params=sp500_list)
            response_sp500.raise_for_status()
            sp_500_jsonResponse = response_sp500.json()
            data = sp_500_jsonResponse["quoteResponse"]["result"]
            get_data(data)
