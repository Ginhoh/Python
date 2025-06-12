from lib.funções import *
from time import sleep
#criar um sistema que calcule quantas caixas de piso daria certo para tal metragem de piso,
#falando quantas caixas e quantas peças para completar.
while True:
    titulo('Sistema Para Despacho')
    sleep(1)
    a = float(input('Quantos Metros vem numa caixa?: '.replace('.',',')))
    b = float(input('Quantas pedras vem em uma caixa?: '))
    c = float(input('Quantos metros você quer? : '.replace('.',',')))
    #metros dividido pela caixa

    caixas = c/a
    pedras = a/b
    n1 = int(pedras * 100)
    #n1 coloca pra inteiro e multiplica por 100, pra não ter virgula
    n2 = float(n1 / 100)
    #n2 volta pra float, mas exatamente com as casas decimais usadas pela loja
    necessário = int(caixas)*b    #POSSIVEL BUG: NECESSÁRIO
    mtporcx = int(caixas)*n2*b
    restante = pdfcx =0
    while True:
        if mtporcx < c:
            mtporcx +=n2
            restante += 1
            pdfcx += 1
        if mtporcx >= c:
            break
    while True:
        if restante > b:
            caixas += 1
            restante -= b
        else:
            break
    sleep(1)
    print(f'Caixas necessárias: {int(caixas)}')
    sleep(1)
    print(f'Metro da pedra: {n2}')
    sleep(1)
    print(f'Total de pedras: {int(necessário)+pdfcx}')
    sleep(1)
    print(f'Pedras foras da caixa: {int(restante)}')
    sleep(1)
    print(f'\nRESULTADO: {int(caixas)} caixas e {int(restante)} pedras')
    sleep(2)

    r = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if r != 'N' or r != 'S':
        print()
    if r == 'N':
        titulo('SAINDO DO SISTEMA', 50)
        break