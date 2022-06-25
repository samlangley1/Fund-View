import pandas as pd

processed_data = []

class Processor():
    def __init__(self):
        self.processed_data = processed_data


    def processdata(data):
        for i in data:
            raw_data = pd.read_csv(data[i])
            raw_data = raw_data["Symbol"].to_list()
            for i in raw_data:
                if len(i) > 4:
                    raw_data.remove(i)
            processed_data +=raw_data