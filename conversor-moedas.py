import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
cotacao_dolar = 5.36
cotacao_euro = 6.25
cotacao_iene = 28.39
cotacao_pesoA = 274.94


print("seja bem vindo ao convertor de moedas!")
saldo_real = float(input(f"digite o seu saldo em real: "))
while True:
    limpar_tela()
    print("seu saldo é:", saldo_real)
    print("===== ESCOLHA A MOEDA QUE DESEJA CONVERTER O REAL =====")
    print("1 - dolar")
    print("2 - euro")
    print("3 - iene")
    print("4 - pesoA")
    print("0 - Sair")

    opcao = input("\nescolha a opçao que deseja converter o saldo:")

    if opcao == '1':
        saldo_convertido = saldo_real / cotacao_dolar
        print(f"\no saldo convertido em dolar foi {saldo_convertido:.2f}")
    elif opcao == '2':
        saldo_convertido = saldo_real / cotacao_euro
        print(f"\no saldo convertido em euro foi {saldo_convertido:.2f}")
    elif opcao == '3':
        saldo_convertido = saldo_real / cotacao_iene
        print(f"\no saldo convertido em iene foi {saldo_convertido:.2f}")
    elif opcao == '4':
        saldo_convertido = saldo_real / cotacao_pesoA
        print(f"\no saldo convertido em peso Argentino foi {saldo_convertido:.2f}")
    elif opcao == '0':
        print("\nsaindo do sitema, TCHAUUUU")
        break
    else:
        print("\nOPÇÃO INDISPONIVEL, ESCOLHA OUTRA")
        
    input("\npressio ENTER para retornar ao menu")
