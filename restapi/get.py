import requests
import pandas as pd

url = "https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/all_transactions.json"










response = requests.get(url).json()
print(response)