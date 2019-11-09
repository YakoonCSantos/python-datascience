#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests ##para trabalhar com web, parecido com Chomium
import re ##regex
import json ##converte arquivos para json
from bs4 import BeautifulSoup ##raspador / Scrapers


# In[ ]:


enderecos = [
    ('https://web.archive.org/web/20170703223243/http://allrecipes.com.br/receita/4465/lasanha-de-frango-com-molho-branco.aspx?o_is=LV'),
    ('https://web.archive.org/web/20170518091145/http://allrecipes.com.br/receita/13024/lasanha-de-frango-f-cil.aspx'),
    ('https://web.archive.org/web/20170520122942/http://allrecipes.com.br/receita/13038/lasanha-de-frango-com-molho-branco-e-vermelho.aspx'),
    ('https://web.archive.org/web/20170516184714/http://allrecipes.com.br/receita/8478/lasanha-de-frango-com-queijo.aspx'),
    ('XP', 'https://play.google.com/store/apps/details?id=br.com.xp.carteira'),
    ('clear', 'https://play.google.com/store/apps/details?id=br.com.clear.droid')
]

("")
    ("")
    ("")
    ("")
    'https://web.archive.org/web/20170516182044/http://allrecipes.com.br/receita/3293/lasanha-de-frango-com-creme-de-leite.aspx',
    'https://web.archive.org/web/20170518091305/http://allrecipes.com.br/receita/4805/lasanha-de-frango-com-espinafre.aspx',
    'https://web.archive.org/web/20170516183437/http://allrecipes.com.br/receita/11695/lasanha-de-frango-com-presunto-e-queijo.aspx',
    


# In[7]:




def ferramenta_receitas(endereco, ditar = False):
    result = requests.get(endereco)
    if result.status_code == 200:
        src = result.content
        soup = BeautifulSoup(src, 'lxml')
        nome_receita = soup.find('div').find_all("span", {'itemprop':'name'})
        for a in nome_receita:
            nome_receita = a.text
        descricao = soup.find('div').find_all("p", {'itemprop':"description"})
        for a in descricao:
            descricao = a.text
        ingredients = soup.find('div').find_all('span',{'itemprop':'ingredients'})
        ingredients_list = []
        for a in ingredients:
            ingredients_list.append(a.text)
        receita = soup.find('div').find_all("ol", {'itemprop':'recipeInstructions'})
        for a in receita:
            receita = a.text
        receita_dict = {'ID': 1,
       'Titulo': nome_receita,
       'Descrição': descricao,
       'Ingredientes': ingredients_list,
       'Receita': receita}
        if ditar == True:
            print(receita_dict)
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)    # Speed percent (can go over 100)
            engine.setProperty('volume', 0.9)  # Volume 0-1
            engine.say(receita_dict['Titulo'])
            engine.say('Descrição')
            engine.say(receita_dict['Descrição'])
            engine.say('Ingredientes')
            engine.say(receita_dict['Ingredientes'])
            engine.say('Receita')
            engine.say(receita_dict['Receita'])
            engine.runAndWait()
            return(receita_dict)
        else:
            return(receita_dict)
    else: 
        print('Página não pode ser raspada')


# In[8]:


ferramenta_receitas('https://web.archive.org/web/20170703223243/http://allrecipes.com.br/receita/4465/lasanha-de-frango-com-molho-branco.aspx?o_is=LV')


# In[ ]:




