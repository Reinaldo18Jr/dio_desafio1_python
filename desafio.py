menu = '''
               Bem-vindo ao Banco Python!

              =========== MENU ===========

              [d] Depositar
              [s] Sacar
              [e] Extrato
              [q] Sair

              ============================
''' 


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print('''
              ========= Depósito =========
              ''')
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            print(f"Depósito de: R$ {valor:.2f} realizado com sucesso!")
            extrato += f'''
              Depósito de: R$ {valor:.2f}'''

        else:
            print("Operação Cancelada! O valor Informado não é válido.")

    elif opcao == "s":
        print('''
              ========== Saque ===========
              ''')
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Cancelada! Você não possui saldo suficiente.")

        elif excedeu_limite:
            print("Operação Cancelada! O valor do saque excedeu o limite.")

        elif excedeu_saques:
            print("Operação Cancelada! Número máximo de saques foi excedido.")

        elif valor > 0:
            saldo -= valor
            print(f"Saque de: R$ {valor:.2f} realizado com sucesso!")
            extrato += f'''
              Saque de: R$ {valor:.2f}'''
            numero_saques += 1

        else:
            print("Operação Cancelada! O valor informado não é válido.")

    elif opcao == "e":
        print('''
              ========= Extrato ==========
              ''')
        print('''
              não foram realizadas movimentações.
              ''' if not extrato else extrato)
        print(f'''
              Saldo: R$ {saldo:.2f}
              ''')
        print('''
              ============================
              ''')

    elif opcao == "q":
        print("Obrigado por usar o Banco Python, tenha um bom dia!")
        break

    else:
        print("Operação Inválida! Por favor selecione um item do MENU.")