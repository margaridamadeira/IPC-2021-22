#!/usr/bin/env python
# coding: utf-8

# # Primeiros passos na programação em Python
# 
# Nas primeiras aulas práticas vamos ensaiar algumas das ferramentas que temos disponíveis.
# 

# ## Usar o posto de trabalho
# 
# 
# Entrar no computador faz-se usando o identificador oficial da Universidade do Algarve, estilo a12345, (sem a parte @ualg.pt), e dando a password atribuída. Por vezes demora mais tempo do que esperaríamos, mas é mesmo assim.
# 
# Na escolha das imagens, usamos a configuração do DEEI. 
# 
# Experimente, mesmo que tenha o seu computador pessoal consigo.

# ## Criar uma área de trabalho para Introdução à programação científica
# 
# 1. Na pasta *Documents* da sua área crie uma pasta IPC. Dentro desta, crie uma pasta geral.
# Guarde tudo o que tiver a ver com a nossa cadeira nessa pasta! 
# 
# 1. Abra o IDE Spyder (menu *Iniciar* > *Anaconda* > *Spyder*)  e crie um pequeno texto, como quiser e com o que quiser. Guarde-o na sua pasta geral.
# E, se for essa a sua opção, faça isto no seu computador pessoal também. Mantenha os dois computadores “iguais”, por assim dizer. Use a sua área do [OneDrive](https://onedrive.live.com/about/en-us/signin/) para manter a informação: no fim da aula, passe para lá os seus ficheiros, e em casa trabalhe nessa pasta; quando voltar à aula, terá lá tudo o que fez fora da aula.
# 
# 1. Se estiver a usar o computador da sala, saia da sessão. Depois volte a entrar, noutro computador. Verifique que o seu ficheiro está lá.

# ## Primeiros passos
# 
# 1. No menu *Iniciar* do computador, localize o *Anaconda Prompt*.
# 
# 1. Para iniciar uma sessão de Python, escreva
# 
#         python
#  
#     A linha de comando do python é representada por '>>>', designada *prompt*. Na linha de comando, a introdução de uma instrução completa é seguida pela sua execução.
# 
#     Usando o exemplo mais famoso da informática, escreva:
# 
#         print ("Olá mundo")
#     e pressione *Enter*. Fará com que seja apresentado:
# 
#         Olá mundo
#     
#     Para sair, escreva:
# 
#         exit()
#     
# 1. Inicie uma sessão de IPython, escrevendo
# 
#         ipython
#     
#     A *prompt* de comando do ipython é numerada e colorida. Faça também aqui o exemplo anterior. Para sair, escreva:
#         
#         exit()
# 
# 1. Uma das utilizações típicas da linha de comando do python é como calculadora. Teste agora os exemplos apresentados na [Introdução](https://tutoria.ualg.pt/2021/mod/resource/view.php?id=16235).

# ## Notebook
# 
# 1. Descarregue o ficheiro *Introdução_fresh.ipynb* que está na Tutoria para a sua área. 
# 
# 1. A partir do menu *Iniciar* abra agora o *Jupyter Notebook*. No separador do explorador que foi aberto, localize o ficheiro descarregado e abra-o.
# 
# 1. Vá pressionando as teclas *Shift*+*Enter* para executar as células. Experimente mudar o seu conteúdo. 
# 
# 1. Os números das células de código indicam a ordem de execução. Note que se uma instrução depender de uma anterior e essa anterior ainda não tiver sido executada, haverá um erro.
#     Apague a saída de todas as células. Se, nos exemplos de uso de bibliotecas, executar a instrução que refere
#         
#         cos(pi)
#     haverá um erro. 
#     Se, no futuro, se deparar com uma situação destas, mande executar todas as células anteriores e repita então a execução da célula corrente.
#     
