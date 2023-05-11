#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


# In[72]:


# connect to website
   
URL = 'https://www.amazon.com/MSI-GeForce-RTX-3060-12G/dp/B08WPRMVWB/ref=nav_signin?pd_rd_w=JrL4L&content-id=amzn1.sym.c5b8618b-0079-4b03-b9e8-5d2de782ccb8&pf_rd_p=c5b8618b-0079-4b03-b9e8-5d2de782ccb8&pf_rd_r=SHMZCT9R706WK29B9AKJ&pd_rd_wg=NMCLb&pd_rd_r=f7ee7cb6-4ca2-4a1a-a353-06e090c949aa&pd_rd_i=B08WPRMVWB&psc=1&claim_type=EmailAddress&new_account=1&language=en_US'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0"}

page = requests.get(URL, headers=headers)

#gets the bare html contents of the webpage
soup1 = BeautifulSoup(page.content, "html.parser")

#prettify makes things look better
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

#getting the name of the product
title = soup2.find(id='productTitle').get_text()

#getting the span where price of the product is located
span = soup2.find('span', {"class" : "a-offscreen"})

print(title)

#cleaning the price of the product
prodprice = div.string

print(prodprice)








# In[73]:


#removing the whitespace of the product
price = prodprice.strip()[1:]
title = title.strip()

print(title)
print(price)


# In[78]:


import datetime

today = datetime.date.today()

print(today)


# In[79]:


#create the csv with the data from web scraping
import csv

header = ['Title:', 'Price', 'Date']
data = [title, price, today]


with open('AmazonwebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

    


# In[82]:


#double checking the csv with pandas
import pandas as pd

df = pd.read_csv(r'C:\Users\Fritz\AmazonwebScraperDataset.csv')

print(df)


# In[81]:


#appending data to the csv

with open('AmazonwebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[88]:


def check_price():
    URL = 'https://www.amazon.com/MSI-GeForce-RTX-3060-12G/dp/B08WPRMVWB/ref=nav_signin?pd_rd_w=JrL4L&content-id=amzn1.sym.c5b8618b-0079-4b03-b9e8-5d2de782ccb8&pf_rd_p=c5b8618b-0079-4b03-b9e8-5d2de782ccb8&pf_rd_r=SHMZCT9R706WK29B9AKJ&pd_rd_wg=NMCLb&pd_rd_r=f7ee7cb6-4ca2-4a1a-a353-06e090c949aa&pd_rd_i=B08WPRMVWB&psc=1&claim_type=EmailAddress&new_account=1&language=en_US'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0"}

    page = requests.get(URL, headers=headers)

    #gets the bare html contents of the webpage
    soup1 = BeautifulSoup(page.content, "html.parser")

    #prettify makes things look better
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #getting the name of the product
    title = soup2.find(id='productTitle').get_text()

    #getting the span where price of the product is located
    span = soup2.find('span', {"class" : "a-offscreen"})

    #cleaning the price of the product
    prodprice = div.string
    
    price = prodprice.strip()[1:]
    title = title.strip()
    
    import datetime

    today = datetime.date.today()
    
    import csv

    header = ['Title:', 'Price', 'Date']
    data = [title, price, today]
    
    with open('AmazonwebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


# In[89]:


#checks the product daily (every 24hrs)
while(True):
    check_price()
    time.sleep(86400)


# In[90]:


import pandas as pd

df = pd.read_csv(r'C:\Users\Fritz\AmazonwebScraperDataset.csv')

print(df)


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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




