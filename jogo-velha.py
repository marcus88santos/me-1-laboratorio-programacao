from termcolor import colored

board = []
positions = {}

arquivo = 'placar.txt'

def criarArquivo(arquivo):
	f = open(arquivo,'w')
	f.write('Jogador'.ljust(20) + 'Vitórias')
	f.close()

def verificarDados(arquivo):
	f = open(arquivo,'r')
	tamanho = len(f.read())
	if (tamanho < 20):
		f.close()
		raise

def createPositions():
	for x in range(1, 10):
		positions[f'p{x}'] = ' '

def printBoard():
	board.clear()
	for linha in range(1,8):
		if linha == 1:
			board.append('¡-----'*3 + '¡')
		elif linha % 2 == 0:
			temp = ''
			for i in range(1, 4):
				temp = temp + (f'|  {positions[f"p{int((linha / 2 - 1)*3 + i)}"]}  ')
				temp = temp + '|'
			board.append(temp)
		elif linha == 7:
			board.append('!-----'*3 + '!')
		else:
			board.append('|-----'*3 + '|')

def checkVictory(board):
	print(1)

def updateBoard(posicao, symbol):
	print('')

try:
	verificarDados(arquivo)

except:
	criarArquivo(arquivo)

createPositions()

print(colored('\n-> JOGO DA VELHA', 'red'))
print(colored('-> Escolha uma opção:'))
print(colored('-> 1 - ', 'blue'))

printBoard()


positions['p1'] = 'X'

positions['p9'] = 'O'

# updateBoard(posicao, symbol)

printBoard()