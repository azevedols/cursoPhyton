print('******************************')
print('**Bem vindo ao jogo da Forca**')
print('******************************')

palavara_secreta = 'banana'

letras_acertadas = ['_','_','_','_','_','_']

acertou = False
enforcou = False

erros = 0

while(not acertou and not enforcou):
	chute = input('Digite uma letra: ')

	posicao = 0

	for letra in palavara_secreta:
		if (chute.upper() == letra.upper()):
			letras_acertadas[posicao] = letra 

		posicao = posicao + 1

	print(letras_acertadas)

print('Fim do Jogo!!!')