import os
import random
print(os.getcwd())

# início do programa

arquivo = "lista_palavras.txt" # altere o caminho se necessário
                               # o ideal é que esteja no mesmo diretório do programa
                               
def le_arquivo(arq):
    """ Lê arquivo especificado e retorna uma lista com todas as linhas """    
    with open(arq, encoding="UTF-8") as f:
        return [linha.strip() for linha in f] # método strip remove o '\n' do final da linha