from utils.get_ticker_10k_filings import get_ticker_10k_filings 

import pandas as pd
ticker_data = pd.read_csv("name_cik_mapped.csv")
tickers = ticker_data['ticker'].dropna()
for i in tickers:
    print(get_ticker_10k_filings(i))
    break  