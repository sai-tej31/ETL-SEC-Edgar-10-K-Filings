from utils.get_ticker_10k_filings import get_ticker_10k_filings 
from pyspark.sql import SparkSession
import logging
import pandas as pd
import time

# ticker_data = pd.read_csv("name_cik_mapped.csv")
# tickers = ticker_data['ticker'].dropna()




def call_api(ticker):
    try:
        get_ticker_10k_filings(ticker) # call API
        time.sleep(1)
    except Exception as e:
        logging.error(f"Error occurred for the ticker- {ticker}: {e}")
        return None



# Initialize Spark Session
spark = SparkSession.builder \
    .appName("File Downloading Task") \
    .config("spark.dynamicAllocation.enabled", "true") \
    .getOrCreate()

# Read CSV file
df = spark.read\
    .option("header","true")\
        .option("inferSchema","true")\
            .csv("name_cik_mapped.csv")

df = df.dropna()


# Select 'TickerSymbol' column and convert DataFrame to RDD
tickers_rdd = df.select("ticker").rdd.flatMap(lambda x: x)

# Apply the API call function to each ticker in parallel 
api_responses_rdd = tickers_rdd.map(call_api)


# Stop the SparkSession
spark.stop()



# for i in tickers:
#     print(i)
#     # print(get_ticker_10k_filings(i))
#     break  