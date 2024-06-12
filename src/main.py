menu = ("*"*20 + "Bem vindo ao Bancão " + "*"*20 +"\n"
        "\t'1' - Depósito \n"
        "\t'2' - Saque\n"
        "\t'3' - Extrato\n"
        "\t'0' - Sair\n" )
saldo = 0
limite_diario = 500
extrato = ""
saques_feitos = 0
limite_saques = 3
valor_ja_sacado = 0
while True:
    opcao = int(input(menu))
    if opcao == 1:
        valor_deposito = float(input("\tDigite o valor que deseja depositar: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        else:
            print("O valor do depósito deve ser maior que 0!")
    elif opcao == 2:
        if saques_feitos >= limite_saques:
            print("Você já realizou a quantidade máxima de saques diários!")
        elif valor_ja_sacado >= limite_diario:
            print(f"Você já sacou seu limite diário (R$ {limite_diario:.2F})!")
        else:
            valor_saque = float(input("\tDigite o valor que deseja sacar: "))
            if valor_saque > saldo:
                print("Saldo indisponível!")
            elif valor_saque >= limite_diario:
                print("Seu saque é maior que seu limite diário!")
            else:
                saldo -= valor_saque
                valor_ja_sacado += valor_saque
                saques_feitos += 1
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
    elif opcao == 3:
        print("\n","*"*20,"Extrato","*"*20)
        print("Não existem movimentação na conta" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("*"*50)
    elif opcao == 0:
        break
    else:
        print("Operação inexistente")
    
