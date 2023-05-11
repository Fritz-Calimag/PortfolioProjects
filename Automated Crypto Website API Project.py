#!/usr/bin/env python
# coding: utf-8

# In[1]:


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'15',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'ebb0d8e5-89ef-4c99-a08b-7904edcb4394',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

#Put the following into Anaconda prompt to allow this code to pull data
#"jupyter notebook --NotebookApp.iopub_data_rate_limit=1e10"


# In[2]:


type(data)


# In[11]:


import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# In[4]:


#this normalizes the data and makes it organized to be viewed in a dataframe

df = pd.json_normalize(data['data'])
df['timestamp'] = pd.to_datetime('now',utc=True)
df


# In[39]:


def api_runner():
    global df
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'15',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'ebb0d8e5-89ef-4c99-a08b-7904edcb4394',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      #print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)

#Put the following into Anaconda prompt to allow this code to pull data
#"jupyter notebook --NotebookApp.iopub_data_rate_limit=1e10"

    #we will append the new data that came in to the old dataframe
    list_storage = []
    df2 = pd.json_normalize(data['data'])
    df2['timestamp'] = pd.to_datetime('now', utc=True)
    list_storage.append(df2)
    df = pd.concat(list_storage)
    
    import os
    path = r"D:/Ron/SQL training/Python automated crypto pull api/API.csv"
    
    if not os.path.isfile(path):
        df.to_csv(path, header='column_names')
    else:
        df.to_csv(path, mode='a', header=False)


# In[40]:


import os
from time import time
from time import sleep

#we pull the data within our limited api key (333 pulls per day)
for i in range(333):
    api_runner()
    print('API Runner ran successfully')
    sleep(60) #sleep for 1 minute
exit()


# In[41]:


import os
path = r"D:/Ron/SQL training/Python automated crypto pull api/API.csv"
df72 = pd.read_csv(path)
df72


# In[42]:


df


# In[43]:


pd.set_option('display.float_format', lambda x: '%.5f' % x)


# In[44]:


df


# In[45]:


#grouping crypto by their name and comparing their percent changes in different intervals
df3 = df.groupby('name', sort=False)[['quote.USD.percent_change_1h', 'quote.USD.percent_change_24h', 'quote.USD.percent_change_7d', 'quote.USD.percent_change_30d', 'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d']].mean()
df3


# In[46]:


#a better visualization of the data above
df4 = df3.stack()
df4


# In[47]:


type(df4)


# In[48]:


df5 = df4.to_frame(name='values')
df5


# In[20]:


df5.count()


# In[49]:


#Creating an index for the the dataframe
index = pd.Index(range(90))

df6 = df5.reset_index()
df6


# In[50]:


df7 = df6.rename(columns={'level_1': 'percent_change'})
df7


# In[52]:


df7['percent_change'] = df7['percent_change'].replace(['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d'],['1h','24h','7d','30d','60d','90d'])
df7


# In[53]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[54]:


sns.catplot(x='percent_change', y='values', hue='name', data=df7, kind='point')


# In[59]:


df10 = df[['name','quote.USD.price','timestamp']]
df10 = df10.query("name == 'Bitcoin'")
df10


# In[62]:


sns.set_theme(style="darkgrid")

sns.lineplot(x='timestamp',y='quote.USD.price',data=df10)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




