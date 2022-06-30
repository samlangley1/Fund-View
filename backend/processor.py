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
        self.processed_data = [['AAP', 'AMZN', 'APTV', 'AZO', 'BBWI', 'BBY', 'BKNG', 'BWA', 'CCL', 'CMG', 'CZR', 'DG', 'DHI', 'DLTR', 'DPZ', 'DRI', 'EBAY', 'ETSY', 'EXPE', 'F', 'GM', 'GPC', 'GRMN', 'HAS', 'HD', 'HLT', 'KMX', 'LEN', 'LKQ', 'LOW', 'LVS', 'MAR', 'MCD', 'MGM', 'MHK', 'NCLH', 'NKE', 'NVR', 'NWL', 'ORLY', 'PENN', 'PHM', 'POOL', 'PVH', 'RCL', 'RL', 'ROST', 'SBUX', 'TGT', 'TJX', 'TPR', 'TSCO', 'TSLA', 'UA', 'UAA', 'ULTA', 'VFC', 'WHR', 'WYNN', 'YUM', 'ADM', 'BF.B', 'CAG', 'CHD', 'CL', 'CLX', 'COST', 'CPB', 'EL', 'GIS', 'HRL', 'HSY', 'K', 'KHC', 'KMB', 'KO', 'KR', 'LW', 'MDLZ', 'MKC', 'MNST', 'MO', 'PEP', 'PG', 'PM', 'SJM', 'STZ', 'SYY', 'TAP', 'TSN', 'WBA', 'WMT', 'APA', 'BKR', 'COP', 'CTRA', 'CVX', 'DVN', 'EOG', 'FANG', 'HAL', 'HES', 'KMI', 'MPC', 'MRO', 'OKE', 'OXY', 'PSX', 'PXD', 'SLB', 'VLO', 'WMB', 'XOM', 'AFL', 'AIG', 'AIZ', 'AJG', 'ALL', 'AMP', 'AON', 'AXP', 'BAC', 'BEN', 'BK', 'BLK', 'BRO', 'C', 'CB', 'CBOE', 'CFG', 'CINF', 'CMA', 'CME', 'COF', 'DFS', 'FDS', 'FITB', 'FRC', 'GL', 'GS', 'HBAN', 'HIG', 'ICE', 'IVZ', 'JPM', 'KEY', 'L', 'LNC', 'MCO', 'MET', 'MKTX', 'MMC', 'MS', 'MSCI', 'MTB', 'NDAQ', 'NTRS', 'PFG', 'PGR', 'PNC', 'PRU', 'RE', 'RF', 'RJF', 'SBNY', 'SCHW', 'SIVB', 'SPGI', 'STT', 'SYF', 'TFC', 'TROW', 'TRV', 'USB', 'WFC', 'WRB', 'WTW', 'ZION', 'A', 'ABBV', 'ABC', 'ABMD', 'ABT', 'ALGN', 'AMGN', 'ANTM', 'BAX', 'BDX', 'BIIB', 'BIO', 'BMY', 'BSX', 'CAH', 'CERN', 'CI', 'CNC', 'COO', 'CRL', 'CTLT', 'CVS', 'DGX', 'DHR', 'DVA', 'DXCM', 'EW', 'GILD', 'HCA', 'HOLX', 'HSIC', 'HUM', 'IDXX', 'ILMN', 'INCY', 'IQV', 'ISRG', 'JNJ', 'LH', 'LLY', 'MCK', 'MDT', 'MOH', 'MRK', 'MRNA', 'MTD', 'OGN', 'PFE', 'PKI', 'REGN', 'RMD', 'STE', 'SYK', 'TECH', 'TFX', 'TMO', 'UHS', 'UNH', 'VRTX', 'VTRS', 'WAT', 'WST', 'XRAY', 'ZBH', 'ZTS', 'AAL', 'ALK', 'ALLE', 'AME', 'AOS', 'BA', 'CARR', 'CAT', 'CHRW', 'CMI', 'CPRT', 'CSX', 'CTAS', 'DAL', 'DE', 'DOV', 'EFX', 'EMR', 'ETN', 'EXPD', 'FAST', 'FBHS', 'FDX', 'FTV', 'GD', 'GE', 'GNRC', 'GWW', 'HII', 'HON', 'HWM', 'IEX', 'IR', 'ITW', 'J', 'JBHT', 'JCI', 'LDOS', 'LHX', 'LMT', 'LUV', 'MAS', 'MMM', 'NDSN', 'NLSN', 'NOC', 'NSC', 'ODFL', 'OTIS', 'PCAR', 'PH', 'PNR', 'PWR', 'RHI', 'ROK', 'ROL', 'ROP', 'RSG', 'RTX', 'SNA', 'SPGI', 'SWK', 'TDG', 'TT', 'TXT', 'UAL', 'UNP', 'UPS', 'URI', 'VRSK', 'WAB', 'WM', 'XYL', 'AAPL', 'ACN', 'ADBE', 'ADI', 'ADP', 'ADSK', 'AKAM', 'AMAT', 'AMD', 'ANET', 'ANSS', 'APH', 'AVGO', 'BR', 'CDAY', 'CDNS', 'CDW', 'CRM', 'CSCO', 'CTSH', 'CTXS', 'DXC', 'ENPH', 'EPAM', 'FFIV', 'FIS', 'FISV', 'FLT', 'FTNT', 'GLW', 'GPN', 'HPE', 'HPQ', 'IBM', 'INTC', 'INTU', 'IPGP', 'IT', 'JKHY', 'JNPR', 'KEYS', 'KLAC', 'LRCX', 'MA', 'MCHP', 'MPWR', 'MSFT', 'MSI', 'MU', 'NLOK', 'NOW', 'NTAP', 'NVDA', 'NXPI', 'ORCL', 'PAYC', 'PAYX', 'PTC', 'PYPL', 'QCOM', 'QRVO', 'SEDG', 'SNPS', 'STX', 'SWKS', 'TDY', 'TEL', 'TER', 'TRMB', 'TXN', 'TYL', 'V', 'VRSN', 'WDC', 'ZBRA', 'ALB', 'AMCR', 'APD', 'AVY', 'BLL', 'CE', 'CF', 'CTVA', 'DD', 'DOW', 'ECL', 'EMN', 'FCX', 'FMC', 'IFF', 'IP', 'LIN', 'LYB', 'MLM', 'MOS', 'NEM', 'NUE', 'PKG', 'PPG', 'SEE', 'SHW', 'VMC', 'WRK', 'AMT', 'ARE', 'AVB', 'BXP', 'CBRE', 'CCI', 'DLR', 'DRE', 'EQIX', 'EQR', 'ESS', 'EXR', 'FRT', 'HST', 'IRM', 'KIM', 'MAA', 'O', 'PEAK', 'PLD', 'PSA', 'REG', 'SBAC', 'SPG', 'UDR', 'VNO', 'VTR', 'WELL', 'WY', 'ATVI', 'CHTR', 'DIS', 'DISH', 'EA', 'FB', 'FOX', 'FOXA', 'GOOG', 'IPG', 'LUMN', 'LYV', 'MTCH', 'NFLX', 'NWS', 'NWSA', 'OMC', 'PARA', 'T', 'TMUS', 'TTWO', 'TWTR', 'VZ', 'AEE', 'AEP', 'AES', 'ATO', 'AWK', 'CEG', 'CMS', 'CNP', 'D', 'DTE', 'DUK', 'ED', 'EIX', 'ES', 'ETR', 'EVRG', 'EXC', 'FE', 'LNT', 'NEE', 'NI', 'NRG', 'PEG', 'PNW', 'PPL', 'SO', 'SRE', 'WEC', 'XEL']]


    def processdata(self,raw_data):
        for data in raw_data:
            new_data = pd.read_csv(raw_data[data])
            new_data = new_data["Symbol"].to_list()
            for symbol in new_data:
                if len(symbol) < 5:
                    self.processed_data.append(symbol)