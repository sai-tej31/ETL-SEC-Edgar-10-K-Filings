import logging
from sec_edgar_downloader import Downloader


def get_ticker_10k_filings(ticker):
    # Create a downloader instance with the "data" folder as the destination
    dl = Downloader("data")

    try:
        # Get all 10-K filings for the specified ticker
        dl.get("10-K", ticker)
    except Exception as e:
        logging.error(
            f"Error occurred while downloading 10-K filings for {ticker}: {e}"
        )
