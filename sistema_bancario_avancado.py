saldo = 0
limite = 500
LIMITE_DE_SAQUE_DIARIO = 3
extrato = ""

usuario = {"nome":"","idade":0,"email":"email","senha":"senha","cpf":"cpf"}

def criarUsuario():
    verificar_senha_cadastro = ""
    verificar_senha_novamente = ""

    usuario["nome"] = input("Informe o seu nome: ")
    usuario["idade"] = input("Informe a sua idade: ")
    usuario["email"] = input("Informe o seu email: ")
    usuario["cpf"] = input("Informe o seu CPF: ")

    while True:
        verificar_senha_cadastro = input("digite a senha que deseja cadastrar: ")
        verificar_senha_novamente = input("digite a senha novamente: ")

        if(verificar_senha_cadastro==verificar_senha_novamente):
            usuario["senha"] = verificar_senha_cadastro
            break
        else:
            print("As senhas não são iguais")

    print("Sua conta foi criada com sucesso !")
    


def login():
    cpf_login = ""
    senha_login = ""

    while True:
        cpf_login = input("Informe o seu cpf: ")
        senha_login = input("Informe a sua senha: ")

        if senha_login==usuario["senha"] and cpf_login==usuario["cpf"]:
            return True

        elif cpf_login != usuario["cpf"]:
            print("CPF informado não foi cadastrado  \n\n Deseja criar uma conta ?\n[1] SIM\n[2] SAIR \n[3] Tentar novamente")

            opcao = int(input("Informe a opcao: "))

            if opcao == 1:
                criarUsuario()
            elif opcao == 2:
                break
            elif opcao > 3 and opcao < 1:
                print("Numero digitado está incorreto")

        else: 
            print(" Senha incorreta ")
            return False

while True:
    print(""" 
      
    =============== MENU ================
      
      [1] Já possuo uma conta
      [2] Desejo criar uma conta]
      [3] Sair

    """)

    opcao = int(input("Informe a opcao desejada: "))

    if opcao == 1:
        if login():
            contador_saques = 0
            print(f"Bem vindo {usuario['nome']} !")


            extrato = """
            ========== EXTRATO =========

                    """
            
            while True:
                menu_banco = f"""

                        Saldo: {saldo} 

                        [1] Depositar
                        [2] Sacar
                        [3] Extrato
                        [4] Sair
                        

                        """
                print(menu_banco)
                opcao = int(input("Digite a opcao: "))

                if opcao == 1:
                    valor_de_deposito = float(input("Qual o valor que deseja depositar ?"))

                    saldo += valor_de_deposito

                    extrato += f"\nDEPOSITO: {valor_de_deposito:.2f}"

                elif opcao == 2:
                    valor_de_saque = float(input("Digite o valor que deseja sacar: "))

                    if valor_de_saque > limite:
                        print("valor de saque informado, e maior que o limite de saque")

                    elif contador_saques >= LIMITE_DE_SAQUE_DIARIO:
                        print("Seu limite de saque diario foi atingido")

                    elif valor_de_saque>saldo:
                        print("Saldo insuficiente")
                    
                    else:
                        saldo -= valor_de_saque
                        contador_saques += 1
                        extrato += f"\nSAQUE: {valor_de_saque:.2f}"

                elif opcao == 3:
                    print(extrato)

                elif opcao == 4:
                    break
                
                else:
                    print("Opcao invalida")

                

    elif opcao == 2:
        criarUsuario()

    elif opcao == 3:
        break

    else:
        print("Opcao invalida !")