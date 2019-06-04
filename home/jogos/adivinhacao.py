from random import randint

def jogar():

	print('******************************')
	print('*	Jogo da adivinhacao	*')
	print('******************************')

	print('O Número secreto vai de 0 a 100.')
	print('O jogo possui 3 níveis de dificuldade\nNível 1 (Você tem 7 tentativas)\nNível 2 (Você tem 5 tentativas)\nNível 3 (Você tem 3 tentativas)\n')

	nivel = int(input('Informe seu nível: '))
	numero_secreto = randint(0,100)
	PONTUACAO = 1000

	if(nivel == 1):
		total_de_tentativas = 7
		pontuacao_atual = 0

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

			pontuacao_atual = abs(pontuacao_atual - chute) 
			rodada = rodada + 1

		pontuacao_atual = PONTUACAO - numero_secreto - (pontuacao_atual * 5)
		print('Sua pontuação foi: {}'.format(pontuacao_atual))
		print('O número secreto é: {}'.format(numero_secreto))

	elif(nivel == 2):
		total_de_tentativas = 5
		pontuacao_atual = 0 

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

			pontuacao_atual = abs(pontuacao_atual - chute)
			rodada = rodada + 1

		pontuacao_atual = PONTUACAO - numero_secreto - (pontuacao_atual * 3)
		print('Sua pontuação foi: {}'.format(pontuacao_atual))
		print('O número secreto é: {}'.format(numero_secreto))

	elif(nivel == 3):
		total_de_tentativas = 3
		pontuacao_atual = 0 

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

			pontuacao_atual = abs(pontuacao_atual - chute)
			rodada = rodada + 1

		pontuacao_atual = PONTUACAO - numero_secreto - pontuacao_atual
		print('Sua pontuação foi: {}'.format(pontuacao_atual))
		print('O número secreto é: {}'.format(numero_secreto))

	else:
		print('Não existe esta alternativa\nTente novamente!!!')

	print('\nFim de jogo!')