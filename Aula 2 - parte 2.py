#!/usr/bin/env python
# coding: utf-8

# In[31]:


import sympy as sp #importa a biblioteca Sympy
get_ipython().run_line_magic('matplotlib', 'inline #configura o matplot para exibir o grafiço ao tamanho da tela de exibição')
from sympy.plotting import plot3d #
sp.init_printing() #


# In[32]:


x, y, z = sp.symbols('x y z')
display((x,y,z))


# In[44]:


from sympy.solvers.solveset import linsolve

eq1 = sp.Eq(x + y, 5)
eq2 = sp.Eq(x - y, 1)

eqs = [eq1,eq2]
linsolve(eqs, (x,y))


# In[34]:


from sympy.solvers.solveset import linsolve

eq1 = sp.Eq(2*x - 5*y, 9)
eq2 = sp.Eq(7*x + 5*y, 10)

eqs = [eq1,eq2]
linsolve(eqs, (x,y))


# In[35]:


from sympy.solvers.solveset import linsolve

eq1 = sp.Eq(3*x -2*y, -14)
eq2 = sp.Eq(2*x + 3*y, 8)

eqs = [eq1,eq2]
linsolve(eqs, (x,y))


# In[36]:


from sympy.solvers.solveset import linsolve

eq1 = sp.Eq(4*x + 5*y, 2)
eq2 = sp.Eq(8*x + 7*y, 4)

eqs = [eq1,eq2]
linsolve(eqs, (x,y))


# In[55]:


from sympy.solvers.solveset import linsolve 

expr = 2**x -10
sp.solve(expr) #resolver a expressão 


# In[56]:


sp.plot(expr) #Plotar a expressão


# In[69]:


#função bascara
expr = x**2 +2*x -4
exprc = x**2 -3*x +2
exprc = x**2 +2*x -4
sp.solve(exprc)


# In[70]:


sp.plot(exprc)


# In[ ]:


#próxima aula
#Esponenciais 
#Logaritimo
#Matrizes
#Estatistica descritiva
#Media
#moda
#mediana
#Graficos
#Bossplot
#histograma
#dencidade de Kernel

#Controle de fluxo

#


# In[ ]:


#função modular
expr = x**2 +2*x -4


# In[38]:


expr2 = sp.Eq(y, x**2)
expr2


# In[39]:


expr3 = sp.Eq(y, x**2)
expr3


# In[ ]:




