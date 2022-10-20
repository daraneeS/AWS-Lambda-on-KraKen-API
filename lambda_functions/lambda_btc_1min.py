# add a zip file of requests module for requests layer
# add AWSSDKPandas-Python39 layer for pandas

import json
import requests
from datetime import datetime, time
import pandas as pd
import boto3
from io import StringIO

bucket = "bucket_name"

def lambda_handler(event, context):
    
    resp = requests.get('https://api.kraken.com/0/public/OHLC?pair=XBTUSD&interval=1&since=unix_now').json()

    kraken_ohlc_cols = ["date","open", "high", "low", "close", "vwap","volume", "trades"]
    
    df = pd.DataFrame([resp['result']['XXBTZUSD'][-1]], columns=kraken_ohlc_cols)

    df["date"] = pd.to_datetime(df["date"],unit='s')
    
    print(df)
    
    csv_buffer = StringIO()
    df.to_csv(csv_buffer)
    s3_resource = boto3.resource('s3')
    file_name = datetime.now().strftime("%Y%m%d-%H%M%S")
    s3_resource.Object(bucket, f'btc_{file_name}.csv').put(Body=csv_buffer.getvalue())
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
