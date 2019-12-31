#!/usr/bin/env python
# coding: utf-8

# In[2]:


# o que é ETL (Extração, transformação e Carregamento de dados)
#array são matrizes, com varias matrizes 

# material de apoio >>> http://www.estruturas.ufpr.br/disciplinas/pos-graduacao/introducao-a-computacao-cientifica-com-python/introducao-python/2-1-o-objeto-array-do-numpy/
import numpy as np # Importar o NUMPY


# In[5]:


data = np.array([1,2,3]) # Array de 1 linha com 3 colunas
data


# In[13]:


data1 = np.array([[1,2,3],[4,5,6],[7,8,9]]) # Array de 3 linha com 3 colunas
data1


# In[21]:


num = data1[0][2] #metodo para soma entre posições de um array!
num2 = data1[0][1]
num + num2


# In[22]:


data2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
data2


# In[23]:


data2 + data2 # metodo para soma entre matrizes utilizando a função SOMA


# In[28]:


data2 * 10 # metodo para soma entre matrizes utilizando a função Multiplicação


# In[29]:


data2 ** 2 


# In[30]:


1 / data2


# In[34]:


idade = np.array([20,58,78,98,54,22])
peso = np.array([58,60,65,87,54,100])
idade
peso


# In[35]:


data2.shape # soma a quantidade de itens na matriz


# In[37]:


data2.dtype # Informa o expaço de armazenamento


# In[40]:


data3 = np.array([[3.0,6.0,9.0],[12.0,15.0,18.0],[21.0,24.0,28.0]])
data3.dtype


# In[45]:


np.zeros((3,2)) #cria um array 3 por 2 preenchidas por zero


# In[46]:


np.ones((3,3)) #cria um array 3 por 3 preenchidas por um


# In[49]:


np.eye((3))


# In[54]:


arr1 = np.random.randn(2,3,2) #gerador de matriz
arr1


# In[60]:


v1 = np.empty((2,3,2))#gerador de matriz
v1


# In[61]:


v1.shape


# In[62]:


v2 = np.arange(15) #gerador de Array
v2


# In[75]:


v2[::7]


# In[80]:


# tipos de DTYPE, repositório:  https://docs.scipy.org/doc/numpy-1.13.0/user/basics.types.html
v3 = np.array([1,2,3],dtype = np.float32)
v3


# In[87]:


arr2 = np.random.randn(5,5) #gerador de matriz
arr2


# In[112]:


arr2[4:,:3] #ou arr2[n][n]


# In[130]:


nome = np.array(['bob','joe','will','bob','will','joe','joe'])


# In[131]:


array_mask = np.random.randn(7,7)
array_mask


# In[132]:


nome == 'bob'


# In[133]:


array_mask[nome == 'bob'] #filtrando por validação positiva


# In[159]:


array_mask[nome != 'bob'] #Filtrando por validação negativa  


# In[160]:


array_mask[~(nome == 'bob')] #Filtrando por validação negativa, podendo utilizar != ou ~


# In[161]:


mask = (nome =='bob') | (nome =='will') # filtrando por validação positiva e utilizando "OU" , "|"
array_mask[mask]


# In[205]:


arr4 = np.random.randn(6,6)
arr4


# In[ ]:





# In[193]:


arr5 = np.random.randn(10000,10000)


# In[194]:


arr5.shape


# In[195]:


arr5 = [(arr5 < 0) | (arr5 < 2)]
arr5


# In[198]:


arr6 = np.arange(15) 
arr6[10] = 12 # Alterar elementos pela posição
arr6


# In[199]:


cidades = np.array(['são paulo',' são paulo de piratininga','sorocaba','tapiraí'])
cidades.shape


# In[203]:


cidades[3] ='tupinamba'
cidades


# In[202]:


cidades.shape


# In[206]:


arr6 = np.arange(15).reshape((3,5)) #transformar vetor em matriz utilizando o RESHAPE
arr6


# In[207]:


arr6.T #transformar matriz da horizontal para vertical


# In[215]:


meses = (['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro', 'novembro', 'dezembro'])
meses


# In[208]:


arr6 = np.random.randn(6,3)
arr6


# In[209]:


np.dot(arr6.T,arr6) # valor do item bruto horizontal, vertical


# In[214]:


np.sqrt(arr6) # calcular matrix pela raiz quadrada


# In[213]:


np.exp(arr6) # calcular matrix pela exponencial


# In[238]:


x = np.random.randn(100)
x


# In[217]:


y = np.random.randn(100)
y


# In[218]:


np.maximum(x,y) #saber o máximo entre matrizes


# In[219]:


np.minimum(x,y) #saber o minimo entre matrizes


# In[220]:


arr7 = np.random.randn(10)
arr7


# In[231]:


arr7 = remainder, whole_part = np.modf(arr7)
arr7


# In[233]:


# ict1 = {1: "Jan", 2: "Fev", 12: "Dez"}


# In[236]:


#ict1 = [1,2,3]
#a = [i for i in ict1]
#b = []
#for i in ict1:
#    for x in a:
#        b.append(x + i)
#a = b

#print( a )


# In[ ]:




