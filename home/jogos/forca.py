def jogar():
	print('******************************')
	print('**Bem vindo ao jogo da Forca**')
	print('******************************')

	palavara_secreta = 'banana'

	letras_acertadas = ['_','_','_','_','_','_']
	print('\n')

	acertou = False
	enforcou = False

	erros = 0

	print(letras_acertadas)

	while(not acertou and not enforcou):
		chute = input('\nDigite uma letra: ')

		if(chute in palavara_secreta):
			posicao = 0

			for letra in palavara_secreta:
				if (chute.upper() == letra.upper()):
					letras_acertadas[posicao] = letra
					print('\n')
					
				posicao += 1	
				
		else:
			erros += 1	

		acertou = '_' not in letras_acertadas
		enforcou = erros == 6

		print(letras_acertadas)

	if(acertou):
		print('Você ganhou!!!')
	else:
		print('Você perdeu!!!')

	print('Fim do Jogo!!!')