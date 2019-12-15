#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd # importando a biblioteca do pandas, para ETL dos Dados   >>>https://pandas.pydata.org/pandas-docs/stable/reference/
import numpy as np # Importando a biblioteca do numpy, Trabalhar os numeros
from pandas import Series, DataFrame # Importando a biblioteca complentar do Pandas


# In[9]:


obj = pd.Series(
                range(3),
                index = ['a','b','c']
                )
obj


# In[10]:


index = obj.index
index


# In[11]:


index[1:]


# In[13]:


labels = pd.Index(np.arange(3))
labels


# In[15]:


obj2 = pd.Series(
                [1.5,-2.5,0], 
                index = labels # utilizando o index citados na Valiavel obj
                )
obj2


# In[17]:


obj2.index is labels # afirmando se os resultados estaão no Labels e no obj2


# In[18]:


#Usando o Re Index


obj3 = pd.Series(
                [4.5,7.2,-5.3,3.6],
                index = ['d','b','a','c']
                )

obj3


# In[23]:


#incremendando mais elementos no Index do objeto
obj3.reindex(
            ['a','b','c','d','e','f','g','h','i','j'] 
            ) 


# In[25]:


obj4 = pd.Series(
                ['blue','purple','yellow'],
                index = [0,2,4]
)
obj4


# In[27]:


obj4.reindex(range(6), method = 'ffill')


# In[48]:


frame = pd.DataFrame(np.arange(9).reshape((3,3)), #criando matrix 3 por 3 com o Reshape e preenchendo com os dados de 0 ate 9 com np.arange
                     index = ['a','c','d'], #index dessa tabela
                     columns = ['ohio','texas','califonia'] #colunas dessa tabela  
                    )
frame


# In[49]:


frame2 = frame.reindex(['a','b','c','d'])
frame2


# In[53]:


states = ['texas','utah','califonia','ohio']
states


# In[57]:


frame.reindex(columns =states,fill_value=0 ) # alterando colunas com o Reindex e utilizando o Fill Value para zerar os NAN / nulos


# In[60]:


obj5 = pd.Series(np.arange(4.),index = ['a','b','c','d'])
obj5 [2:4]


# In[61]:


obj5[['b','c','d']]


# In[62]:


obj5[obj5 <2]


# In[64]:


obj5['b':'c'] = 5


# In[65]:


obj5


# In[71]:


data = pd.DataFrame(np.arange(16).reshape((4,4)),
                    index = ['São Paulo','Itaquaquecetuba','Santa Bárbara do Oeste','Niteroi'],
                    columns = ['PIB','IDH','GINI','Mortalidade Infantil']
                   )
data


# In[72]:


data['GINI']


# In[73]:


data[['PIB','GINI']]


# In[74]:


data[2:]


# In[77]:


data[data > 5]


# In[79]:


data[data['GINI'] > 5 ]


# In[82]:


data < 5


# In[83]:


data[data < 5]


# In[86]:


data[data < 5] = 0
data


# In[87]:


data


# In[90]:


data.loc['São Paulo',['PIB','GINI']] #localizar dados com a função LOC, do indice São Paulo e a Coluna PIB / GINI


# In[91]:


data.iloc[2] #busca


# In[93]:


data.iloc[2 ,[3,0,1]] # busca com alteração de posição


# In[94]:


data.iloc[[1,2] ,[3,0,1]] # busca com alteração de posição


# In[98]:


data.loc[:'São Paulo','GINI']


# In[100]:


data.iloc[:,:3] [data.GINI > 3]


# In[ ]:


#df[val] Select single column or sequence of columns from the DataFrame; special case conveniences: boolean array (filter rows), slice (slice rows), or boolean DataFrame (set values based on some criterion) 
#df.loc[val] Selects single row or subset of rows from the DataFrame by label 
#df.loc[:, val] Selects single column or subset of columns by label 
#df.loc[val1, val2] Select both rows and columns by label 
#df.iloc[where] Selects single row or subset of rows from the DataFrame by integer position
#df.iloc[:, where] Selects single column or subset of columns by integer position 
#df.iloc[where_i, where_j] Select both rows and columns by integer position 
#df.at[label_i, label_j] Select a single scalar value by row and column label 
#df.iat[i, j] Select a single scalar value by row and column position (integers) reindex method Select either rows or columns by labels get_value, set_value methods Select single value by row and column labe


# In[108]:


frame4 = pd.DataFrame(np.random.randsn(4,3), 
        columns = list(bde),
        index = ['utah','ohio','texas','oregon'])
frame4


# In[119]:


frame4= pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
frame4


# In[120]:


np.abs(frame4)


# In[125]:


f = lambda x: x.max() - x.min() #o que é Lambda, uma função genêrica, para mapear e reduzir
f


# In[126]:


frame4.apply(f) #utilizando a lambda na vertical 


# In[129]:


frame4.apply(f, axis ='columns') #utilizando a lambda na Horizontal 


# In[130]:


def f (x):  #função para calcular o minimo e o maximo em conjunto
    return pd.Series([x.min(), x.max()],
                     index = ['min','max'])
frame4.apply(f)


# In[131]:


def f (x):  #função para calcular o minimo e o maximo em conjunto
    return pd.Series([x.max() - x.min(), x.max(), x.min()],
                     index = ['range','max','min'])
frame4.apply(f)


# In[141]:


frame4.describe()


# In[144]:


format = lambda x: '%.2f' % x # formatar o numero para duas casas decimais


# In[143]:


frame4.applymap(format)


# In[147]:


frame4['e'].map(format)


# In[148]:


obj6 = pd.Series(range(4),index = list('dabc'))
obj6


# In[149]:


obj6.sort_index() # ordenação pelo índice


# In[151]:


obj6.sort_values() # ordenação pelo resultado


# In[152]:


obj7 = pd.Series(np.random.randn(7))
obj7


# In[ ]:




