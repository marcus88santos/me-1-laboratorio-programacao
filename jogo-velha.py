import sys
import random
from termcolor import colored

board = []
positions = {}
scores = []

file = 'scores.txt'

players = ['', '']
playerMoving = ['']
symbol = ['X', 'O']

def createFile(file):
	f = open(file,'w')
	f.write('JOGADOR'.ljust(20) + 'VITORIAS')
	f.close()

def verifyData(file):
	f = open(file,'r')
	tamanho = len(f.read())

	if (tamanho < 20):
		f.close()
		raise
	else:
		f.seek(0)
		scores.append(f.readlines())
		f.close()

def createPositions():
	for x in range(1, 10):
		positions[f'p{x}'] = x

def printBoard():
	board.clear()
	for line in range(1,8):
		if line == 1:
			board.append('¡-----'*3 + '¡')
		elif line % 2 == 0:
			temp = ''
			tempPosit = {2: [1,2,3], 4: [4,5,6], 6: [7,8,9]}
			for i in tempPosit[line]:
				if positions[f'p{i}'] == symbol[0]:
					color = 'blue'
				elif positions[f'p{i}'] == symbol[1]:
					color = 'red'
				else:
					color = 'grey'
				temp = temp + (f'|  ' + colored(f'{positions[f"p{i}"]}', color) + '  ')
			temp = temp + '|'
			board.append(temp)
		elif line == 7:
			board.append('!-----'*3 + '!')
		else:
			board.append('|-----'*3 + '|')
	for line in board:
		print(line)

def checkVictory(player):
	for n in [1, 4, 7]:
		if positions[f'p{n}'] == positions[f'p{n+1}'] == positions[f'p{n+2}'] and isinstance(positions[f'p{n}'], str):
			return True
	for n in [1, 2, 3]:
		if positions[f'p{n}'] == positions[f'p{n+3}'] == positions[f'p{n+6}'] and isinstance(positions[f'p{n}'], str):
			return True
	if positions[f'p1'] == positions[f'p5'] == positions[f'p9'] and isinstance(positions[f'p1'], str):
		return True
	if positions[f'p7'] == positions[f'p5'] == positions[f'p3'] and isinstance(positions[f'p1'], str):
		return True
	if player == 1:
		playerMoving[0] = 2
	else:
		playerMoving[0] = 1
	return False

def updateBoard(move, player):
	
	positions[f'p{move}'] = symbol[player-1]

def initialMenu():
	
	while True:
		print(colored('\n-> JOGO DA VELHA <-\n', 'red'))
		print(colored('-> Escolha uma opção:'))
		print(colored('-> 1 - ', 'blue') + 'Escolher jogadores')
		print(colored('-> 2 - ', 'blue') + 'Consultar o ranking de vitórias')
		print(colored('-> 0 - ', 'blue') + 'Sair')
		opcao = int(input(colored('\n-> ', 'green')))
		if opcao == 1:
			choosePlayers()
			break
		elif opcao == 2:
			printScores()
		elif opcao == 0:
			print(colored('\n-> O app foi finalizado...\n','red'))
			exit()

def choosePlayers():
	print('\n-> Digite o nome do jogador 1:')
	players[0] = str(input(colored('-> ','green')))
	
	while True:
		print('\n-> Digite o nome do jogador 2:')
		players[1] = str(input(colored('-> ','green')))
		if players[1] != players[0]:
			break
	
	while True:
		print('\n-> Escolha uma opção:')
		print(colored('-> 1 - ','blue') + 'O jogador 1 começa')
		print(colored('-> 2 - ','blue') + 'O jogador 2 começa')
		print(colored('-> 0 - ','blue') + 'Escolha aleatória')
		opcao = int(input(colored('\n-> ', 'green')))
		print('')
		if opcao == 1:
			playerMoving[0] = 1
			break
		elif opcao == 2:
			playerMoving[0] = 2
			break
		elif opcao == 0:
			playerMoving[0] = random.randint(1,2)
			break

def printScores():
	print('')
	tempScore = {}
	for i, line in enumerate(scores[0]):
		if i > 0:
			temp = line.replace('\n', '')
			temp = temp.replace(' ', ';', 1)
			temp = temp.replace(' ', '')
			temp = temp.split(';')
			tempScore[temp[0]] = int(temp[1])
	tempScore = dict(sorted(tempScore.items(), key=lambda item: item[1], reverse=True))
	print(colored('JOGADOR'.ljust(20) + 'VITORIAS'.rjust(8), 'yellow'))
	for key in tempScore:
		print(key.ljust(20) + str(tempScore[key]).rjust(8))
	input('\n-> Pressione {Enter} para continuar...')

def playAgain():
	while True:
		print('\n-> Escolha uma opção:')
		print(colored('-> 1 - ', 'blue') + 'Jogar novamente')
		print(colored('-> 2 - ', 'blue') + 'Redefinir nome, jogador inicial ou consultar ranking')
		print(colored('-> 0 - ', 'blue') + 'Sair')
		opcao = int(input(colored('-> ', 'green')))
		print('')
		if 0 <= opcao <= 2:
			return opcao
	
def updateScores(player, scores):
	newScore = {}
	scores = scores[0]
	for i, line in enumerate(scores):
		if i > 0:
			temp = line.replace('\n', '')
			temp = temp.replace(' ', ';', 1)
			temp = temp.replace(' ', '')
			temp = temp.split(';')
			newScore[temp[0]] = int(temp[1])
	
	newScore = dict(sorted(newScore.items(), key=lambda item: item[1], reverse=True))

	vitorias = int(newScore.get(players[player-1]) or 0) + 1
	
	newScore[players[player-1]] = vitorias

	f = open('scores.txt', 'w')
	f.write('JOGADOR'.ljust(20) + 'VITORIAS')

	for key in newScore:
		f.write('\n' + str(key).ljust(20) + str(newScore[key]).rjust(8))

		if playerMoving[0] == 1:
			color = 'blue'
		else:
			color = 'red'
	print('\n-> PARABÉNS, ' + colored(f'{players[player-1]}', color) + '!!!')
	print('-> Você possui ' + colored(f'{vitorias}', 'red') + ' vitória(s)!')


try:
	verifyData(file)
except:
	createFile(file)

initialMenu()

while True:

	createPositions()

	while True:
		printBoard()
		if checkVictory(playerMoving[0]):
			break
		
		if playerMoving[0] == 1:
			color = 'blue'
		else:
			color = 'red'

		while True:
			print(f'-> É a vez de ' + colored(f'{players[playerMoving[0]-1]}', color) + '. Escolha uma posição vazia para jogar (1-9):')
			move = input(colored('-> ', 'green'))
			move = int(move)
			print('')
			if 1 <= move <= 9 and isinstance(positions[f'p{move}'], int) :
				break

		updateBoard(move, playerMoving[0])

	updateScores(playerMoving[0], scores)

	newGame = playAgain()
	if newGame == 0:
		print(colored('\n-> O app foi finalizado...\n','red'))
		exit()
	elif newGame == 2:
		initialMenu()