import logging
from ticker_utils import TickerFilesCollector


def collect_ticker_files(data_folder, tickers):
    """
    Collects and organizes ticker files from the specified data folder for the given tickers.

    Parameters:
        data_folder (str): The path to the root folder where company files are located.
        tickers (list): A list of ticker symbols for which files should be collected.

    Returns:
        dict: A dictionary with company tickers as keys and lists of associated file paths as values.
    """
    try:
        # Create an instance of TickerFilesCollector
        ticker_collector = TickerFilesCollector(data_folder)

        # Get all ticker files from the collector
        all_ticker_files = ticker_collector.get_all_ticker_files()

        # Create a new dictionary with ticker symbols as keys and associated file paths as values
        collected_files_dict = {}
        for ticker in tickers:
            ticker_files = all_ticker_files.get(ticker, [])
            collected_files_dict[ticker] = ticker_files
            print(f"Files for {ticker}: {ticker_files}")

        return collected_files_dict

    except Exception as e:
        # Log the error message
        logging.error(f"Error occurred while collecting ticker files: {e}")
        return None


if __name__ == "__main__":
    # Set up logging configuration to save errors to a file
    logging.basicConfig(
        filename="error_log.txt",
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    data_folder = (
        "data/sec-edgar-filings"  # Replace this with the path to your data folder
    )
    tickers_to_collect = [
        "AAPL",
        "MSFT",
    ]  # Replace this with the desired list of tickers
    all_ticker_files = collect_ticker_files(data_folder, tickers_to_collect)
