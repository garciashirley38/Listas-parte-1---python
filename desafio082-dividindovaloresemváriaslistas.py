""" Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas."""

valores = []
par = []
impar = []
while True:
    valor = (int(input('Digite um valor: ')))
    valores.append(valor)
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while resp != 'N' and resp != 'S':
        resp = str(input('RESPOSTA INVÁLIDA!! \n'
                         'A resposta tem que ser SIM ou NÃO [S/N]. Por favor, digite novamente: ')).strip().upper()[0]
    if valor % 2 == 0 and valor not in par:
        par.append(valor)
    elif valor % 2 == 1 and valor not in impar:
        impar.append(valor)
    if resp == 'N':
        break
print(f'Os valores lidos foram: {valores}')
print(f'Os valores pares são: {par}\n'
      f'Os valores impares são {impar}')

"""while True:
    valores.append(int(input('Digite um número: ')))
    resp = str(input('Deseja cntinuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'Os valores lidos foram: {valores}')
print(f'Os valores pares são: {par}\n'
      f'Os valores impares são {impar}')"""