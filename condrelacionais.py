if 7*3 == 27:
    print("Verdadeiro")
elif 7 * 3 == 21:
    print('Essa é verdadeira')

# Operadores Relacionais ==, >, >= <, <=, !=
'''print(2 == 2)
print(10 > 8)
print(2 >= 1)
print(5 < 2)
print(5 <= 5)
print(10 != 10) #diferente'''

nome = input("Qual é o seu nome? ")
idade = int(input("Qual sua idade? "))

idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar um emprestimo')
else:
    print(f'{nome}Não pode pegar emprestimo')
