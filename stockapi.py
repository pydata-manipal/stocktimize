import requests
import pandas as pd
import csv
import sys
from io import StringIO

def getStockData(ticker,size):
    apikeyFile = open('apiKey','r')
    apikey = str(apikeyFile.readline())

    baseURL = 'https://www.alphavantage.co/query'


    PARAMS = {
        'outputsize':size,
        'apikey'    :apikey,
        'symbol'    :ticker,
        'function'  :'TIME_SERIES_DAILY_ADJUSTED',
        'datatype'  :'csv'
    }
    
    data = requests.get(baseURL,PARAMS).text
    data = StringIO(data)
    stock = pd.read_csv(data)
    dropColumns = ['open','high','low','close','volume','dividend_amount','split_coefficient']
    stock.drop(dropColumns,axis=1,inplace=True)
    stock['timestamp'] = pd.to_datetime(stock['timestamp'])
    stock.set_index('timestamp',inplace=True)


    return stock

