#!/usr/bin/env python
# coding: utf-8

# # Programação em Python - parte 3
# 
# ## Objetivos de aprendizagem 
# 
# Com esta lição saberemos:
# 
# 
# 1. utilizar listas, como as criar, usar e quais os métodos definidos para este tipo de dados
# 1. ler dados da consola, podendo ter vários valores por linha e/ou várias linhas
# 1. definir o formato da escrita de resultados
# 

# ## Tipo de dados: lista
# 
# ### Recordemos
# 
# Python é uma linguagem de programação *orientada a objetos*. Já abordámos o conceito de objetos e ainda não é agora que vamos aprofundar este tema.
# Para já, será suficiente que se considere que cada objecto é caracterizado por um identificador, um valor corrente, e um conjunto de métodos e operações que lhe são aplicáveis (e que são determinados pela *classe* do objeto). 
# 
# Ora sucede também que o Python é uma linguagem *fortemente tipada*. Isto significa que se se aplicar uma operação a um valor inadequado resulta numa mensagem de erro. 
# 
# O sistema de tipos é dinâmico e os tipos são implícitos: se por um lado, não é necessário declarar o tipo, por outro lado cada expressão tem associado um objeto de determinado tipo.
# 
# Se o valor que está associado a um objeto é sempre o mesmo, o tipo diz-se *imutável*; se existirem métodos para alterar o valor associado a um objeto então o tipo diz-se *mutável*.

# #### Tipos básicos
# 
# Em Python, cada valor pertence a um determinado tipo. Esse tipo determina quais as operações que podem ser aplicadas a esse valor. Hoje (re)veremos alguns aspetos dos tipos numéricos, de sequências e de mapeamento.
# 
# Com esta perspectiva, vejamos em maior detalhe alguns tipos básicos com que já trabalhámos.
# 
# Alguns tipos básicos com que já trabalhámos são: números inteiros ( **int** ),  números reais ( **float** ) e valores lógicos ( **bool** ). Os tipos básicos são **imutáveis**.
# 
# Usando *type()* podemos ver o tipo. Experimentemos.

# In[1]:


type(1)


# In[2]:


type(1.0)


# In[3]:


type(True)


# In[4]:


type('texto')


# Podemos também ver o tipo que resulta de operações.

# In[5]:


type(2+2)


# In[6]:


type(2+2.0)


# In[7]:


type(2 == 2.0)


# #### Strings
# 
# Também já usámos strings ( **str** ), um tipo de sequências de códigos Unicode.

# In[8]:


type('A')


# In[9]:


type('Maria')


# In[10]:


nome = 'Maria'
nome[0]


# Mas
#     `nome[0] = 'm'` 
# não funciona porque as cadeias de carateres em Python são **imutáveis**, ou seja, não podem ser alteradas depois de terem sido criadas.

# In[11]:


# Porque as strings são sequências podemos fazer
nome = 'Maria'; 
for letra in nome:
    print(letra)


# ### Listas
# 
# As [listas](https://docs.python.org/pt-br/3/tutorial/introduction.html#lists) são um tipo de dados *composto* usado para agrupar outros valores. Este tipo de dados é também designado *iterável* ou *sequencial*. Não nos preocupemos para já demasiado com estas designações, teremos mais oportunidades de detalhar. 
# 
# O que é muito interessante é que as listas são **mutáveis**, ou seja, o seu conteúdo pode ser alterado.
# 
# Uma lista pode ser escrita como uma sequência de valores separados por vírgula e contidos entre parênteses retos. Embora as listas possam conter elementos de tipos variados, normalmente os elementos são todos do mesmo tipo. 

# #### Introdução

# In[12]:


primos_até_10 = [2, 3, 5, 7]


# In[13]:


primos_até_10


# Podemos indexar a lista (ou seja, aceder a uma posição usando o índice)

# In[14]:


primos_até_10 [0]


# Se quiser saber quantos elementos tenho

# In[15]:


len(primos_até_10)


# Algumas operações alteram a lista, pelo que se não quiser alterações, devo ter o cuidado de guardar criar uma versão de trabalho.

# In[16]:


primos_até_10_invertido = primos_até_10.copy()
primos_até_10_invertido.reverse()
print(primos_até_10)
print(primos_até_10_invertido)


# Mas atenção: tenho que usar **.copy**.
# Se tivesse apenas criado uma nova variável, estava a falar da mesma lista.

# In[17]:


primos_até_10_invertido = primos_até_10 # sem o copy
primos_até_10_invertido.reverse()
print(primos_até_10)
print(primos_até_10_invertido)


# Vamos repor o exemplo e criar uma nova lista para conter, em breve, os números primos até 20.

# In[18]:


primos_até_10 = [2, 3, 5, 7]
primos_até_20 = []


# Começamos por acrescentar os primos_até_10, um a um 

# In[19]:


primos_até_20.append(primos_até_10[0])
primos_até_20.append(primos_até_10[1])
primos_até_20.append(primos_até_10[2])
primos_até_20.append(primos_até_10[3])

print(primos_até_20)


# Ou mesmo, todos de uma vez

# In[20]:


primos_até_20 = []
for elem in primos_até_10:
    primos_até_20.append(elem)
print(primos_até_20)


# **Atenção**: não podemos adicionar a lista de uma só vez.

# In[21]:


primos_até_20_temporário = []
primos_até_20_temporário.append(primos_até_10)
primos_até_20_temporário


# porque teríamos uma lista onde o primeiro elemento da lista seria uma lista! Não era isto que queríamos. 

# Acrescentemos agora alguns elementos

# In[22]:


primos_até_20.append(11)
primos_até_20.append(11) #repetimos o mesmo elemento
primos_até_20.append(13)
primos_até_20.append(17)
primos_até_20.append(19)


# In[23]:


print( primos_até_20 )


# Ups! E quantas vezes surge o elemento 11 na lista? e onde?

# In[24]:


primos_até_20.count(11)


# In[25]:


primos_até_20.index(11)


# Retiremos então o elemento da posição 4

# In[26]:


primos_até_20[4:5] = []
primos_até_20


# E podemos pedir o último elemento, o penúltimo, 

# In[27]:


primos_até_20[-1]


# In[28]:


primos_até_20[-2]


# Ou fazer algumas operações

# In[29]:


primos_até_10 + primos_até_10


# In[30]:


t_lista = primos_até_10 * 2
t_lista


# Podemos ordenar

# In[31]:


t_lista.sort() # ordenar, por omissão crescente
t_lista


# In[32]:


t_lista = primos_até_10 * 2
list.sort(t_lista, reverse=True) # ordenação decrescente
t_lista


# O que posso fazer com as listas, posso fazer com as *variáveis* do tipo lista.
# Experimente, no Spyder, fazer
# 
#         list.<Tab>
#         primos_até_10.<Tab>

# ### Uso de lista e range

# Já falámos de *range*. Na verdade, **range** é um tipo (uma classe) e representa uma sequência imutável de números inteiros e é muito útil para ciclos específicos.

# In[33]:


for i in range(10):
    print(i, end = ' ')    


# In[34]:


inic = 5
fim = 50
passo = 5
list(range(inic, fim, passo))


# In[35]:


t_range = range(inic, fim, passo)
32 in t_range


# In[36]:


t_range[3]


# In[37]:


quadrados = [x**2 for x in range(10)]
quadrados


# ### Exemplo
# 
# Neste outro exemplo, queremos saber qual é o maior elemento da lista e onde está.
# Não vamos fazer duas funções, devolvemos dois valores a partir da mesma função.
# 
# Saber qual é o maior elemento consegue-se com uma estratégia simples: é o último elemento de uma lista ordenada.
# 
# Para saber onde está o maior elemento, procuro-o na lista original.
# 
# No Spyder, criamos um exemplo e ensaiamos as instruções que precisamos. Aqui no Jupyter Notebook, juntamos umas instruções de *print* para que tudo faça sentido.
# Depois reunimos as instruções numa função e experimentamos.
# 
# Vejamos, pois.

# In[38]:


# A minha lista de teste
tt_lista = [2, 5, 7, 1, 4, -16]


# In[39]:


# Faço já os ensaios pensando que a função vai ter como parâmetro t
t = list.copy(tt_lista)

t


# In[40]:


# Vou precisar de uma cópia para não perder a ordem original
v = list.copy(t)

# Uso o método sort das listas para ordenar os elementos na lista v
v.sort()

# E tenho então
v


# In[41]:


print('A minha lista ordenada é', v)


# In[42]:


# Guardo o maior elemento, que é o primeiro a contar do fim
maior = v[-1]


# In[43]:


print(f'O maior é {maior:d}')


# In[44]:


# E vejo onde estava na lista original
onde = t.index(maior)

print('A minha lista é', t)
print('O maior elemento é o {0:d} e está na posição {1:d}'.format(maior, onde))


# In[45]:


# Juntando tudo.
# A minha lista de teste
tt_lista


# In[46]:


# A minha função que devolve dois valores
def maior_onde(t):
    """Função que devolve o maior valor de uma lista e o seu índice."""
    v = list.copy(t)
    v.sort()
    maior = v[-1]
    onde = t.index(maior)
    return maior, onde


# In[47]:


# e aplico a função à minha lista de teste
maior_onde(tt_lista)
    


# In[48]:


x, y = maior_onde(tt_lista)
print ('x =', x ,' y =', y)


# (Leitura)=
# ## Leitura da consola

# Já vimos alguns casos em que aparecem mensagens de erro. Acontece que em alguns desses casos queremos _interceptar_ o erro, ou seja, não permitir que o programa termine por causa desse erro e reagir à situação de forma mais positiva. A forma de fazer isso é usar a instrução *try-except*.
# 
# A instrução *try-except* é constituída por dois blocos: o bloco do *try* e o bloco do *except*. No bloco do *try* incluímos as instruções quer poderão dar origem a erros. No bloco do *except*, incluímos o tratamento desse erro. Mas, tipicamente, indicamos quais os erros que desejamos tratar.
# 
# E usamos estas funcionalidades para ler dados da consola, tantas vezes quantas necessárias, e terminamos o programa graciosamente, sem erros.
# 
# No programa seguinte temos um ciclo *while* que não termina por si só. A forma que usamos para terminar graciosamente este programa é chamando a função de saída (*sys.exit()*). E chamamos a função de saída se a leitura dos dados não correr bem, nomeadamente se chegarmos ao fim dos dados - EOFError - ou se o utilizador primir as teclas `<Ctrl>+<C>` - KeyboardInterrupt.

# Nota: este programa deve ser experimentado na consola.
# 
# 
#     import sys
# 
#     def soma(x, y):
#         return int(x)+int(y)
# 
# 
#     def test_soma_e_segue():
#         while True:
#             try:
#                 line = input().split()
#             except (EOFError, KeyboardInterrupt):
#                 sys.exit(0)
#             if line:
#                 x,y = line
#                 z = soma(x,y)
#                 print(z)
#             else:
#                 sys.exit(0)
# 
#     test_soma_e_segue()
#   

# ## Apresentar informação
# 
# 
# Para apresentar informação usamos **print**. Já o usámos em algumas instruções simples. Na documentação do Python pode encontrar mais exemplos sobre [formas elaboradas de escrita](https://docs.python.org/pt-br/3/tutorial/inputoutput.html#fancier-output-formatting).
# Vejamos alguns dos exemplos mais interessantes para agora.
# 

# In[49]:


from math import pi
print(pi)
print(f'O valor de pi é aproximadamente {pi:.3f}.')
print('O valor de pi é aproximadamente {0:.3f}.'.format(pi))
print('{0:1.3e}'.format(pi))


# In[50]:


for i in range(1,3):
    print('{0:f} x {1:d} ~= {2:1.3f} '.format(pi, i, i*pi))


# In[51]:


for i in range(1, 5):
    print('{0:d}{1:> 6d}'.format(i, 10**i))


# In[52]:


print ('Range(1,5) vai iterar sobre', end = ": ")
for i in range(1, 5):    
    print(i,  end = ";")


# Se quisermos todos os valores numa linha, podemos criar a string pretendida e apresentá-la de uma só vez.

# In[53]:


resultado = ''
for i in range(1, 5):
    if len(resultado) == 0:
        resultado = str(i)
    else:
        resultado = resultado + ' ' + str(i)
print(resultado)


# ## Resumo
# 
# Nesta lição vimos várias funcionalidades do Python.
# 
# O tipo `list` suporta as listas, que são sequências mutáveis. São criadas com `list()` ou `[]`. Podemos percorrer as listas usando `for ... in` ou, por indexação, referir a uma posição ou parte da lista. 
# 
# A anotação do código com os tipos, embora opcional, auxilia no desenho de programas.
# 
# A instrução `try ... except` permite incluir o tratamento de casos que poderiam dar origem à paragem abrupta da execução do programa. Usamos frequentemente esta instrução para prever a entrada de dados com um número variável de elementos por linha ou várias linhas. Colocamos no bloco do `try` as instruções que podem das origem a exceções e depois indicamos como cada exceção deve sert tratada. Exceções comuns são, por exemplo, `KeyboardInterrupt` e `EOFError`.
# 
# A definição do formato da escrita pode ser conseguida com `f-strings` ou usando o método `str.format`:
# + usando `f-strings` criamos a string a apresentar prefixada com *f* e indicamos entre parênteses a expressão e a formatação pretendida. 
# + usando `str.format` criamos a string indicando entre parênteses o conteúdo e formato e indicamos os elementos a formatar.
# 
