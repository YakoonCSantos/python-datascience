#!/usr/bin/env python
# coding: utf-8

# In[138]:


import pandas as pd # importando a biblioteca do pandas, para ETL dos Dados
import numpy as np # Importando a biblioteca do numpy, Trabalhar os numeros
from pandas import Series, DataFrame # Importando a biblioteca complentar do Pandas


# In[139]:


obj = pd.Series([1,2,3,4,5,6])
obj


# In[140]:


obj.values # printar os valores dentro da variavel


# In[141]:


obj.index #printa o indexador


# In[142]:


obj2 = pd.Series([2,4,-5,3],index = ['d','b','a','c']) # declarando valores, nomenando o index 
obj2


# In[143]:


obj2[obj2 > 0] # filtrando o array


# In[144]:


obj2 * 2 # Calculando o array 


# In[145]:


'b' in obj2 # buscando valores na array com 'IN'


# In[146]:


'e' in obj2 # buscando valores na array com 'IN'


# In[147]:


sdata ={'ohio':35000,'texas':71000,'oregon':16000,'utah':5000} #declarando um dicionario '{}'
sdata


# In[148]:


obj3 = pd.Series(sdata)
obj3


# In[149]:


states = ['california','ohio','oregon','texas'] #declarando uma Lista '[]'
states


# In[150]:


obj4 = pd.Series (sdata, index = states) # Utilizando os dados do dicionario Sdata, indexando com a lista States, utah será retirado pois não foi listado na lista States
obj4


# In[151]:


pd.isnull(obj4) # utilizando o Metodo Is NUll para validar se algum dado no data frame esta vazio


# In[152]:


obj4.isnull


# In[153]:


pd.notnull(obj4) # utilizando o Metodo NOt NUll para validar se algum dado no data frame esta preenchido


# In[154]:


obj4.notnull


# In[155]:


obj4.isnull


# In[156]:


obj3+obj4 # quando calculamos NAN com NAN o resultado será NAN, se possivel remova ou trate


# In[157]:


obj4


# In[158]:


obj3


# In[159]:


obj4.name ='population'   # Nomendo o titulo dos dados, usando funcão 'Name'
obj4.index.name = 'states' # Nomendo o titulo dos Index, usando função 'index' + 'Name'


# In[160]:


obj4


# In[161]:


obj5 = pd.Series([4,7,-5,3],index = ['d','b','a','c'])
obj5


# In[162]:


obj5.index = ['bob','steve', 'jeff','ryan']
obj5.index.name = 'Nome'
obj5.name ='Nota'
obj5


# In[163]:


data ={
        'state':['ohio','ohio','ohio','nevada','nevada','nevada'],
       'year':[2000,2001,2002,2001,2002,2003],
       'pop':[1.5,1.7,3.6,2.4,2.9,3.2]
    }
data


# In[164]:


frame = pd.DataFrame(data)
frame


# In[165]:


frame.head() # imprime as 5 primeiras linhas


# In[166]:


frame.tail() #Retorne as últimas linhas
 


# In[167]:


pd.DataFrame(data,columns = ['year','state','pop']) #ordenando as Colunas do Data Frame com COLUMNS


# In[168]:


frame2 = pd.DataFrame(data,
                      columns = ['year','state','pop','debt'],
                      index = ['one','two','three','four','five','six']
                     )
frame2


# In[169]:


frame2.columns #acessar as mascaras de dados das colunas


# In[170]:


frame2 ['state'] # acessando os dados pelo nome do index


# In[171]:


frame2.year # acessando os dados pelo nome da variável


# In[172]:


frame2.loc['three'] #acessando os dados pela linha do index


# In[173]:


frame2['debt']=16.5 # alterar valores da coluna DEBT par aum valor fixo
frame2


# In[174]:


frame2['debt']=np.arange(6.) # alterar valores da coluna DEBT para um valor variavel urilizando o ARANGE do numpy
frame2


# In[175]:


val = pd.Series([-1.2,-1.5,-1.7], # declarando uma variavel para transformar uma coluna
               index= ['two', 'four','five'])
val


# In[176]:


frame2['debt'] = val #alterando a coluna DEBT utilizando a variavel VAL, que ira utilizar o indexador para preecher as linhas correspondende
frame2


# In[191]:


frame2['eastern'] = frame2.state == 'ohio' #Criando e validando a coluna eastern se o state for ohio, Usando validação logica '=='
frame2


# In[192]:


del frame2 ['eastern'] # apagar a coluna eastern, usando DEL 
frame2


# In[197]:


pop = {
        'nevada':{2001: 2.4,2002: 2.9},
        'ohio': {2000: 1.5,2001:1.7,2002:3.6}
      }
pop


# In[198]:


frame3 = pd.DataFrame(pop)
frame3


# In[200]:


frame3.T #Transpor os dados de Linhas por colunas


# In[205]:


pd.DataFrame(pop, index = [2001,2002,2003])
pop


# In[210]:


pdata = {
        'ohio':frame3['ohio'][:-1],
        'nevada':frame3['nevada'][:2]
        }
pd.DataFrame(pdata)


# In[215]:


frame3.index.name ='year' ; frame3.columns.name = 'state' # MUdar os nomes na mesma coluna utilizando ";"


# In[216]:


frame3


# In[217]:


frame3.values


# In[ ]:


#O que pode entrar no DataFrame  2d Array, Dicionarios, Numpy


# In[218]:


frame3


# In[219]:


frame3.columns


# In[220]:


'ohio' in frame3.columns


# In[221]:


2003 in frame3.columns


# In[ ]:


# lista de opções utilizadas em DataFrame
#append
#diffence  Saber o que é diferente em cada bases
#intessection Saber o que é em comum em cada bases
#union União de bases
#isin
#delete, del, Drop deletar dados
#insert
#is_monotonico
#is_unique
#unique

