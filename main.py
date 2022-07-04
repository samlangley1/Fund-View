from backend.processor import Processor
from backend.fetcher import Fetcher

data_import = {
        # This is an example of a dict you would use to point to custom symbols in csv files
        # "consumer_discretionary":"./data/sp-sectors/sp-sectors-consumer-discretionary.csv",
        }

Processor = Processor()
Fetcher = Fetcher()

if __name__ == "__main__":
    Fetcher.fetch(Processor.processed_data)