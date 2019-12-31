#!/usr/bin/env python
# coding: utf-8

# In[61]:


import numpy as np # Importar o NUMPY


# In[62]:


plan = np.random.randn(1000,10)
plan


# In[63]:


plan.mean() #metodo para calcular os valores da colunas, com o sem o axis=


# In[64]:


np.mean(plan)


# In[65]:


plan.mean(axis=0)


# In[66]:


plan.mean(axis=1)


# In[67]:


plan.cumsum(axis=1) #soma acumulativa


# In[68]:


plan.cumprod()


# In[69]:


plan1 = np.random.randn(10)
plan1


# In[70]:


plan1.cumprod(axis=0)


# In[71]:


plan1.cumsum(axis=0)


# In[72]:


plan1.sum()


# In[73]:


plan1.mean()


# In[74]:


plan1.std()


# In[75]:


plan1.var()


# In[76]:


plan1.min()


# In[77]:


plan1.max()


# In[78]:


plan1.argmin()


# In[79]:


plan1.argmax()


# In[80]:


plan1.sort()
plan1


# In[81]:


ints = np.array([1,1,2,3,5,5,5,7,7,9,10,12,17])
ints


# In[82]:


np.unique(ints)


# In[83]:


len(ints)


# In[86]:


np.intersect1d(plan,plan1)


# In[249]:


np.save('C:/Users/fic/Desktop/data-master/myarray.npy',arr7)


# In[257]:


np.load('C:/Users/fic/Desktop/data-master/myarray.npy')


# In[278]:


from numpy.linalg import inv


# In[279]:


x = np.random.randn(5,5)


# In[280]:


mot = x.T.dot(x)


# In[281]:


inv(mot)


# In[282]:


mot.dot(inv(mot))


# In[5]:


pip install pandas-profiling


# In[6]:


pip install googlefinance


# In[10]:


import numpy as np
import pandas as pd
import pandas_profiling
from googlefinance import getQuotes
import json


# In[3]:


df=pd.read_json('https://api.coinmarketcap.com/v1/ticker/?limit=10000')
df.head


# In[ ]:


#capitulo 5 do livro


# In[ ]:




