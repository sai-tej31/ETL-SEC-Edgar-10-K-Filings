# Project Documentation: 10k-download

## Table of Contents

- [Project Documentation: 10k-download](#project-documentation-10k-download)
  - [Table of Contents](#table-of-contents)
  - [1. Overview ](#1-overview-)
  - [2. Folder Structure ](#2-folder-structure-)
  - [3. Module: TickerFilesCollector ](#3-module-tickerfilescollector-)
    - [Methods:](#methods)
  - [4. Module: collect\_ticker\_files ](#4-module-collect_ticker_files-)
    - [Function:](#function)
  - [5. Module: get\_ticker\_10k\_filings ](#5-module-get_ticker_10k_filings-)
    - [Function:](#function-1)
  - [6. Usage Examples ](#6-usage-examples-)
  - [7. License ](#7-license-)
  - [8. Contributing ](#8-contributing-)
  - [9. Acknowledgments ](#9-acknowledgments-)

---

## 1. Overview <a name="overview"></a>

The 10k-download project provides utilities for downloading, collecting, and organizing 10-K filings for various companies from the SEC Edgar website. It consists of modules that facilitate file collection, 10-K download, and usage examples for a smooth experience.

---

## 2. Folder Structure <a name="folder-structure"></a>

```
myenv/
playground.ipynb
requirements.txt
utils/
|-- TickerFilesCollector.py
|-- __init__.py
```

- **`myenv/`**: Virtual environment directory for managing project dependencies.
- **`playground.ipynb`**: A Jupyter notebook for testing and usage examples.
- **`requirements.txt`**: A text file containing required Python packages.
- **`utils/`**: A directory containing utility modules.
  - **`TickerFilesCollector.py`**: Module for collecting ticker files.
  - **`__init__.py`**: Initialization file for the `utils` package.

---

## 3. Module: TickerFilesCollector <a name="module-tickerfilescollector"></a>

The `TickerFilesCollector` class in the `TickerFilesCollector.py` module is responsible for collecting and organizing ticker files from the specified data folder.

### Methods:

- `__init__(self, root_folder)`: Initializes a `TickerFilesCollector` object.
- `_collect_files(self, root_folder)`: Collects all TXT, HTML, and XML files inside the `root_folder` and its subfolders.
- `_get_ticker_files(self, root_folder, ticker)`: Collects all TXT, HTML, and XML files for a specific ticker and stores them in a dictionary.
- `get_all_ticker_files(self)`: Collects all TXT, HTML, and XML files for all tickers in the `root_folder`.

---

## 4. Module: collect_ticker_files <a name="module-collect_ticker_files"></a>

The `collect_ticker_files.py` module provides the `collect_ticker_files` function, which is responsible for collecting and organizing ticker files from the specified data folder for all tickers.

### Function:

- `collect_ticker_files(data_folder='data/sec-edgar-filings')`: Collects and organizes ticker files from the specified data folder for all tickers.

---

## 5. Module: get_ticker_10k_filings <a name="module-get_ticker_10k_filings"></a>

The `get_ticker_10k_filings.py` module provides the `get_ticker_10k_filings` function, which downloads all the 10-K filings for a given ticker from the SEC Edgar website.

### Function:

- `get_ticker_10k_filings(ticker)`: Downloads all the 10-K filings for a given `ticker` from the SEC Edgar website.

---

## 6. Usage Examples <a name="usage-examples"></a>

For detailed usage examples and demonstration of the project functionalities, refer to the `playground.ipynb` Jupyter notebook in the root directory.

---

## 7. License <a name="license"></a>

This project is licensed under the [MIT License](LICENSE).

---

## 8. Contributing <a name="contributing"></a>

If you wish to contribute to this project, please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 9. Acknowledgments <a name="acknowledgments"></a>

Special thanks to all the contributors who have contributed to this project.

---