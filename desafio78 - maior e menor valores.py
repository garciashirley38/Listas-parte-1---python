"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista."""

valores = []
for cont in range(0, 5):
    valor = int(input(f'Digite um valor na posição {cont}: '))
    valores.append(valor)
print('-='*30)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi: {max(valores)} nas posições ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}....', end='')
print(f'\n O menor valor digitado foi: {min(valores)} nas posições ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}...', end='')
