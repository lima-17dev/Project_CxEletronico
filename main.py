saldo = 1000
emprestimo = 0
print(""" Bem vido ao seu caixa eletrônico!

Opções atuais:

1 = Ver Saldo. 2 = Depositar valor. 3 = Sacar valor. 4 = Pedir empréstimo. 5 = Pagar empréstimo. 6 = Consultar Empréstimo. 7 = Sair " """"")
print()
opMenu = int(input("Digite qual opção você deseja seguir: "))
while opMenu != 7:
    if opMenu == 1:
        print(f"Seu saldo é : R$ {saldo}")
    elif opMenu == 2:
        deposito = float(input("Digite o valor a ser depoisitado: "))
        saldo = deposito + saldo
        print(f"Deposito no valor de : R$ {deposito} realizado com sucesso. Seu saldo Atual é: {saldo}")
    elif opMenu == 3:
        saque = float(input("Digite o valor a ser sacado: "))
        if saque <= saldo:
            saldo = saldo - saque
            print(f"Saque no valor de : R$ {saque} realizado com sucesso. Seu saldo Atual é: {saldo}")
        else:
            print("Saldo insuficiente para saque solicitado. Tente realizar o saque com outro valor. ")
    elif opMenu == 4:
        peEmprestimo = float(input("Digite o valor a ser solicitado: "))
        emprestimo = peEmprestimo + emprestimo
        saldo = peEmprestimo + saldo
        print(f"Seu empréstimo de: {peEmprestimo} foi realizado com sucesso. Seu saldo atual é de R$ {saldo}")
    elif opMenu == 5:
        paEmprestimo = float(input("Digite o valor a ser quitado: "))
        emprestimo = emprestimo - paEmprestimo
        saldo = saldo - paEmprestimo
            if paEmprestimo > saldo:
                print(f"Seu saldo é insuficiente para quitar seu empréstimo!")
            else:
        print(f"O valor de R$ {paEmprestimo} foi quitado da sua conta. Seu saldo atual é de R$ {saldo}. E seu empréstimo atual é de R$ {emprestimo}")
    elif opMenu == 6:
        print(f"Seu empréstimo atual é de: R$ {emprestimo}")
    opMenu = int(input("Digite novamente a sua opção: "))