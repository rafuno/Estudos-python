nome = 'Rafa'
idade = 22
altura = 1.82
maioridade = idade > 18
peso = 63
imc = 63 / (altura**2)


print('Nome:', type(nome))
print('Idade:', idade)
print('Altura:', altura)
print('Maior de idade:', maioridade)
print(f'{nome} tem {idade} anos de idade e seu imc é, {imc:.3f}')
