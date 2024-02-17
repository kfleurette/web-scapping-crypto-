#This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def api_runner():
  global df

  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
    'start':'1',
    'limit':'5000',
    'convert':'USD'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '6dddbda7-9f70-470e-8cff-8480aa5b2361',
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(data)
  except (ConnectionError, Timeout, TooManyRedirects) as e:
   print(e)
    
  import pandas as pd

  #pd.set_option('display.max_columns',None)

  #normalize the data
  df = pd.json_normalize(data['data'])

  #add a timestamp

  df['timestamp'] = pd.to_datetime('now')

  if not os.path.isfile(r'C:\Users\user\Documents\API.csv'):
    df.to_csv(r'C:\Users\user\Documents\API.csv', header = 'column_names')
  else: 
    df.to_csv(r'C:\Users\user\Documents\API.csv', mode = 'a', header = False)

import os
from time import time
from time import sleep

for i in range(333):
  api_runner()
  print('API Runner completed')
  sleep(60)# sleep for 1 minute
exit()

df72 = pd.read_csv(r'C:\Users\user\Documents\API.csv', header = 'column_names')
df72

pd.set_option('display.float_format', lambda x:'%.5f' % x)

#df.groupby('name', sort= False)

df