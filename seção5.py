Exercísios da Seção 5

# 1

n1 = int(input(f'Digite um número: '))
n2 = int(input(f'Digite outro número: '))
if n1 > n2:
    print(f'{n1} é maior que {n2}.')
else:
    print(f'{n2} é maior que {n1}. ')

# 2

x = int(input(f'Digite um número: '))
if x > 0:
    print(x ** (1/2))
else:
    print('Número inválido.')

# 3

x = int(input(f'Digite um número: '))
if x > 0:
    print(x ** (1/2))
else:
    print(x ** 2)

# 4

x = int(input(f'Digite um número: '))
if x > 0:
    print(x ** 2), print(x ** (1/2))

# 5

x = int(input(f'Digite um número: '))
if x % 2 == 0:
    print('É um número par.')
else:
    print('É um número ímpar.')

# 6

n1 = int(input(f'Digite um número: '))
n2 = int(input(f'Digite outro número: '))
if n1 > n2:
    print(f'{n1} é o maior número.')
else:
    print(f'{n2} é o maior número. ')
print(n1 - n2)

# 7

n1 = int(input(f'Digite um número: '))
n2 = int(input(f'Digite outro número: '))
if n1 > n2:
    print(f'{n1} é o maior número.')
elif n1 == n2:
    print('OS números são iguais.')
else:
    print(f'{n2} é o maior número. ')

# 8

nota1 = float(input(f'Digite a nota 1: '))
nota2 = float(input(f'Digite a nota 2: '))
if 0.0 < (nota1) < 10.0 and 0.0 < (nota2) < 10.0:
    print((nota1 + nota2) / 2)
else:
    print('Nota inválida.')

# 9

salario = float(input(f'Digite o salário: '))
prestacao = float(input(f'Digite o valor da prestação: '))
if prestacao > (salario * 20 / 100):
    print('Empréstimo não concedido.')
else:
    print('Empréstimo concedido.')

# 10

altura = float(input(f'Digite sua altura: '))
sexo = input(f'Digite o sexo (masculino ou feminino): ')
if sexo == 'masculino':
    print(f'Peso ideal é: {float((72.7 * altura) - 58)}kg')
else:
    print(f'Peso ideal é: {float((62.1 * altura) - 44.7)}kg')

# 11
soma = 0
num = input(f'Digite um número: ')
if int(num) > 0:
    print(sum(int(i) for i in num))
else:
    print('Número inválido.')

# 12
num1 = int(input(f'Digite um número inteiro: '))
if num1 < 0:
    print('Número inválido.')
else:
    import math
    math.log10(num1)
    print(num1)

# 13
p1 = float(input(f'Digite a nota da p1: '))
p2 = float(input(f'Digite a nota da p2: '))
p3 = float(input(f'Digite a nota da p3: '))
media = (p1 * 1 + p2 * 1 + p3 * 2) / 4
if media >= 60:
    print(f'Você está aprovado. Sua média foi {media}.')
else:
    print(f'Você está reprovado. Sua média foi {media}.')

# 14

# import numpy
p1 = float(input(f'Digite a nota do Trabalho de Laboratório: '))
p2 = float(input(f'Digite a nota da Avaliação Semestral: '))
p3 = float(input(f'Digite a nota do Exame Final: '))
media = (p1 * 2 + p2 * 3 + p3 * 5) / 2 + 3 + 5
# if media in numpy.arange(0, 3, 0.1):
print(media)
if media in range(0, 3):
    print('Reprovado.')
elif media in range(3, 5):
    print('Em recuperação.')
else:
    print('Aprovado.')

# 15
num = int(input(f'Digite um número de 1 a 7: '))
if num == 1:
    print('Domingo')
elif num == 2:
    print('Segunda-feira')
elif num == 3:
    print('Terça-feira')
elif num == 4:
    print('Quarta-feira')
elif num == 5:
    print('Quinta-feira')
elif num == 6:
    print('Sexta-feira')
elif num == 7:
    print('Sábado')
else:
    print('Número inválido.')

# 16
num = int(input(f'Digite um número de 1 a 12: '))
if num == 1:
    print('Janeiro')
elif num == 2:
    print('Fevereiro')
elif num == 3:
    print('Março')
elif num == 4:
    print('Abril')
elif num == 5:
    print('Maio')
elif num == 6:
    print('Junho')
elif num == 7:
    print('Julho')
elif num == 8:
    print('Agosto')
elif num == 9:
    print('Setembro')
elif num == 10:
    print('Outubro')
elif num == 11:
    print('Novembro')
elif num == 12:
    print('Dezembro')
else:
    print('Número inválido.')

# 17
base_maior = int(input(f'Digite o valor da base maior: '))
base_menor = int(input(f'Digite o valor da base menor: '))
altura = int(input(f'Digite a altura: '))
a = (base_maior + base_menor) * altura / 2
if base_maior and base_menor > 0:
    print(f'Área do trapézio é: {a}')
else:
    print('Base maior e/ou base menor menores que zero.')

# 18
operacao = input(f'Digite o tipo de operação matemática - SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO OU DIVISÃO: ')
a = int(input(f'Digite o valor 1: '))
b = int(input(f'Digite o valor 2: '))
if operacao == 'soma':
    print(f'Resultado de {a} + {b} = {a + b}')
elif operacao == 'subtração':
    print(f'Resutado de {a} - {b} = {a - b}')
elif operacao == 'multiplicação':
    print(f'Resultado de {a} * {b} = {a * b}')
elif operacao == 'divisão':
    print(f'Resultado de {a} / {b} = {a / b}')
else:
    print('Operação inválida.')

# 19
num = int(input(f'Digite um número inteiro: '))
if num % 3 == 0 and num % 5 == 0:
    print(f'{num} é divisível por ambos.')
elif num % 3 == 0 or num % 5 == 0:
    print(f'{num} é divisível por 3 ou 5.')
else:
    print(f'{num} não é divisível por 3 ou 5.')

# 20
a = int(input(f'Digite o valor do lado A: '))
b = int(input(f'Digite o valor do lado B: '))
c = int(input(f'Digite o valor do lado C: '))
if a == b and b == c:
    print('O triângulo é EQUILÁTERO.')
elif a == b or a == c:
    print('O triângulo é ISÓSCELES.')
else:
    print('O triângulo é ESCALENO.')

# 21
menu = input(f'Escolha uma opção: \n'
             f'1- Soma de 2 números: \n'
             f'2- Diferença entre 2 números: (Maior pelo menor)\n'
             f'3- Produto entre 2 números: \n'
             f'4- Divisão entre 2 números: (denominador não pode ser 0)\n'
             f'Opção  ')
if menu == '1':
    a = int(input(f'Digite o primeiro número: '))
    b = int(input(f'Digite o segundo número: '))
    print(f'A soma dos números é: {a + b}')
elif menu == '2':
    a = int(input(f'Digite o primeiro número: '))
    b = int(input(f'Digite o segundo número: '))
    if a < b:
        print('Digite o maior número primeiro!')
    else:
        print(f'A diferença entre os némeros é: {a - b}')
elif menu == '3':
    a = int(input(f'Digite o primeiro número: '))
    b = int(input(f'Digite o segundo número: '))
    print(f'O produto entre os números é: {a * b}')
elif menu == '4':
    a = int(input(f'Digite o primeiro número: '))
    b = int(input(f'Digite o segundo número: '))
    if b == 0:
        print('Denominador não pode ser 0!')
    else:
        print(f'A divisão entre os números é: {a / b}')
else:
    print('Opção inválida.')

# 22
idade = int(input(f'Digite a idade: '))
tempo_de_servico = int(input(f'Digite o tempo de serviço: '))
if idade >= 65 or tempo_de_servico >= 30:
    print('Apto a se aposentar.')
elif idade >= 60 and tempo_de_servico >= 25:
    print('Apto a se aposentar.')
else:
    print('Não está apto a se aposentar.')

# 23
ano = int(input(f'Digite o ano: '))
if ano % 400 == 0:
    print('Ano bissexto.')
elif ano % 4 == 0 and ano % 100 != 0:
    print('Ano bissexto.')
else:
    print('O ano não é bissexto.')

# 24
valor = float(input(f'Digite o valor da mercadoria: '))
estado = input(f'Digite o estado de destino do produto: ')
if estado == 'MG':
    print(f'Valor da mercadoria será: R$ {valor * 0.07 + valor}')
elif estado == 'SP':
    print(f'Valor da mercadoria será: R$ {valor * 0.12 + valor}')
elif estado == 'RJ':
    print(f'Valor da mercadoria será: R$ {valor * 0.15 + valor}')
elif estado == 'MS':
    print(f'Valor da mercadoria será: R$ {valor * 0.09 + valor}')
else:
    print('Estado inválido.')

# 25
print('Cálculo de Equação do 2º grau: ax² + bx + c = 0')
a = int(input(f'Digite o valor de ax²: '))
b = int(input(f'Digite o valor de bx: '))
c = int(input(f'Digite o valor de c: '))
delta = (b ** 2) - 4 * a * c
raiz1 = (- b + (delta ** (1/2))) / 2 * a
raiz2 = (- b - (delta ** (1/2))) / 2 * a
if a == 0:
    print('Não é equação de 2º grau.')
elif delta < 0:
    print('Não existe raiz.')
elif delta == 0:
    print(f'Delta = {raiz1}, raiz única.')
elif delta >= 0:
    print(f'Raiz 1 = {raiz1} e Raiz 2 = {raiz2}')

# 26
km = int(input(f'Digite o km percorrido: '))
litros = int(input(f'Digite a quantidade de gasolina consumida em litros: '))
consumo = km / litros
if consumo < 8:
    print('Venda o carro!')
elif consumo > 8 or consumo < 14:
    print('Econômico!')
elif consumo > 12:
    print('Super econômico!')

# 27
idade = int(input(f'Digite a idade do nadador: '))
if idade in range(5, 8):
    print('Categora Infantil A')
elif idade in range(8, 11):
    print('Categoria Infantil B')
elif idade in range(11, 14):
    print('Categoria Juvenil A')
elif idade in range(14, 18):
    print('Categoria Juvenil B')
elif idade > 17:
    print('Categoria Sênior')
else:
    print('Idade não se aplica a nenhuma categoria.')

# 28
x = int(input(f'Digite o primeiro número inteiro: '))
y = int(input(f'Digite o segundo número inteiro: '))
z = int(input(f'Digite o terceiro número inteiro: '))
print(f'Média Geométrica: {(x * y * z) / (1/3)}')
print(f'Média Ponderada: {(x + 2 * y + 3 * z) / 6}')
print(f'Média Harmônica: {1 / ((1 / x) + (1 / y) + (1 / z))}')
print(f'Média aritmética: {(x + y + y) / 3}')

# 29
import random
print('Qual soma de a + b? Serão gerados números aleatórios para a e b. \n Tente adivinhar a soma deles!')
chute1 = int(input(f'Tente adivinhar a soma 1: '))
sorteio1 = random.randint(1, 100)
print(sorteio1)
if chute1 == sorteio1:
    print('Acertou.')
else:
    print('Errou.')
chute2 = int(input(f'Tente adivinhar a soma 2: '))
sorteio2 = random.randint(1, 100)
print(sorteio2)
if chute2 == sorteio2:
    print('Acertou.')
else:
    print('Errou.')
chute3 = int(input(f'Tente adivinhar a soma 3: '))
sorteio3 = random.randint(1, 100)
print(sorteio3)
if chute3 == sorteio3:
    print('Acertou.')
else:
    print('Errou.')
chute4 = int(input(f'Tente adivinhar a soma 4: '))
sorteio4 = random.randint(1, 100)
print(sorteio4)
if chute1 == sorteio4:
    print('Acertou.')
else:
    print('Errou.')
chute5 = int(input(f'Tente adivinhar a soma 5: '))
sorteio5 = random.randint(1, 100)
print(sorteio5)
if chute1 == sorteio5:
    print('Acertou.')
else:
    print('Errou.')

# 30
a = int(input(f'Digite o primeiro número: '))
b = int(input(f'Digite o segundo número: '))
c = int(input(f'Digite o terceiro número: '))
lista = [a, b, c]
print(f'{sorted(lista)}')

# 31

# 32
codigo = int(input(f'Digite o código do produto: '))
qtd = int(input(f'Digite a quantidade: '))
if codigo == 100:
    print(f'Escolheu {qtd} Cachorro Quente. Total: R$ {qtd * 1.20}')
elif codigo == 101:
    print(f'Escolheu {qtd} Bauru Simples. Total: R$ {qtd * 1.30}')
elif codigo == 102:
    print(f'Escolheu {qtd} Bauru com Ovo. Total: R$ {qtd * 1.50}')
elif codigo == 103:
    print(f'Escolheu {qtd} Hamburguer. Total: R$ {qtd * 1.20}')
elif codigo == 104:
    print(f'Escolheu {qtd} Cheeseburguer. Total: R$ {qtd * 1.70}')
elif codigo == 105:
    print(f'Escolheu {qtd} Suco. Total: R$ {qtd * 2.20}')
elif codigo == 106:
    print(f'Escolheu {qtd} Refrigerante. Total: R$ {qtd * 1.00}')
else:
    print('Código inválido!')

# 33
preco_antigo = int(input(f'Digite o preço antigo: R$ '))
if preco_antigo <= 50:
    preco_novo = preco_antigo + (preco_antigo * 0.05)
    print(f'Preço novo será R${preco_novo}')
elif preco_antigo in range(50, 101):
    preco_novo = preco_antigo + (preco_antigo * 0.1)
    print(f'Preço novo será R${preco_novo}')
elif preco_antigo > 100:
    preco_novo = preco_antigo + (preco_antigo * 0.15)
    print(f'Preço novo será R${preco_novo}')
if preco_novo <= 80:
    print('Barato')
elif preco_novo in range(80, 121):
    print('Normal')
elif preco_novo in range(120, 201):
    print('Caro')
elif preco_novo > 200:
    print('Muito caro')

# 34
nota = float(input(f'Digite a nota: '))
faltas = int(input(f'Digite o número de faltas: '))
lista1 = [9.0, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10.0]
lista2 = [7.5, 7.6, 7.7, 7.8, 7.9, 8.0, 8.1, 8.2, 8.2, 8.3, 8.4, 8.5, 8.9]
lista3 = [5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.0, 7.1, 7.2, 7.3, 7.4]
lista4 = [4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9]
lista5 = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9]
if nota in lista1 and faltas <= 20:
    print('Conceito A.')
elif nota in lista1 and faltas > 20:
    print('Conceito B.')
elif nota in lista2 and faltas <= 20:
    print('Conceito B.')
elif nota in lista2 and faltas > 20:
    print('Conceito C.')
elif nota in lista3 and faltas <= 20:
    print('Conceito C.')
elif nota in lista3 and faltas > 20:
    print('Conceito D.')
elif nota in lista4 and faltas <= 20:
    print('Conceito D.')
elif nota in lista4 and faltas > 20:
    print('Conceito E.')
elif nota in lista5 and faltas <= 20:
    print('Conceito E.')
elif nota in lista5 and faltas > 20:
    print('Conceito E.')
