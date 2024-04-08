saldo = 0.0
contador_de_saques = 0
extrato = "  EXTRATO BANCARIO  "
limite = 500
LIMITE_DE_SAQUES = 3
numero_de_saques = 0

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
    opcao = int(input("Digite a opcao da operacao que deseja realizar: "))

    # Depositar
    if opcao == 1:
        # Criar uma variavel para armazenar a quantidade de deposito que o cliente deseja solicitar
        valor_de_deposito_str = input("Qual o valor que deseja depositar: ")

        # Substituir vírgulas por pontos (caso existam)
        valor_de_deposito_str = valor_de_deposito_str.replace(',', '.')

        # Converter para float
        valor_de_deposito = float(valor_de_deposito_str)

        # Adicionar ao meu saldo
        saldo += valor_de_deposito

        # Adicionando a Operação ao meu Extrato
        valor_de_deposito = round(valor_de_deposito, 2)
        extrato += f"\nDeposito R${valor_de_deposito}"

    # Operacao de Saque
    if opcao==2:
        
        #Criar uma variavel para armazenar a quantidade que o cliente deseja sacar
        valor_de_saque_str = input("Qual o valor que deseja sacar: ")

        # Substituir vírgulas por pontos(caso existam)
        valor_de_saque_str = valor_de_saque_str.replace(',','.')

        # Converter para float
        valor_de_saque = float(valor_de_saque_str)

        # Verificar se o valor de saque é maior que o limite
        if valor_de_saque>limite:
            print(limite)
            print(valor_de_saque)
            print("Erro!. O valor de saque e maior que o limite")
        # Verificar se o valor quantas operações ja foram realizadas de saque
        elif numero_de_saques==LIMITE_DE_SAQUES:
            print("Erro!. O seu limite de saques diario foi atingigo")
        # Verificar se o valor de saque é menor que 0 (pois não existe saque negativo)
        elif valor_de_saque<0:
            print("Erro!. O valor de saque é menor que 0")
        
        else:
            saldo -= valor_de_saque
            numero_de_saques = numero_de_saques + 1
            extrato += f"\nSaque R${valor_de_saque}"

            print("Valor sacado com Sucesso !")

    # Operacao de Extrato
    if opcao==3:
        print(extrato)
    # Sair do Sistema
    if opcao == 4:
        break
