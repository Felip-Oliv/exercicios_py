# Imprimir tabuleiro
# Recebe o tabuleiro como entrada e itera por cada linha criando a grade
def print_board(board):
    for row in board:
        print(" | ".join(row)) 
 
# Verifica vencedor
# Ela verifica se há marcações especificadas de (X) ou (O) nas linhas, colunas e diagonais do tabuleiro.
# Se alguma das verificações for positiva retorna True caso negativa False
def check_winner(board, player):
    # Verifica linhas e colunas
    for i in range(4):
        if all(board[i][j] == player for j in range(4)) or all(board[j][i] == player for j in range(4)):
            return True

    # Verifica diagonais
    if all(board[i][i] == player for i in range(4)) or all(board[i][3 - i] == player for i in range(4)):
        return True

    return False
       
# O tabuleiro está totalemente preenchido?
# Essa função percorre todo o tabuleiro e verifica se há algum espaço vazio.       
# Se todos os campos estão preenchidos e caso estiverem vazios retorna True dando empate no jogo
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)      

# Onde o jogo inicia
# Inicia com o tabuleiro vazio e define o primeiro jogador como (X)
# Exibe o tabuleiro em formato de loopin e os jogadores fazem suas jogadas alternadamente. 
# Até um ser vencedor ou o tabuleiro estar totalmente preenchido(empate)
def main():
    bordl = int(input('Qual a quantidade de linhas?'))
    bordc = int(input('Qual a quantidade de cululas?'))
        
    board = [[' ' for _ in range(bordl)] for _ in range(bordc)]
    current_player = 'X'

    print("Bem-vindo ao jogo da velha NxN!")
    print_board(board)

    while True:
        row = int(input(f"Jogador {current_player}, escolha a linha (posição inicia 0): "))
        col = int(input(f"Jogador {current_player}, escolha a coluna (posição inicia 0): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Essa posição já está ocupada. Tente novamente.")
            continue

        print_board(board)

        if check_winner(board, current_player):
            print(f"Parabéns, jogador {current_player}! Você venceu!")
            break
        elif is_board_full(board):
            print("O jogo terminou em empate!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

# Isso garante que o código dentro do bloco main 
# seja executado se este arquivo for executado como um programa
# não se for importado como um módulo em outro arquivo Python.
if __name__ == "__main__":
    main()
