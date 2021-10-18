# -*- coding: utf-8 -*-

"""
Ficheiro de exemplo para submissão ao Mooshak
(c) Margarida Madeira e Moura, 2021
"""

def converte_polegada_para_centimetro(dist_polegadas):
    """Função que converte uma distância de polegadas para centímetros."""

    centimetros_por_polegada = 2.54
    resultado = dist_polegadas * centimetros_por_polegada
    return resultado 

x = int(input())
z = converte_polegada_para_centimetro(x)
print(z)
    