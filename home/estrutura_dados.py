lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

ehMaior = -70000
ehMenor = 70000
listaPares = []
primeiro = lista[0]
ocorrencia = 0
cont = 0
media = 0

for numero in lista:
	teste = numero

	if(teste > ehMaior):
		ehMaior = teste

print('O maior número da lista é: {}\n'.format(ehMaior))

for numero in lista:
	teste = numero

	if(teste < ehMenor):
		ehMenor = teste

print('O menor número da lista é: {}\n'.format(ehMenor))

for numero in lista:
	teste = numero

	if(teste % 2 == 0):
		listaPares.append(teste)

print('Os números pares da lista são: {}\n'.format(listaPares))


for numero in lista:
	if(numero == primeiro):
		ocorrencia+=1

print('A primeira ocorrência da lista é o número {}, este número aparece {} vezes na lista.\n'.format(primeiro, ocorrencia))

for numero in lista:
	teste += numero
	cont += 1

media = teste/cont

print('A média da lista {} é: {}\n'.format(lista, media))