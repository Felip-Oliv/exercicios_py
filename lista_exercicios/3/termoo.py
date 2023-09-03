import os
import random
# início do programa

arquivo = 'C:/_src/exercicios_py/lista_exercicios/3/lista_palavras.txt' # altere o caminho se necessário
# o ideal é que esteja no mesmo diretório do programa
                               
def le_arquivo(arq):
    """ Lê arquivo especificado e retorna uma lista com todas as linhas """    
    with open(arq, encoding="UTF-8") as f:
        return [linha.strip() for linha in f] # método strip remove o '\n' do final da linha
    
    
def gera_lista_n_letras(lista, n):
    return [x for x in lista if len(x) == n]

def imprime_palavra_atual(palavra):
    for l in palavra:
        print(l,end=" ")
    print("")

lista = le_arquivo(arquivo)
#print(lista) # descomente para verificar se a lista está correta

lista = le_arquivo(arquivo)
# print(lista) # descomente para verificar se a lista está correta


qtde = int(input("Quantas letras? "))
lista_n = gera_lista_n_letras(lista, qtde)

print(lista_n)
palavra = list(random.choice(lista_n))
print(palavra)
