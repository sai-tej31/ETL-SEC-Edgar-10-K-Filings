import os

class TickerFilesCollector:
    def __init__(self, root_folder):
        self.root_folder = root_folder
        self.ticker_files = {}

    def _collect_files(self, root_folder):
        # Collect all TXT and HTML files inside the root_folder and its subfolders
        collected_files = []
        try:
            for root, _, files in os.walk(root_folder):
                for file in files:
                    if file.endswith('.txt') or file.endswith('.html'):
                        collected_files.append(os.path.join(root, file))
        except Exception as e:
            print(f"Error occurred while collecting files: {e}")
        return collected_files

    def _get_ticker_files(self, root_folder, ticker):
        # Get a dictionary with 'ticker' as the key and list of associated files as the value
        ticker_files = {}
        try:
            ticker_files[ticker] = self._collect_files(root_folder)
        except Exception as e:
            print(f"Error occurred while getting files for {ticker}: {e}")
        return ticker_files

    def get_all_ticker_files(self):
        # Get a dictionary with company tickers as keys and their associated files as values
        try:
            for folder in os.listdir(self.root_folder):
                ticker_folder = os.path.join(self.root_folder, folder)
                if os.path.isdir(ticker_folder):
                    self.ticker_files.update(self._get_ticker_files(ticker_folder, folder))
        except Exception as e:
            print(f"Error occurred while getting all ticker files: {e}")
        return self.ticker_files