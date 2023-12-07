'''nome ='Alison'
altura = 1.60
peso = 70
imc = (peso / (altura * altura))
'''
#pratica aula 15 (iniciativa propria)
nome = input('Qual seu nome? ')
altura = float(input ('Qual é a sua altura? '))
peso = int(input('Qual o seu peso? '))
imc = (peso / (altura * altura))

# F-strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'

print(linha_1)
print(linha_2)
print(f'{imc:.2f}')

#print(peso / (altura ** 2)) #tentativa
#print(peso / (altura * altura)) #correção

#PEDIDO PELO EXERCICIO
# ALISON TEM 1.60 DE ALTURA,
# PESA 70 QUILOS E SEU IMC É
# 27.343749999999996  (ultilizando -> (:.2f))