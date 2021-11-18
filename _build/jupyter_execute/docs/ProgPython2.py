#!/usr/bin/env python
# coding: utf-8

# # Programação em Python - parte 2

# ## Objetivos de aprendizagem
# 
# Nesta lição, vamos dedicar especial atenção à manipulação de strings.  Teremos assim oportunidade de conhecer outra forma de controlar ciclos de execução e usar algumas das funções do Python. Em particular:
# 
# 1. entenderemos o que é indexação e a sua aplicação a strings
# 1. saberemos como usar as funções *len* e *range* e como descobrir outras funções nativas do Python
# 1. seremos capazes de controlar a execução com ciclos *for*

# ## Strings

# Python implementa o tipo string (*str*) como uma sequência imutável de carateres Unicode e métodos de apoio à manipulação de strings.

# Para obtermos informação sobre o tipo, podemos fazer
# > help(str)

# In[1]:


# help(str)


# Exploremos alguns dos métodos deste tipo, usando 

# In[2]:


frase = 'Introdução à Programação Científica - Bioengenharia!'


# ### Indexação
# 
# Podemos indicar um elemento da string ou referir uma parte da string usando a posição; este mecanismo é designado por indexação. 
# 

# In[3]:


frase[0] # o primeiro


# In[4]:


frase[0:10] # uma parte da string


# In[5]:


frase[-1] # o último


# ### Função *len*

# Uma string tem um número definido de carateres, ainda que não saibamos quantos são.

# Se quisermos saber quantos carateres tem a string, usamos a função *len*.

# In[6]:


len(frase)


# A frase tem então 52 carateres. Como os índices começam em zero, então o 51º elemento terá que ser o ponto de exclamação.
# 
# Verifiquemos:

# In[7]:


frase[51]


# A reter: os carateres de uma string de dimensão $n$ podem ser acedidos nas posições, em Python, $[ 0, n+1 [ $.
# 
# Verifiquemos:

# In[8]:


frase[0:51] # falta o último carater


# In[9]:


frase[0:52] # Todos os elementos


# ## Ciclo *for*

# Sabemos que as ações a desempenhar dependem das circunstâncias e vimos duas formas de definir o que vai ser, ou não, feito. 
# 
#     - if
#         Se <algo se verifica> <faça-se>
#         
#     - while
#         Enquanto <algo se verifica> <faça-se>

# A instrução *if* é interessante quando temos uma ação pontual, ou seja, **se** a condição se aplica.
# 
# O ciclo *while* é especialmente interessante quando as ações são para ser feitas **enquanto** uma condição se verifica. Ou seja, quando precisamos de avaliar continuamente se devemos continuar a fazer determinada ação ou se já é suficiente.

# Mas, em algumas situações, sabemos à partida que é para fazer e quantas vezes o queremos fazer. E é então que que escolhemos usar um ciclo *for*.
# 
#     - for
#         Para <enumeração do elementos do conjunto> <faça-se>
#         Para <pessoa de um grupo> <validar acesso>

# In[10]:


for elem in frase:
    #print(elem)
    print(elem, end='')


# ### Função *range*

# A função *range* produz uma sequência de inteiros. Podemos indicar em que inteiro paramos (e esse não é incluído), onde começar e onde parar, ou ainda onde começar, onde parar e qual o passo-

# In[11]:


for elem in range(5):
    print(elem)


# In[12]:


for elem in range(10,16):
    print(elem, end=' ')


# In[13]:


for elem in range(0,21,5):
    print(elem, end=' ')


# In[14]:


for elem in range(20, -1, -5):
    print(elem, end=' ')


# Imagine agora que queriamos escrever a frase ao contrário.
# Há várias alternativas.

# #### Exemplo
# 
# Imagine que, por questões de formatação, queriamos escrever entre cada carater de uma string um ponto ('.').

# Mas se sabemos quantas vezes temos que fazer, não podemos usar um *for*?
# Podemos e devemos.
# 
# 

# In[15]:


for letra in frase:
    print(letra, end='.')


# Como ficaria então para inverter a frase?

# In[16]:


for pos in range(len(frase)-1, -1, -1):
    print(frase[pos], end='')
    


# ### Funções nativas do Python
# 
# Já vimos algumas das funções do Python. Vimos funções "gerais" e outras que são específicas de alguns tipos de dados.
# 
# #### Recordemos
# 

# In[17]:


abs(-4)


# In[18]:


type(-4)


# In[19]:


int('5')


# In[20]:


int(5.0)


# In[21]:


float('5')


# In[22]:


lido = '5.0'
print(lido.isnumeric())


# #### Conhecer novas funções
# 
# Para sabermos que funções estão disponíveis, no spyder ou mesmo num notebook, podemos usar a ajuda em linha. Experimente escrever
# 
# ```
# frase.
# ```
# 
# e percorra as sugestões.
# 
# Para saber mais, use a função *help*. Por exemplo, 
# 
# ```
# help(frase.count)
# ```
# 
# ##### Alguns exemplos

# In[23]:


help(frase.count)


# In[24]:


frase


# In[25]:


# quantas vezes aparece o carater 'o'
frase.count('o')


# In[26]:


# e onde aparece o primeiro?
frase.index('o')


# In[27]:


# E o segundo 'o'?
frase.index('o', 5)


# In[28]:


# E o terceiro?
frase.index('o', 14)


# In[29]:


# Vamos substituir os 'o's por '.'
nova_frase = frase.replace('o', '.')
print(nova_frase)


# Veja que outras funções para strings existem e experimente-as.

# ## Resumo
# 
# Nesta lição, vimos que:
# 
# A instrução *for* permite definir o número de vezes que uma instrução ou grupo de instruções se deve repetir. 
# 
# Uma string corresponde a uma sequência imutável de carateres Unicode.
# 
# A indexação permite a seleção de parte da string, referindo a sua posição.
# 
# Com *len* podemos saber o número de items de um elemento.
# 
# Com *range* produzir uma sequência de inteiros.
# 
# Um padrão comum na programação é:
# - obter o comprimento da string com *len*
# - percorrer a string com o apoio de um ciclo *for* que suporta a seleção (por indexação, usando o *range*) dos elementos pretendidos
# 
# Para percorrer uma string em Python, podemos usar *for <var> in <string>*
# 
# 
# Fazendo ```help(str)``` obtemos a ajuda sobre as strings e os seus métodos.

# 
