"""
Escreve o número 1 num arquivo chamado `um.txt`.
Cria o arquivo, caso não exista. Sobrescreve, caso exista.
"""

arquivo = open('um.txt', 'w')
arquivo.write('1')
