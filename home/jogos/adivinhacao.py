print('******************************')
print('*	Jogo da adivinhacao	*')
print('******************************')

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
	print('\nTentativa {} de {}' .format(rodada, total_de_tentativas))


	chute = int(input('Digite o seu numero: \n'))
	print('\nVoce digitou: ', chute)

	acertou = chute == numero_secreto
	maior = chute > numero_secreto
	menor = chute < numero_secreto

	if (acertou):
		print('\nVoce acertou!')
		break
	elif(maior):
		print('\nVoce errou! \n O seu chute foi maior que o numero secreto.\n')
	elif(menor):
		print('\nVoce errou! \n O seu chute foi menor que o numero secreto.')

	rodada = rodada + 1

print('\nFim de jogo!')