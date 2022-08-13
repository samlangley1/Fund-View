fetch_url = "https://yfapi.net/v6/finance/quote"
api_key = "YOUR_API_KEY"

# The plan that your API key relates to (Choose one of "BASIC", "PRO", "ULTRA", "MEGA")
subscription_plan = "BASIC"


# False will display all scraped stocks, True will only show scraped stocks that meet the criteria defined in fetcher.py
alert_only = False



# Throttles outgoing API calls to avoid potential IP ban *Recommended*
throttle = True