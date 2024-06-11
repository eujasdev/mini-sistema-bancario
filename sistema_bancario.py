menu = """
====Sistema báncario====

    [1] Depositar
    [2] Sacar
    [3] Ver extrato
    [0] Sair

========================

=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    if opcao == "1":

        valor = (float(input("Digite o valor que dejesa depositar: ")))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print(f"O valor de R${valor} foi creditado na sua conta. ")
            
        else:
            print("Valor de déposito inválido !")

    elif opcao == "2":
        valor = (float(input("Digite o quanto quer sacar: ")))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES


        if excedeu_saldo:
            print(f"O valor é mais alto do que você tem em conta, saldo atual R${saldo}")

        elif excedeu_limite:
            print("O valor do saque é muito alto, nosso máximo é de R$500")

        elif excedeu_saques:
            print("Você ja passou do número de saques diários permitidos")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"O valor de R${valor} foi debitado na sua conta. ")
        else:
            print("O valor do saque é inválido")
        
    elif opcao == "3":
        print("======Extrato======")
        print(f"Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo = R${saldo:.2f}")

    elif opcao == "0":
        break

    else:
        print("Operação inválida")

    