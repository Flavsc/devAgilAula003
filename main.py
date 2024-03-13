import ad
import sub
import mult
import div

run = 1

while run == 1:
    x = int(input("Digite o primeiro numero:\n"))
    y = int(input("Digite o segundo numero:\n"))
    print('''
Digite:
    1 - Adição
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
    5 - Sair
          ''')
    op = int(input("Opção: "))
    if op == 1:
        print("Resultado:")
        print(ad.soma(x, y))
    elif op == 2:
        print("Resultado:")
        print(sub.subtrai(x, y))
    elif op == 3:
        print("Resultado:")
        print(mult.multiplica(x, y))
    elif op == 4:
        print("Resultado:")
        print(div.divide(x, y))
    elif op == 5:
        break
    else:
        print("Opção não reconhecida.")
    