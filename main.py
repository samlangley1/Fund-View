from backend.processor import Processor,processed_data
from backend.fetcher import Fetcher

if __name__ == "__main__":
    Processor.processdata(data={
        "consumer_discretionary":"./data/sp-sectors/sp-sectors-consumer-discretionary.csv",
        "consumer_staples":"./data/sp-sectors/sp-sectors-consumer-staples.csv",
        "energy":"./data/sp-sectors/sp-sectors-energy.csv",
        "financial":"./data/sp-sectors/sp-sectors-financial.csv",
        "health_care":"./data/sp-sectors/sp-sectors-health-care.csv",
        "industrials":"./data/sp-sectors/sp-sectors-industrials.csv",
        "information_technology":"./data/sp-sectors/sp-sectors-information-technology.csv",
        "materials":"./data/sp-sectors/sp-sectors-materials.csv",
        "real_estate":"./data/sp-sectors/sp-sectors-real-estate.csv",
        "telecom_services":"./data/sp-sectors/sp-sectors-telecom-services.csv",
        "utility":"./data/sp-sectors/sp-sectors-utility.csv"
        })

    Fetcher.get_data(processed_data)