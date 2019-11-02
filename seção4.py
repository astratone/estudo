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
