#!/usr/bin/env python
# coding: utf-8

# # Programação em Python 
# 

# ## Introdução
# 
# Para criar uma solução informática temos que saber resolvê-lo e programar essa forma de resolução.
# A abordagem que adotamos para resolvermos um problema é designada algoritmo. O programa é a tradução desse algoritmo numa linguagem de programação.
# 
# O que deve ser feito nas diferentes etapas do problema pode variar conforme a situação. É pois importante que sejamos capazes de definir se algo deve ser feito, ou enquanto algo deve ser feito.

# ## Objetivos de aprendizagem
# 
# Nesta lição exploramos o desenvolvimento de soluções. Depois desta lição deveremos ser capazes de
# 
# 1. Construir expressões lógicas com tipos de dados nativos simples
# 1. Construir instruções de controlo de fluxo usando *if* e *while*
# 

# ## Operações com resultado lógico
# 
# Um dos tipos de dados nativos do Python é o tipo lógico (*bool*).
# Um valor lógico pode ser **False** ou **True** e é o resultado de uma comparação ou da avaliação de uma expressão lógica.
# 

# 
# ### Comparação
# 
# | Operador | Avalia | Exemplo |
# | -------- | ------ | --------|
# | == | igual | ```a == b``` |
# | != | diferente | ```a != b``` |
# | < | menor | ```a < b``` |
# | <= | menor ou igual | ```a <= b``` | 
# | > | maior | ```a > b``` |
# | >= | maior ou igual | ```a >= b``` |
# 

# In[1]:


# Experimente: altere os valores de a, b, e o operador usado
a = 3
b = 5
a == b


# 
# ### Operadores lógicos
# 
# | Operador | Operação | Exemplo  | 
# | -------- | -------- | ------- |
# | not()    | Negação  | ```not(a)``` |
# | and | e lógico | ```a and b``` |
# | or | ou lógico | ```a or b```|

# #### Recordar os operadores lógicos
# 
# ##### not (Negação)
# 
# | A | not A |
# | - |  ----------|
# | True|False|
# | False|True|

# ##### and (e lógico)
# 
# | A | B | A and B |
# | - | - | ----------|
# | False | False| False|
# | False|True| False |
# | True | False | False|
# | True | True | True |

# ##### or ( ou lógico)
# 
# | A | B | A or B |
# | - | - | ----------|
# | False | False | False |
# | False | True | True |
# | True | False | True|
# | True | True | True |

# In[2]:


# Experimente: faça variar os valores de a, b e o operador usado
a = True; b = not a; a and b 


# ## Interrogações e ciclo *while*
# 
# As ações a desempenhar na resolução de um problema podem depender das circunstâncias. 
# 
# Para controlarmos o que deve ou não ser feito (controlo de execução) procedemos à avaliação das circunstâncias pela interrogação de estados significativos e decidimos se é de prosseguir ou repetir.
# 
# 

# Vejamos então, duas formas de controlar o fluxo de execução.
# 
# 
#     - if
#         Se <algo se verifica> <faça-se>
#         Se <acabou o filme> <acender luzes>
#         
#     - while
#         Enquanto <algo se verifica> <faça-se>
#         Enquanto <o filme decorre> <luzes apagadas>
# 

# #### Exemplos
# 
# Queremos apresentar uma mensagem a indicar se um número é maior, igual, ou menor que zero.
# 
# Vamos esboçar a solução e melhorando progressivamente.
# 
# 
# A variável *num* representará o nosso número neste caso.

# In[3]:


num = 4


# Para começar, queremos a mensagem para indicar se o número é maior que zero 

# In[4]:


if (num > 0):
    # a identação é importante
    print('{} é maior que zero'.format(num))


# Agora que isso está, acrescentamos outro caso. E para testar esse caso, mudamos o valor de *num*

# In[5]:


num = -2


# In[6]:


if (num > 0):
    print('{} é maior que zero'.format(num))
else:
    print('{} não é maior que zero'.format(num))


# Mas não ser maior que zero, não é suficiente. 
# 
# Agora precisávamos de outro teste para saber se é zero, ou menor que zero.

# In[7]:


num = 0 


# In[8]:


if (num > 0):
    print('{} é maior que zero'.format(num))
elif (num == 0):
    print('{} é igual a zero'.format(num))
else:
    print('{} é menor que zero'.format(num))


# Vejamos outro exemplo: queremos saber se um número é par.
# 
# Ora um número par é divisível por 2, ou seja, o resto da divisão por dois é zero.

# In[9]:


num = 6


# In[10]:


if (num%2) == 0:
    # a indentação é importante
    print(num, 'é par')


# In[11]:


num = 5


# In[12]:


if (num%2) == 0:
   print(num, 'é par')
else:
   print(num, 'não é par')


# Por vezes, queremos tratar toda uma gama de elementos, mas não sabemos quantos são.
# Sabemos, isso sim, em que condições queremos fazer esse "tratamento".
# 
# Por exemplo, queremos apresentar os elementos $a$ do intervalo $ [0, 5[ $ sabendo que $a \in N$

# In[13]:


a = 0 # condição inicial
while (a < 5): # condição de 'validade'
    # a indentação é importante
    print (a)
    a += 1 # O passo, como varia entre repetições


# Se quisessemos os valores de $[0, 3]$ por ordem decrescente, podíamos fazer

# In[14]:


a = 3 # condição inicial
while (a >= 0): 
    print (a)
    a -= 1 # O passo


# Criando expressões com estes operadores e conseguindo moldar o nosso programa às circunstâncias, já conseguimos fazer muitas coisas.

# Vejamos agora o cálculo do fatorial de um número.

# Queremos calcular o fatorial de um número usando a expressão $n! = n * (n-1)!$, para  $n > 1$

# In[15]:


def fatorial_r(n):
    """Calculo do fatorial de um número.
    n! = n * (n-1)! para n > 1
    """
    
    resultado = 1 # Elemento neutro da multiplicação 
    if (n>1):
        resultado = n * fatorial_r(n-1)
    
    return resultado
    


# In[16]:


print(fatorial_r(5))


# Queremos agora calcular o fatorial de um número usando a expressão $n! = n * (n-1) * ... * 2$, para  $n > 0$

# In[17]:


def fatorial_i(n):
    """Calculo do fatorial de um número.
    n! = n * (n-1) * ... * 2
    """
    
    resultado = 1 # Elemento neutro da multiplicação 
    while (n>1):
        resultado *= n 
        n -= 1        
    
    return resultado


# In[18]:


print(fatorial_i(5))


# ## Resumo
# 
# Para criarmos uma solução há que decidir o que fazer ou não fazer e quando. 
# 
# Aprendemos como podemos construir expressões que têm um resultado do tipo lógico (*bool*) usando comparações ou operações lógicas. Usamos essas expressões para representar condições ou estados.
# 
# Aprendemos a regular o que deve ser feito ou não e quando, usando interrogações (```if```) e ciclos condicionais (```while```). Já somos capazes de resolver problemas que requerem a avaliação de estados como condição para executar determinadas operações.
