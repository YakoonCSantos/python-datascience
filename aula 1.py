#!/usr/bin/env python
# coding: utf-8

# In[5]:


a = 10
b = 2
c = 50
d = 86


# In[13]:


a + b


# In[6]:


import math as mt


# In[16]:


mt.sqrt(49)


# In[ ]:


e,f,g,h(85,67,85,100)


# In[18]:


print(a)


# In[61]:


set1 = {2,4,5,6}
set2 = {4,6,7,8}
set3 = {4,6,8}


# In[62]:


print(set1.union(set2))


# In[65]:


print('Os valores unicos entre os "Set" são:')
for n in (set1.union(set2,set3)):
    print(n)


# In[66]:


set1.add(10)


# In[68]:


set1


# In[69]:


set1.pop()


# In[70]:


set1


# In[74]:


set1.remove(10)


# In[75]:


set1


# In[81]:


set1.discard(4)


# In[82]:


set1


# In[83]:


len(set1)


# In[86]:


set1.clear()


# In[87]:


set1


# In[92]:


set1 = {2,4,5,6}
set1


# In[90]:


sorted(set1)


# In[93]:


min(set1)


# In[94]:


max(set1)


# In[96]:





# In[104]:


print('O valor Máximos no "Set1" são:' + str(max(set1)))
print('O valor Minimo no "Set" são:' + str(min(set1)))
print('A diferença do Máximo e o Minimo do "Set" é: ' + str(max(set1) - min(set1)))
print('A média do "Set" é: ' + str(sum(set1)/len(set1)))


# In[105]:


set4 = {4,8,5,6,7,9,5}
set5 = {4,10,5,0,7,15,5}


# In[114]:


print('A união dos "set" são :' + str(set4.union(set5)))
print('Os valores unicos entre os "set" são :' + str(set4.intersection(set5)))
print('A diferença dos "set" são :' + str(set4.difference(set5)))


# In[ ]:




