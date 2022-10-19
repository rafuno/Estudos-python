'''nome = input("Qual é o seu nome? ")
idade = input("Qual a sua idade? ")
Nascimento = 2022 - int(idade)


print(f'o usuário {nome} tem {idade} anos e nasceu em {Nascimento}.')'''


# len

'''usuario = input("digite seu usuário: ")
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print("Você precisa digitar pelo menos 6 caracteres")
else:
    print("Você foi cadastrado no sistema")


print(usuario, qtd_caracteres, type(qtd_caracteres))'''

# exercicio 1: verificar se o digito é um numero inteiro, par ou impar.
'''numero_inteiro = input("Digite um número inteiro: ")
if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)
    if numero_inteiro % 2 == 0:
        print(f"{numero_inteiro} é par")
    else:
        print(f"{numero_inteiro} é ímpar")
else:
    print("Isso não é um número inteiro")'''


'''exercicio 2: fazer um programa que pergunte a hora ao usuario 
e baseando-se nisso mandar a saudação apropriada bom dia 0-11, boa tarde 12-17 e
boa noite 17-23'''

'''horario = input("Digite um horario (0-23):  ")
if horario.isdigit:
    horario = int(horario)
    if horario < 0 or horario > 23:
        print('Horario deve ser entre 0 e 23 horas')
    else:
        if horario <= 11:
            print('Bom dia')
        elif horario <= 17:
            print('Boa tarde')
        else:
            print('Boa noite')
else:
    print("por favor digite um horario entre 0 e 23")'''

'''exercicio 3:'''

nome = input('Digite seu nome: ')
tamanho = len(nome)
if tamanho <= 4:
    print('Seu nome é curto')
elif tamanho <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
