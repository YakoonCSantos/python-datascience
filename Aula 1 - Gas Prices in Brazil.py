#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pandas.io.parsers import read_csv


# In[2]:


filepath ="C:\\Users\\fic\\Desktop\\data-master\\2004-2019.tsv"


# In[3]:


output_table = read_csv(filepath, sep='\t', header=0, encoding='utf-8')


# In[4]:


output_table


# In[5]:


data = output_table.copy()


# In[6]:


data = data[['ESTADO','REGIÃO','PRODUTO','ANO','MÊS','DATA FINAL','PREÇO MÉDIO REVENDA']]


# In[7]:


data.head()


# In[8]:


data = data[data.ESTADO =='SAO PAULO']


# In[9]:


data.head()


# In[10]:


data = data[data.PRODUTO !='GLP']


# In[13]:


data2 = data.groupby(['ANO', 'PRODUTO'])['PREÇO MÉDIO REVENDA'].mean().reset_index()


# In[14]:


data2.head()


# In[ ]:




