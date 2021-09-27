#!/usr/bin/env python
# coding: utf-8

# # Introdução
# 
# 
# Começamos com uma visão geral do enquadramento e da linguagem Python.

# 
# 
# Neste capítulo veremos:
# 
# 1.  Porque escolhemos Python
# 1.  Como funcionam os computadores
# 1.  O que é uma linguagem de programação
# 1.  Uma breve apresentação de Python

# ### Porque escolhemos Python?
# 
# Um dos pontos fortes do Python é a existência de múltiplos recursos,
# livres e gratuitos. E assim, existem muitas formas de abordar a
# programação em Python. Nós vamos optar por uma forma que facilitará o
# uso ao longo do curso em Bioengenharia, mas também facilita o uso
# futuro.
# 
# Esta escolha permite o alinhamento com a política da União Europeia de ciência aberta ([Open Science](https://ec.europa.eu/info/research-and-innovation/strategy/strategy-2020-2024/our-digital-future/open-science_pt)). 
# Essa política promove também  que os dados devem poder ser encontrados, acedidos, entendidos, movidos entre sistemas e reutilizados ([FAIR data](https://www.nature.com/articles/sdata201618)).
# 
# É com estes princípios que vamos começar a programar em Python e fazer ciência aberta. Assim, vamos usar o ambiente Jupyter, vamos usar dados publicados na Internet e, programando em Python, vamos obter as nossas próprias conclusões.

# ### Como funcionam os computadores?
# 
# Um computador é um equipamento constituído por vários componentes.
# Quando respondemos a uma pergunta do tipo *Que computador tens?*
# tipicamente indicamos o processador, a quantidade de memória *RAM* e a
# dimensão do disco rígido.
# 
# Mas há outros componentes num computador que, de tão comuns, nem nos
# lembramos de referir. Por exemplo, o teclado, o rato, o monitor.
# 
# Na figura vemos a representação de alguns dos dispositivos que compõem um computador.

# 
# <img src="figures/sketch/computer_sk_transp.png" alt="Esquema computador" title="Diagrama simplificado de um computador" style="width: 500px;"/>

# A ideia básica é que quando o computador recebe um estímulo (pelo rato ou teclado), 
# para produzir o resultado correspondente (apresentar no monitor) irá fazer processamento
# sobre esse estímulo, processamento esse que pode incluir alguns anteriores (que estão em memória ou no disco).
# 
# 
# > Sugere-se a leitura da secção [Arquitetura de hardware](https://pt.wikipedia.org/wiki/Computador#Arquitetura_de_hardware) na Wikipédia.
# 

# ### O que é uma linguagem de programação?
# 
# Uma linguagem de programação é uma forma de descrever um conjunto de
# actividades que pretendemos que sejam efetuadas para atingir um
# determinado fim.
# 
# O conjunto de atividades necessárias para atingir esse fim é designado *algoritmo*.
# 
# Um programa ou uma aplicação é a expressão de um algoritmo usando linguagem de programação.
# 
# Assim, para um caso, ou para um problema, temos que saber como resolver para depois 
# podermos fazer o programa.
# 
# As linguagens de programação podem ser classificadas de acordo com as funcionalidades que 
# oferecem ou com a abordagem (método) para a descrição da solução. 

# > A linguagem que vamos usar é [Python](https://www.python.org/). Veja também a [descrição de Python](https://pt.wikipedia.org/wiki/Python) na Wikipédia.

# Há muitas linguagens de programação. Normalmente, para termos a certeza que tudo está a funcionar 
# como desejável, faz-se um pequeno programa *Hello World*. 
# 
# > Até há uma coleção desses programas [Hello World](http://helloworldcollection.de/).

# Como somos portugueses, o nosso cumprimento em Python seria

# In[1]:


print('Olá mundo')


# ### Breve apresentação de Python
# 
# #### O IPython como interpretador de comandos
# 
# O ambiente IPython, simples e interactivo, é extremamente conveniente para a aprendizagem da programação em Python, pois permite a elaboração de pequenos programas e sua experimentação. 

# Na maioria dos tutoriais, a primeira proposta de utilização do Python é como [calculadora](https://docs.python.org/3/tutorial/introduction.html) simples. 
# 
# Isto porque o Python disponibiliza à partida, para além de algumas funcionalidades básicas, várias operações numéricas que podemos utilizar:
# 
#     + (adição)
#     - (subtração)
#     * (multiplicação)
#     / (divisão)
#     ** (exponenciação)
#     // (divisão inteira)
#     % (resto da divisão inteira)

# A utilização das operações de adição, subtração, multiplicação e divisão é muito simples.
# O único cuidado que temos que ter é lembrarmo-nos da prioridade das operações e usar parenteses se for caso disso.
# Vejamos alguns exemplos.

# In[2]:


5+4*2


# In[3]:


(5+4)*2


# A exponenciação é usada para calcular potências.

# In[4]:


2**3 


# In[5]:


5**2


# A divisão inteira e resto da divisão inteira merece alguma atenção. Na divisão normal, teriamos

# In[6]:


7/2


# Na divisão inteira, o resultado é um número inteiro e poderá haver resto

# In[7]:


7//2


# In[8]:


7%2


# Existem funções, disponíveis em Python, que iremos conhecendo aos poucos. Tente determinar o resultado antes de executar a célula.
# 
#     abs(-1)*max(1, 2, 3) + min(4, 5, 6)
# 
# Para executar a célula abaixo, remova o carater '#' que indica um comentário.
# 

# In[9]:


# abs(-1)*max(1, 2, 3) + min(4, 5, 6)


# Pode consultar a documentação, embora a forma exata possa variar consoante a ferramenta que está a usar (Spyder ou Jupyter). E frequentemente, há mais de uma maneira de obter essa documentação. Por exemplo,

# In[10]:


get_ipython().run_line_magic('pinfo', 'abs')


# In[11]:


get_ipython().run_line_magic('pinfo', 'abs')


# In[12]:


help(abs)


# #### Uso de bibliotecas
# 
# É de notar que existem numerosas e diversas bibliotecas com extensões à linguagem básica, que servem os mais diversos fins. Há bibliotecas que dão suporte a mecanismos de cálculo e visualização gráfica que poderão ser bastante úteis.
# 

# Nesta unidade curricular iremos por vezes usar alguns desses mecanismos. Iniciamos com a programação em Python e avançamos depois para a utilização das bibliotecas. 
# 
# Um exemplo é *Math*.

# In[13]:


from math import *


# In[14]:


pi


# In[15]:


cos(pi)


# > *Sugestão*: Crie uma nova célula antes de importar *math* e tente obter o valor de $ \pi $, ou o $ cos(2\pi) $. A execução da célula vai falhar. Explique porquê.

# In[16]:


log(e**5)


# In[17]:


log2(1024)-log10(1000)


# Outro exemplo do que usaremos é *Matplotlib*.  
# Para ver a descrição, edite a linha abaixo e remova o comentário, isto é, apague o caracter '#'

# In[18]:


#matplotlib?


# No futuro, para se trabalhar com vetores e matrizes, podemos usar *NumPy* ou outras alternativas. 

# A instrução precedida de % é aquilo a que na terminologia do IPython se denomina *magic*, uma extensão à linguagem Python que facilita a interacção com o sistema. Introduziremos, quando necessário, outras magias do IPython. Para vermos os gráficos nesta página, fazemos

# In[19]:


get_ipython().run_line_magic('matplotlib', 'inline')


# Neste caso e para efeitos de demonstração, precisamos de algumas *peças*. 

# In[20]:


import numpy as np
from matplotlib.pyplot import plot, pie, axis, legend


# E já temos algumas funcionalidades disponíveis, por exemplo, para gerar gráficos.

# #### Geração de gráficos
# 
# A representação gráfica é uma parte importante e, felizmente, não é complicada.
# Vejamos como faríamos para representar a função $f(x) = x² $ quando o conjunto de partida é $ \{0, 1, 2, 3, 4, 5 \} $

# In[21]:


x = np.arange(6) # 


# In[22]:


# O que está afinal no eixo do x
print (x)


# In[23]:


plot(x, x**2);


# E como faríamos para representar as funções seno e coseno no mesmo gráfico?

# In[24]:


x=np.arange(0,10,0.1); 


# In[25]:


plot(x, np.sin(x), 'r', x, np.cos(x),'b');


# Há outros tipos de gráficos para além do *plot*, e quando chegarmos lá veremos melhor. Uma *espreitadela* rápida ao que seremos capazes de fazer.

# In[26]:


# Retire o comentário da linha abaixo para ver a documentação
#pie?


# In[27]:


pie([45,30,10,10,4,1], labels=[45,30,10,19,4,1],frame=0);


# In[28]:


from matplotlib.pyplot import plot as dataplot 


# In[29]:


# Retire o comentário da linha abaixo para ver a documentação
#?dataplot


# In[30]:


dataplot([1,2,3,4,5]);


# In[31]:


dataplot([1,-2,3,-4,5],"ro-");


# In[32]:


dataplot([1,5,3,4,2,6],"g*--");


# In[33]:


dataplot([1,2,3,4,5], "go-", label="line 1", linewidth=2)
dataplot([2,9,0,4], "rs",  label="line 2")
axis([-2, 8, -2, 10])
legend();


# ## Em resumo
# 
# * O IPython é um ambiente de programação interactivo muito simples, apropriado à experimentação rápida de programas em Python, e portanto adequado à aprendizagem da programação
# * Munido das extensões adequadas o ambiente IPython pode ser utilizado como poderosa ferramenta de cálculo numérico e simbólico, e de visualização gráfica, extremamente útil em aplicações científicas, matemática e engenharia
# * A biblioteca Matplotlib fornece um ambiente de computação essencialmente equivalente ao popular sistema proprietário MATLAB, também muito usado em aplicações científicas. 
