from backend.params import fetch_url, api_key
from backend.processor import Processor
import requests

class Fetcher():
    """
    A class to fetch and return data from Yahoo finance API.

    ...

    Attributes
    ----------
    URL : str
        The Yahoo finance URL to fetch data from

    api_key : str
        The API key to use in the request header to Yahoo finance API

    headers : dict
        A dictionary formulated from api_key to use as a header when requesting from Yahoo Finance API

    Methods
    ----------
    get_data(data=""):
        Scrapes json response for specific metrics and prints based on a set of requirements
    
    fetch(data=""):
        Fetches data from Yahoo Finance API
    """
    
    def __init__(self):
        self.url = fetch_url
        self.api_key = api_key
        self.headers = {
    'x-api-key': self.api_key
    }


    def get_data(self,data):
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

                #if 0 < stock_peg_ratio < 2 and 0 < stock_pe_ratio < 5 and stock_eps_percent_change > 10:
                    print(
                        f"{stock} is currently at {stock_price} per share.\nCurrent EPS {stock_eps_current} -1y:"
                        f" {stock_eps_trailing} +1y: {stock_eps_forward} +1y % change prediction: "
                        f"{stock_eps_percent_change}\nP/E Ratio (Lower the Better): {stock_pe_ratio} P"
                        f"EG Ratio (Lower the Better): {stock_peg_ratio}\n\n\n\n")
            except:
                pass

    def fetch(self,data):
        for symbol in data:
            symbol_list = {"symbols": symbol}
            response = requests.request("GET", self.url, headers=self.headers, params=symbol_list)
            response.raise_for_status()
            jsonResponse = response.json()
            formatted_data = jsonResponse["quoteResponse"]["result"]
            self.get_data(formatted_data)
