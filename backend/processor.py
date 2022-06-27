import pandas as pd

class Processor():
    """
    A class to process and format data from data_import to be used in request headers to Yahoo Finance API.

    ...

    Attributes
    ----------
    processed_data : list
        A list of symbols scraped from the "Symbols" column in data provided in data_import.

    Methods
    ----------
    processdata(raw_data=""):
        Pulls symbol data provided in data_import csv's and adds them to processed_data list.
    """

    def __init__(self):
        self.processed_data = []


    def processdata(self,raw_data):
        for data in raw_data:
            new_data = pd.read_csv(raw_data[data])
            new_data = new_data["Symbol"].to_list()
            for symbol in new_data:
                if len(symbol) < 5:
                    self.processed_data.append(symbol)