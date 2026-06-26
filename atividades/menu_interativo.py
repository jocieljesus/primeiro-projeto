import time

while True:
    opcao = int(input(""" 
    MENU  
        1 - Somar
        2 - Subtrair
        3 - Multiplicar
        4 - Dividir
        5 - Sair
        Digite sua opçao: """))

    if opcao == 1:
        print("SOMAR")
    elif opcao == 2:
        print("SUBTRAIR")
    elif opcao == 3:
        print("MULTIPLICAR")
    elif opcao == 4:
        print("DIVIDIR")
    elif opcao == 5:
        print("Saindo...")
        time.sleep(1)
        break
    else:
        print("Opção inválida, escolha uma nova.")


