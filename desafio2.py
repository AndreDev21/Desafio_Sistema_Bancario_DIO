# import textwrap


# def menu():
#     menu = """\n
#     ================ MENU ================
#     [d]\tDepositar
#     [s]\tSacar
#     [e]\tExtrato
#     [nc]\tNova conta
#     [lc]\tListar contas
#     [nu]\tNovo usuário
#     [q]\tSair
#     => """
#     return input(textwrap.dedent(menu))


# def depositar(saldo, valor, extrato, /):
#     if valor > 0:
#         saldo += valor
#         extrato += f"Depósito:\tR$ {valor:.2f}\n"
#         print("\n=== Depósito realizado com sucesso! ===")
#     else:
#         print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

#     return saldo, extrato


# def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
#     excedeu_saldo = valor > saldo
#     excedeu_limite = valor > limite
#     excedeu_saques = numero_saques >= limite_saques

#     if excedeu_saldo:
#         print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

#     elif excedeu_limite:
#         print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

#     elif excedeu_saques:
#         print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

#     elif valor > 0:
#         saldo -= valor
#         extrato += f"Saque:\t\tR$ {valor:.2f}\n"
#         numero_saques += 1
#         print("\n=== Saque realizado com sucesso! ===")

#     else:
#         print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

#     return saldo, extrato


# def exibir_extrato(saldo, /, *, extrato):
#     print("\n================ EXTRATO ================")
#     print("Não foram realizadas movimentações." if not extrato else extrato)
#     print(f"\nSaldo:\t\tR$ {saldo:.2f}")
#     print("==========================================")


# def criar_usuario(usuarios):
#     cpf = input("Informe o CPF (somente número): ")
#     usuario = filtrar_usuario(cpf, usuarios)

#     if usuario:
#         print("\n@@@ Já existe usuário com esse CPF! @@@")
#         return

#     nome = input("Informe o nome completo: ")
#     data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
#     endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

#     usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

#     print("=== Usuário criado com sucesso! ===")


# def filtrar_usuario(cpf, usuarios):
#     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
#     return usuarios_filtrados[0] if usuarios_filtrados else None


# def criar_conta(agencia, numero_conta, usuarios):
#     cpf = input("Informe o CPF do usuário: ")
#     usuario = filtrar_usuario(cpf, usuarios)

#     if usuario:
#         print("\n=== Conta criada com sucesso! ===")
#         return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

#     print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


# def listar_contas(contas):
#     for conta in contas:
#         linha = f"""\
#             Agência:\t{conta['agencia']}
#             C/C:\t\t{conta['numero_conta']}
#             Titular:\t{conta['usuario']['nome']}
#         """
#         print("=" * 100)
#         print(textwrap.dedent(linha))


# def main():
#     LIMITE_SAQUES = 3
#     AGENCIA = "0001"

#     saldo = 0
#     limite = 500
#     extrato = ""
#     numero_saques = 0
#     usuarios = []
#     contas = []

#     while True:
#         opcao = menu()

#         if opcao == "d":
#             valor = float(input("Informe o valor do depósito: "))

#             saldo, extrato = depositar(saldo, valor, extrato)

#         elif opcao == "s":
#             valor = float(input("Informe o valor do saque: "))

#             saldo, extrato = sacar(
#                 saldo=saldo,
#                 valor=valor,
#                 extrato=extrato,
#                 limite=limite,
#                 numero_saques=numero_saques,
#                 limite_saques=LIMITE_SAQUES,
#             )

#         elif opcao == "e":
#             exibir_extrato(saldo, extrato=extrato)

#         elif opcao == "nu":
#             criar_usuario(usuarios)

#         elif opcao == "nc":
#             numero_conta = len(contas) + 1
#             conta = criar_conta(AGENCIA, numero_conta, usuarios)

#             if conta:
#                 contas.append(conta)

#         elif opcao == "lc":
#             listar_contas(contas)

#         elif opcao == "q":
#             break

#         else:
#             print("Operação inválida, por favor selecione novamente a operação desejada.")


# main()


# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

# Módulo 're' que fornece operações com expressões regulares.
import re


 # TODO: Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
def validate_numero_telefone(phone_number):
   
    # TODO: Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
   
    # A função 're.match()' para verifica se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match('\(\d{2}\) 9\d{4}-\d{4}', phone_number):  
        return 'Número de telefone válido.'
        # TODO: Agora crie um return, para retornar que o número de telefone é válido:
    else:
      return '	Número de telefone inválido.'
       
       # TODO: Crie um else e return, caso não o número de telefone seja inválido:
    

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()  

# TODO: Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.

result = validate_numero_telefone(phone_number)

# Imprime o resultado:
print(result)