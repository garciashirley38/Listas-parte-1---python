""" Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente."""

valores = []
while True:
    valor = (int(input('Digite um número: ')))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso')
    else:
        print('Valor ja adicionado')
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()
    if resp in 'Nn':
        break
valores.sort()
print(f'Os valores foram:{valores}')
