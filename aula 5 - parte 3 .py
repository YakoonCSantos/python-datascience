#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np


# In[16]:


pip install pip --upgrade


# In[18]:


pip install pandas-datareader


# In[23]:


import pandas_datareader.data as web
import datetime  


# In[24]:



fin_data = web.DataReader("GOOGL", 'yahoo', '2019-01-01', '2019-12-30') #importando os dados da web
fin_data.head()


# In[28]:


data=[]
for ticker in ['GOOG','AAPL','XOM', 'IBM', 'MSFT']:
    x = web.get_data_yahoo(ticker,'11/30/2014','11/30/2019')
    x['ticker'] = ticker
    data.append(x)

print(pd.concat(data))


# In[33]:


data_mf = pd.DataFrame(data)


# In[35]:


data_mf


# In[ ]:




