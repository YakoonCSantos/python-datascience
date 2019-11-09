#!/usr/bin/env python
# coding: utf-8

# In[44]:


#fluxo de controle
x = 0
if x < 0:
    print('numero negativo')
elif x > 0:
    print('numero positivo')
else:
    print('esse numero é 0')
    


# In[ ]:


break #interrompe o código
pass #utilizar para campos vazios


# In[51]:


x = 1
if x < 0:
    print('negativo')
elif x == 0:
    pass
else:
    print('positivo')


# In[4]:





# In[ ]:


for # faça continuo
while # enquanto x for algo então faça 


# In[31]:


#exemplo de FOR e CONTINUE
sequence = [1,2,None, 4,None, 5]
total = 0
for value in sequence:
    if value == None:
        continue
    total += value
    print(total)
    


# In[32]:


#exemplo de FOR e BREAK
sequencia = [1,2,0,4,6,5,2,1]
contador = 0
for valor in sequencia:
    if valor == 5:
        break
    contador += valor
    print(contador)


# In[35]:


for i in range (4):
    for j in range(4):
        if j > i:
            break
        print((i,j))


# In[43]:


#while

x = 256
controlador = 0
while x > 0:
    if controlador > 500:
        break
    controlador += x
    x = x//2 # instrução // é o resto da divisão
    print(controlador, x)


# In[74]:


# utilizando o ZIP Junção de listas
se1= ['for','bar','boz']
se2= ['one','two','tree']

zipped = zip(se1,se2)


# In[75]:


# utilizando o ZIP Junção de listas
banda = [('nolon','ryan'), ('roger','clemmer'), ('schillin', 'curt')]

primeiro_nome, ultimo_nome = zip(*banda)

print(primeiro_nome, ultimo_nome)


# In[ ]:


##########################################################################################
##########################----##############----##########################################
###################################----###################################################
##########################----##############----##########################################
##########################################################################################


# In[ ]:


#Scrapers   ler os componentes da página html
#Crowlors   automatizar a rotina no scrapers

(//)
##beautifulsoup4
## utilitarios:  selectorgadget identificar os elementos da pagina Web (CSS, Tags) >>>  https://chrome.google.com/webstore/detail/selectorgadget/mhjhnkcfbdhnjickkkdbjoemdmbfginb?hl=pt-BR
## utilitarios:  internet wayback machine  indetificar copias de páginas que não estão mais ativos na web >>> https://archive.org/web/


# In[159]:


##Configuração de um raspador (scraper)
import requests ##para trabalhar com web, parecido com Chomium
import re ##regex
import json ##converte arquivos para json
from bs4 import BeautifulSoup ##raspador / Scrapers

# pip install bs4 instalação 


# In[162]:


pip install gtts #pip install gtts


# In[163]:


#pip install gtts
from gtts import gTTS ##para falar, no google
import os ##trabalhar com o sistema, operacional.


# In[85]:


# informar a pagina para acesso
pagina = requests.get('https://web.archive.org/web/20170703223243/http://allrecipes.com.br/receita/4465/lasanha-de-frango-com-molho-branco.aspx?o_is=LV')


# In[86]:


# Verificar se a pagina foi carregada
print(pagina.status_code) ##se tiver status code 200 a pagina está ok, se for 4O4, não encontrada, se for 403 o servidor não aceitou o raspador


# In[103]:


src = pagina.content


# In[111]:


soup = BeautifulSoup(src,'lxml')
soup


# In[143]:


nome_receita = soup.find('div').find_all('span',{'itemprop':'name'})
nome_receita = [t.text for t in nome_receita] #coletar o texto do titulo, metodo 1
#coletar o texto do titulo, metodo 2 
nome_receita


# In[136]:


descrição = soup.find('div').find_all('p',{'itemprop':'description'})
descrição = [t.text for t in descrição] #coletar o texto do titulo
descrição


# In[139]:


ingredientes = soup.find('div').find_all('span',{'itemprop':'ingredients'})
ingredientes = [t.text for t in ingredientes] #coletar o texto do ingredientes
ingredientes


# In[141]:


receita = soup.find('div').find_all('ol',{'itemprop':'recipeInstructions'})
receita = [t.text for t in receita] #coletar o texto da receita
receita


# In[146]:


#Converter dados em um dicionario
receita_dict = {
    'id': '1',
    'Titulo': nome_receita,
    'Descrição': descrição,
    'Ingredientes':ingredientes,
    'Receita':receita,    
}
receita_dict


# In[188]:


##Convertendo para JSON

#'id': '1',
#'Titulo': nome_receita,
#'Descrição': descrição,
#'Ingredientes':ingredientes,
#'Receita':receita, 

receita_json = json.dumps(receita_dict, ensure_ascii=False) #importar e configurar para acentuação brasileira com o Ensure_ASCII
print(receita_json)


# In[191]:


#https://www.programiz.com/python-programming/file-operation
#with open('C:\Users\fic\Desktop\data-master') as f:
# data = json.load(f)


# In[193]:


audiodotexto = gTTS(text=receita_dict['Receita'][0], lang='pt') #enviar o texto para criar o audio

audiodotexto.save("C:/Users/fic/Desktop/data-master/audio0.mp3")


# In[200]:


pip install playsound


# In[196]:


#pip install playsound
import playsound
playsound.playsound("C:/Users/fic/Desktop/data-master/audio0.mp3",True)
#


# In[220]:


pip install pyttsx3 pypiwin32


# In[221]:


#pip install pyttsx3
#pip install pyttsx3 pypiwin32
import pyttsx3

#one time initialization
engine = pyttsx3.init()


# In[ ]:


engine.setProperty('rate', 120) # Velocidade do audio
engine.setProperty('volume', 1) #volume de 0.0 a 1
engine.say(receita_dict)




# In[ ]:


##########################################################################################
##########################----##############----##########################################
###################################----###################################################
##########################----##############----##########################################
##########################################################################################


# In[232]:


endereco = 'https://web.archive.org/web/20170703223243/http://allrecipes.com.br/receita/4465/lasanha-de-frango-com-molho-branco.aspx?o_is=LV'


# In[233]:


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


# In[ ]:





# In[ ]:


def paginas(url):
    paginas = [
    'https://web.archive.org/web/20170703223243/http://allrecipes.com.br/receita/4465/lasanha-de-frango-com-molho-branco.aspx?o_is=LV',
    'https://web.archive.org/web/20170518091145/http://allrecipes.com.br/receita/13024/lasanha-de-frango-f-cil.aspx',
    'https://web.archive.org/web/20170520122942/http://allrecipes.com.br/receita/13038/lasanha-de-frango-com-molho-branco-e-vermelho.aspx',
    'https://web.archive.org/web/20170516184714/http://allrecipes.com.br/receita/8478/lasanha-de-frango-com-queijo.aspx',
    'https://web.archive.org/web/20170516182044/http://allrecipes.com.br/receita/3293/lasanha-de-frango-com-creme-de-leite.aspx',
    'https://web.archive.org/web/20170518091305/http://allrecipes.com.br/receita/4805/lasanha-de-frango-com-espinafre.aspx',
    'https://web.archive.org/web/20170516183437/http://allrecipes.com.br/receita/11695/lasanha-de-frango-com-presunto-e-queijo.aspx',
    ]
    


# In[ ]:



def endereço(endereco,ditar)
endereco = 'https://web.archive.org/web/20170703223243/http://allrecipes.com.br/receita/4465/lasanha-de-frango-com-molho-branco.aspx?o_is=LV'
ditar = False

