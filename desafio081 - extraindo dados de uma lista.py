"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

valores = []
resp = 'S'
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'No total foram: {len(valores)} números digitados\n')
valores.sort()
print(f'Os números digitados em ordem crescente foram: {valores}.')
valores.sort(reverse=True)
print(f'Os números digitados em ordem crescente foram: {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')