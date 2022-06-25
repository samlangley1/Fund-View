import requests
import pandas as pd

url = "https://yfapi.net/v6/finance/quote"

consumer_discretionary = pd.read_csv("data/sp-sectors/sp-sectors-consumer-discretionary.csv")
consumer_discretionary = consumer_discretionary["Symbol"].to_list()
consumer_discretionary = ",".join(consumer_discretionary)

consumer_staples = pd.read_csv("data/sp-sectors/sp-sectors-consumer-staples.csv")
consumer_staples = consumer_staples["Symbol"].to_list()
consumer_staples = ",".join(consumer_staples)

energy = pd.read_csv("data/sp-sectors/sp-sectors-energy.csv")
energy = energy["Symbol"].to_list()
energy = ",".join(energy)

financial = pd.read_csv("data/sp-sectors/sp-sectors-financial.csv")
financial = financial["Symbol"].to_list()
financial = ",".join(financial)

health_care = pd.read_csv("data/sp-sectors/sp-sectors-health-care.csv")
health_care = health_care["Symbol"].to_list()
health_care = ",".join(health_care)

industrials = pd.read_csv("data/sp-sectors/sp-sectors-industrials.csv")
industrials = industrials["Symbol"].to_list()
industrials = ",".join(industrials)

information_technology = pd.read_csv("data/sp-sectors/sp-sectors-information-technology.csv")
information_technology = information_technology["Symbol"].to_list()
information_technology = ",".join(information_technology)

materials = pd.read_csv("data/sp-sectors/sp-sectors-materials.csv")
materials = materials["Symbol"].to_list()
materials = ",".join(materials)

real_estate = pd.read_csv("data/sp-sectors/sp-sectors-real-estate.csv")
real_estate = real_estate["Symbol"].to_list()
real_estate = ",".join(real_estate)

telecom_services = pd.read_csv("data/sp-sectors/sp-sectors-telecom-services.csv")
telecom_services = telecom_services["Symbol"].to_list()
telecom_services = ",".join(telecom_services)

utility = pd.read_csv("data/sp-sectors/sp-sectors-utility.csv")
utility = utility["Symbol"].to_list()
utility = ",".join(utility)

industries = [consumer_discretionary,consumer_staples,energy,financial,health_care,industrials,information_technology,materials,real_estate,telecom_services,utility]

headers = {
    'x-api-key': "DL5uQc7Pn1abSG5jTDfoB72g5fi8z5vz3eBjkW6z"
}


def get_data(data):
    # Iterates through each company listed in stock_list and returns the below values
    global stock_peg_ratio
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



for industry in industries:
    sp500_list = {"symbols": industry}
    response_sp500 = requests.request("GET", url, headers=headers, params=sp500_list)
    response_sp500.raise_for_status()
    sp_500_jsonResponse = response_sp500.json()
    data = sp_500_jsonResponse["quoteResponse"]["result"]
    get_data(data)

is_running = True

while is_running:
    get_data()
    break