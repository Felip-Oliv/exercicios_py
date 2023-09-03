import os
import random
from unidecode import unidecode
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

# Permite que o jogador selecione o número de letras da palavra
qtde = int(input("Quantas letras? "))
lista_n = gera_lista_n_letras(lista, qtde)

#Selecionando uma palavra aleatória com base na quantidade de letras selecionada
palavra = list(unidecode(random.choice(lista_n)))



#Mostra as letras disponiveis para digitar
disponiveis = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", 
               "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
acerto = []
erros = 0
concluido = False

print("--------JOGO DO TERMO---------")
# Inicio do jogo
# Enquanto a variavel concluido for falsa roda o jogo
while concluido == False:
    
    #Limpando o console para o jogo ficar mais limpo
    os.system('cls' if os.name == 'nt' else 'clear')
    # A cada letra em palavra for correta ele mostra a tela com a letra
    # Caso a letra não esteja dentro do espaço ele mostra o espaço em branco
    # Quando o concluido for Verdadeiro ele encerra o jogo
    print(palavra)
    tela = ""
    for letra in palavra:
        if letra in acerto:
            tela += f'[{letra}]'
        else:
            tela += "[ ] "
    if acerto == palavra:
        break
    # Mostra a tela atualiza a cada rodada e as letras disponiveis
    print(tela)
    print()
    print("Letras disponíveis: ")
    print(disponiveis)
    print()
    escolha = input("Escolha uma letra").lower()
    # Verifica se a escolha já foi usada
    if escolha not in disponiveis:
        print("Você já usou essa letra. Ecolha outra")
        continue
    if escolha in palavra:
        #Caso a escolha esteja na palavra ele retorna a escolha e adiciona a mesma em acertos
        print(f"Você acertou a {escolha}!")
        acerto.append(escolha)
    else:
        #Caso as escolha não esteja em palavra ele remove a letra das disponiveis e erro soma 1
        print("Ops, você errou!!")
        erros += 1
    disponiveis.remove(escolha)


#O FIM DO JOGO MOSTRANDO O ACERTO E ERROS.
print("----------FIMMMMMM-------------------")
print(f"A palavra era"+str(palavra))
print()
print(f"Toral de erros: {erros}")