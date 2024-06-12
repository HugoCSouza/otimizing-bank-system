def deposito(saldo, valor, extrato, /): # Ao colocar a barra, os argumentos são todos posicional
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("O valor do depósito deve ser maior que 0!")
    return saldo, extrato

def saque(*, n_saques, dinheiro_sacado_dia, saldo, extrato):
    limite_saques, limite_diario = 3, 1000
    if n_saques >= limite_saques:
        print("Você já realizou a quantidade máxima de saques diários!")
    elif dinheiro_sacado_dia >= limite_diario:
        print(f"Você já sacou seu limite diário (R$ {limite_diario:.2F})!")
    else:
        valor_saque = float(input("\tDigite o valor que deseja sacar: "))
        if valor_saque > saldo:
            print("Saldo indisponível!")
        elif valor_saque >= limite_diario:
            print("Seu saque é maior que seu limite diário!")
        else:
            saldo -= valor_saque
            dinheiro_sacado_dia += valor_saque
            n_saques += 1
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
    return n_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n","*"*20,"Extrato","*"*20)
    print("Não existem movimentação na conta" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("*"*50)

def criar_usuario(usuarios):
    cpf = input("Informe o CPF a ser cadastrado (Somente números): ")
    verificação = any(usuario['cpf'] == cpf for usuario in usuarios)
    
    if verificação:
        print('*'*40,'CPF já cadastrado','*'*40)
    else:
        nome = input("Digite o nome do cliente: ")
        data_nascimento = input("Digite a data de nascimento do cliente (DD-MM-AAAA): ")
        endereço = input('Digite o endereço do cliente (Logradouro, Nº, Bairro, Cidade, UF): ')
        
        usuarios.append({"nome": nome, "CPF": cpf, "Data de nascimento": data_nascimento, "Endereço": endereço})
        
        print('*'*30,'Usúario criado com sucesso','*'*30,'\n'
              '\t\t Dados cadastrados: \n',
              f'\t\tNome: {usuarios[-1]["nome"]} \n',
              f'\t\tCPF: {usuarios[-1]["CPF"]} \n',
              f'\t\tData de nascimento: {usuarios[-1]["Data de nascimento"]} \n',
              f'\t\tEndereço: {usuarios[-1]["Endereço"]} \n')
        

menu = ('\n\n' + "*"*20 + "Bem vindo ao Bancão " + "*"*20 +"\n\n\n"
        "\t\t'1' - Depósito \n"
        "\t\t'2' - Saque\n"
        "\t\t'3' - Extrato\n"
        "\t\t'4' - Criar Usuário\n"
        "\t\t'0' - Sair\n" )
saldo, saques_feitos, valor_ja_sacado = 0, 0, 0
extrato = ""
lista_usuarios = []
while True:
    opcao = int(input(menu))
    if opcao == 1:
        valor_deposito = float(input("\tDigite o valor que deseja depositar: "))
        saldo, extrato = deposito(saldo, valor_deposito, extrato)
    elif opcao == 2:
        saques_feitos = saque(
                            n_saques = saques_feitos,
                            dinheiro_sacado_dia = valor_ja_sacado,
                            saldo = saldo,
                            extrato = extrato
                            )
    elif opcao == 3:
        exibir_extrato(saldo, extrato = extrato)
    elif opcao == 4:
        criar_usuario(lista_usuarios)
    elif opcao == 0:
        break
    else:
        print("Operação inexistente")
    
