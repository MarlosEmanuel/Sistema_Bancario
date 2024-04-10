saldo = 0.0
contador_de_saques = 0
extrato = "  EXTRATO BANCARIO  "
limite = 500
LIMITE_DE_SAQUES = 3
numero_de_saques = 0

def saque(valor_de_saque=0):
    global saldo
    global numero_de_saques
    global extrato
    global LIMITE_DE_SAQUES
    global limite
    
    # Verificar se o valor de saque é maior que o limite
    if valor_de_saque > limite:
        print("Erro! O valor de saque é maior que o limite")
    # Verificar se o valor de saque é menor que 0 (pois não existe saque negativo)
    elif valor_de_saque < 0:
        print("Erro! O valor de saque é menor que 0")
    else:
        # Verificar se o número de saques atingiu o limite diário
        if numero_de_saques == LIMITE_DE_SAQUES:
            print("Erro! O seu limite de saques diário foi atingido")
        else:
            saldo -= valor_de_saque
            numero_de_saques += 1
            extrato += f"\nSaque R${valor_de_saque}"
            print("Valor sacado com sucesso!")

def depositar(valor_de_deposito=0.0):
        global saldo
        global extrato

        # Adicionar ao meu saldo
        saldo += valor_de_deposito

        # Adicionando a Operação ao meu Extrato
        valor_de_deposito = round(valor_de_deposito, 2)
        extrato += f"\nDeposito R${valor_de_deposito}"


while True:
    menu = f"""
            Sistema Bancario

        Saldo: {saldo}

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair

"""
    # Menu
    print(menu)
    opcao = float(input("Digite a opcao da operacao que deseja realizar: "))

    # Depositar
    if opcao == 1:
        
        depositar(float(input("Digite o valor que deseja depositar: ")))

    # Operacao de Saque
    if opcao==2:

        saque(float(input("Digite o valor que deseja sacar: ")))

    # Operacao de Extrato
    if opcao==3:
        print(extrato)
    # Sair do Sistema
    if opcao == 4:
        break
