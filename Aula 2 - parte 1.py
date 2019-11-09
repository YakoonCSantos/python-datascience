#!/usr/bin/env python
# coding: utf-8

# In[3]:


cores = ['azul','amarelo','verde','vermelho','preto']


# In[4]:


cores


# In[6]:


cores[4]


# In[7]:


len(cores)


# In[16]:


cores[len(cores)-1]


# In[14]:


indice = 1
cores[len(cores)-indice]


# In[18]:


cores[-5]


# In[26]:


cores[3:]


# In[27]:


alunos = []


# In[61]:


alunos = ['Yara','Tiago','Lucas','Vicente','Odair','Eveline','Daniel','Gabriel','Bruno','Bruno','Thales','Juliana','Bianca','David','Jair','Natali','Juliano','Natalia']


# In[62]:


alunos


# In[63]:


len(alunos)
alunos[:2]


# In[75]:


cont = 0
for n in alunos:
    print(n + ": ìndice na lista é a posição " + str(cont))
    cont = cont+1


# In[60]:


len(alunos)


# In[67]:


alunos[0] = 'Iara'
alunos


# In[73]:


cores2 = ['preto', 'preto', 'preto', 'preto', 'preto', 'preto', 'preto']
cores2


# In[74]:


cores2[0] = 'Azul'
cores2[1] = 'Vermelho'
cores2[2] = 'Laranja'
cores2[3] = 'Amarelo'
cores2[4] = 'Verde'
cores2[5] = 'Índigo'
cores2[6] = 'Lilas'

cores2


# In[180]:


cores3 = []
cores3

# Inserir uma informação no final da posição da lista
cores3.append('Azul')
cores3

# Inserir mais de uma informação no final da posição da lista
cores3.extend(['Vermelho','Laranja','Amarelo'])
cores3

# Inserir uma informação em qualquer posição / index da lista
cores3.insert(0,'Verde')
cores3

# Consultar a posição / index na lista
cores3.index('Amarelo')

# contar quantas vezes consta uma informação na lista
cores3.count('Amarelo')
cores3

cores3.sort()


# In[ ]:





# In[122]:


caixa = []

caixa.append('Iara')
caixa.extend(['Yara','Tiago','Lucas','Vicente','Odair','Eveline','Daniel','Gabriel','Bruno','Bruno','Thales','Juliana','Bianca','David','Jair','Natali','Juliano','Natalia'])


caixa


# In[94]:


caixa.pop(0)
caixa


# In[92]:


caixa = []
caixa.append('Tiago')

caixa


# In[95]:


caixa


# In[101]:


caixa.append('1Tiago')
caixa


# In[102]:


caixa.pop(0)
caixa


# In[110]:


caixa.sort()
caixa


# In[112]:


caixa.count('Tiago')


# In[115]:


caixa.copy()


# In[164]:


alunos = []


# In[165]:


alunos.append('João')
alunos


# In[166]:


alunos.extend(['Yara','Tiago','Lucas','Vicente','Odair','Eveline','Gabriela','Daniel','Bruno','Bruno','Thales','Juliana','Bianca','David','Jair','Natali', 'Juliano', 'Natalia'])
alunos


# In[167]:


alunos.insert(2,'Thiago')
alunos


# In[168]:


alunos.index('Thiago')


# In[169]:


alunos.pop(2)
alunos


# In[170]:


alunos.remove('Bruno')
alunos


# In[171]:


print('aluno >>> qtd')
for n in alunos:
    print(n +" >>> "+str(alunos.count(n)))


# In[178]:


len(alunos)


# In[188]:


n_cliente = ('Tiago')
n_idata = [30]


# In[189]:


print(n_cliente + str(n_idata))


# In[196]:


nomes1 = ('Yara','Tiago','Lucas','Vicente','Odair','Eveline','Gabriela','Daniel','Bruno','Bruno','Thales','Juliana','Bianca','David','Jair','Natali', 'Juliano', 'Natalia')


# In[197]:


nomes1[5]


# In[199]:


print('>Nomes<')
for n in nomes1:
    print(n)


# In[ ]:




