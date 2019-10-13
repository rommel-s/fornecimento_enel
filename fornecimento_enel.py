
#primeiro input: Consumo
kilowatts = int(input('Insira a quantidade de kWh consumida\n: '))
print('-'*40)
#tabela e verificação da instalação
print('''
	Digite:
		[ R ] Residência
		[ C ] Comércio
		[ I ] Indústria
''')
tipo = str(input('Qual o tipo de instalaçao?\n: ')).upper()

if tipo == 'R':
	if kilowatts <= 500:
		valor = kilowatts * 0.40
		print(f'O valor da conta de luz será R$ {valor:.2f}')
	elif kilowatts > 500:
		valor = kilowatts * 0.65
		print(f'O valor da conta de luz será R$ {valor:.2f}')

elif tipo == 'C':
	if kilowatts <= 1000:
		valor = kilowatts * 0.55
		print(f'O valor da conta de luz será R$ {valor:.2f}');
	elif kilowatts > 1000:
		valor = kilowatts * 0.40
		print(f'O valor da conta de luz será R$ {valor:.2f}')

elif tipo == 'I':
	if kilowatts <= 5000:
		valor = kilowatts * 0.55
		print(f'O valor da conta de luz será R$ {valor:.2f}');
	elif kilowatts > 5000:
		valor = kilowatts * 0.60
		print(f'O valor da conta de luz será R$ {valor:.2f}')