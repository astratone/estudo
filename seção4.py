# Exercícios da seção 4

numero1 = input(f'Digite o número 1: ')
numero2 = input(f'Digite o número 2: ')
numero3 = input(f'Digite o número 3: ')
soma = int(numero1) + int(numero2) + int(numero3)
print(f' A soma é: {int(soma)}')
print(type(soma))

# ou

numero1 = int(input(f'Digite o número 1: '))
numero2 = int(input(f'Digite o número 2: '))
numero3 = int(input(f'Digite o número 3: '))
soma = (numero1) + (numero2) + (numero3)
print(f' A soma é: {int(soma)}')
print(type(soma))


# 1

numero = 32
print(numero)
print(type(numero))

# 2
numero = 25.5
print(numero)
print(type(numero))

# 3

numero1 = int(input(f'Digite o número 1: '))
numero2 = int(input(f'Digite o número 2: '))
numero3 = int(input(f'Digite o número 3: '))
soma = (numero1) + (numero2) + (numero3)
print(f' A soma é: {int(soma)}')
print(type(soma))
"""
# 4
"""
numero = 25.3
resultado = numero ** 2
print(resultado)

# 5
numero = 32.6
resultado = numero / 5
print(resultado)

# 6

c = float(input(f'Insira a temperatura em graus Celsius: '))
f = c * (9.0 / 5.0) + 32.0
print(f'A temperatura em Fahrenheit é: {float(f)}F°')

# 7

f = float(input(f'Insira a temperatura em Fahrenheit: '))
c = 5.0 * (f - 32.0) / 9.0
print(f'A temperatura em graus Celsius é: {float(c)}')

# 8
k = float(input(f'Insira a temperatua em Kelvin: '))
c = k - 273.15
print(f'A temperatura em graus Celsius é: {float(c)}C°')

# 9

c = float(input(f'Insira a tempertura em Celsius: '))
k = c + 273.15
print(f'A temperatura em graus Kelvin é: {float(k)}K°')


# 10

v1 = float(input(f'Insira a velocidade em km/h: '))
v2 = v1 / 3.6
print(f'A velocidade em m/s é: {float(v2)}m/s')

# 11

v1 = float(input(f'Insira a velocidade em m/s: '))
v2 = v1 * 3.6
print(f'A velocidade em km/h é: {float(v2)}km/h')

# 12

m = float(input(f'Insira a distância em milhas: '))
k = 1.61 * m
print(f'A distância em quilômetros é: {float(k)}km')

# 13

k = float(input(f'Insira a distância em quilômetros: '))
m = k / 1.61
print(f'A distância em milhas é: {float(m)}milhas')

# 14

g = float(input(f'Digite o ângulo em graus: '))
pi = 3.14
r = g * pi / 180
print(f'Convertivo em Radianos: {float(r)}R')

# 15

r = float(input(f'Digite o ângulo em radianos: '))
pi = 3.14
g = r * 180 / pi
print(f'Convertido para graus: {float(g)}°')

# 16

p = float(input(f'Digite o valor em polegadas: '))
c = p * 2.54
print(f'Convertido em centímetros: {float(c)}cm')

# 17

c = float(input(f'Digite o valor em centímetros: '))
p = c / 2.54
print(f'Convertido em polegadas: {float(p)}')

# 18

m = float(input(f'Digite o valume em metros cúbicos'))
l = 1000 * m
print(f'Convertido em litros: {float(l)}l')

# 19

l = float(input(f'Digite o valume em litros'))
m = l / 1000
print(f'Convertido em metros cúbicos: {float(m)}m³')

# 20

k = float(input(f'Digite a massa em quilogramas: '))
l = k / 0.45
print(f'Massa convertida em libras: {float(l)}')

# 21

l = float(input(f'Digite a massa em libras: '))
k = l * 0.45
print(f'Massa convertida em quilogramas: {float(k)}kg')

# 22
j = float(input(f'Digite o valor em jardas: '))
m = 0.91 * j
print(f'Covertido em metros é: {m}m')

# 23

m = float(input(f'Digite o valor em metros: '))
j = m / 0.91
print(f'Covertido em jardas é: {j}')


# 24

m = float(input(f'Digite o valor em m²: '))
a = m * 0.000247
print(f'Convetido em acres: {a}')

# 25

a = float(input(f'Digite o valor em acres: '))
m = a * 4048.58
print(f'Convetido em m²: {m}')

# 26
m = float(input(f'Digite o valor em m²: '))
h = m * 0.0001
print(f'Coversão em hectares: {h}ha.')

# 27
h = float(input(f'Digite o valor em hectares: '))
m = h * 10000
print(f'Coversão em metros quadrados: {m}m².')

# 28
num1 = int(input(f'Digite o primeiro número: '))
num2 = int(input(f'Digite o segundo número: '))
num3 = int(input(f'Digite o terceiro número: '))
soma = (num1 ** 2) + (num2 ** 2) + (num3 ** 2)
print(f'A soma dos quadrados dos três números é: {soma}')

# 29
nota1 = float(input(f'Digite a nota 1: '))
nota2 = float(input(f'Digite a nota 2: '))
nota3 = float(input(f'Digite a nota 3: '))
nota4 = float(input(f'Digite a nota 4: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A média aritimética é: {media}')

# 30
real = float(input(f'Digite o valor em reais: R$ '))
dolar = real / 4.00
print(f'O valor em Dólar é: ${dolar}')

# 31
num = int(input(f'Digite um número: '))
print(f'Anterior: {num -1}', f'Posterior: {num + 1}')

# 32
num = int(input(f'Digite um número: '))
triplo = (num * 3) + 1
dobro = (num * 2) - 1
print(f'{triplo + dobro}')

# 33
l = int(input(f'Digite um lado do quadrado: '))
a = l ** 2
print(f'O valor da área do quadro é: {a}')

# 34
raio = float(input(f'Digite o valor do raio de um círculo: '))
pi = 3.141592
a = pi * (raio **2)
print(f'A área do círculo é: {a}')

# 35
a = int(input(f'Digite o valor do cateto 1: '))
b = int(input(f'Digite o valor do cateto 2: '))
h = (a ** 2 + b ** 2) ** 1/2
print(f'O valor da hipotenusa é: {h}')

# 36
altura = float(input(f'Digite a altura do cilindro: '))
raio = float(input(f'Digite o raio do cilindro: '))
pi = 3.141592
v = pi * (raio ** 2) * altura
print(f'O valor do volume do cilindro é: {v}')

# 37
produto = float(input(f'Digite o Valor do produto: R$ '))
desconto = 0.12
resultado = produto * desconto
print(f'Valor com desconto de 12%: R${resultado}')

# 38
salario = float(input(f'Digite seu salário: R$'))
aumento = salario + salario * 0.25
print(f'Seu salário com aumento de 25% é: R${aumento}')

# 39
premio = 780_000.00
ganhador1 = premio * 0.46
ganhador2 = premio * 0.32
ganhador3 = premio - (ganhador1 + ganhador2)  # ou 22% (0.22)
print(f'Ganhador 1 um receberá: R${ganhador1}')
print(f'Ganhador 2 um receberá: R${ganhador2}')
print(f'Ganhador 3 um receberá: R${ganhador3}')

# 40
diaria = 30.00
dias = int(input(f'Digite a quantidade de dias trabalhados: '))
imposto = 0.08  # imposto de renda 8%
total = dias * diaria  # valor bruto
desconto = total * imposto  # valor bruto * 8%
liquido = total - imposto  # valor líquido
print(f'Valor líquido a receber: R$ {liquido}')

# 41
hora_de_trab = float(input(f'Digite o valor da hora de trabalho: R$ '))
hora_trab = int(input(f'Digite a quantidade de horas trabalhadas: '))
valor = hora_de_trab * hora_trab
adicional = valor * 0.10
total = valor + adicional
print(f'Total a receber: R${total}')

# 42
salario_base = float(input(f'Digite o salário base: R$ '))
gratificacao = salario_base * 0.05  # Gratificação de 5%
print(f'Gratificação: {gratificacao}')
desc_imposto = salario_base - (salario_base * 0.07)  # Imposto de renda 7%
print(f'Desconto imposto: {desc_imposto}')
salario_receber = desc_imposto + gratificacao
print(f'Salário a receber: R${salario_receber}')

# 43
valor_total = float(input(f'Digite o valor total do produto: R$'))
desconto = valor_total * 0.10
print(f'Valor com 10% de desconto: R$ {valor_total - desconto}')
parcela = valor_total / 3
print(f'Parcelando em 3x sem juros, cada parcela sai por: R${parcela}')
comissao = (valor_total - desconto) * 0.05
print(f'Comissão de 5% do vendedor (à vista): R${comissao}')
comissao2 = valor_total * 0.05
print(f'Comissão de 5% do vendedor (parcelado): R${comissao2}')

# 44
degrau = int(input(f'Digite a altura do degrau: '))
destino = int(input(f'Digite a altura de destino: '))
x = destino - degrau
print(f'Faltam {x} degraus.')

# 45
nome = 'anne'
print(nome.upper())
nome2 = 'PEDRO'
print(nome2.lower())

# 46
num = int(input(f'Digite um número de três dígitos: '))
if num < 100:
    print('O número tem menos de 3 dígitos.')
elif num > 999:
    print('O número tem mais de três dígitos.')
else:
    print(f'{str(num)[::-1]}')

# 47
num = int(input(f'Digite um número de 4 dígitos: '))
if num < 1000:
    print('O número tem menos de 4 dígitos.')
elif num > 9999:
    print('O número tem mais de 4 dígitos.')
else:
    print(f'{num}')

# 48
s = int(input(f'Digite o valor em segundos: '))
h = s // 3600
resto = s % 3600
m = resto // 60
s = resto % 60
print(f'{int(h)}h:{int(m)}m:{int(s)}s')

# 49
h = int(input(f'Digite a hora incial: '))
m = int(input(f'Digite os minutos inciais: '))
s = int(input(f'Digite os segundos iniciais: '))
duracao = int(input(f'Digite a duração do experimento em segundos: '))
print(f'Experimento começou às {h}h:{m}m:{s}s e durou {duracao}s.')
h2 = duracao // 3600 + h
resto = (duracao % 3600)
m2 = resto // 60 + m
s2 = resto % 60 + s
print(f'Experimento terminou às {int(h2)}h:{int(m2)}m:{int(s2)}s')

# 50
idade = int(input(f'Digite a sua idade: '))
ano_atual = int(input(f'Digite o ano atual: '))
ano_nascimento = ano_atual - idade
print(f'Seu ano de nascimento é: {ano_nascimento}')

# 51

# 52

# 53
c = float(input(f'Digite o comprimento do terreno: '))
l = float(input(f'Digite a largura do terreno: '))
p = float(input(f'Digite o preço do metro de tela: '))
a = c * l
tela = a * p
print(f'Área do terreno: {a}m²')
print(f'Custo para cercar o terreno: R${tela}')
