import os
from time import sleep
from datetime import datetime
from params import extrato,SINGLE_LINE,DOUBLE_LINE,BANK_TITLE,MSG_RODAPE,PRESS_ANY_KEY

def cabecalho_padrao():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(DOUBLE_LINE)
    print(BANK_TITLE.center(40))
    print(SINGLE_LINE)

def rodape_padrao():
    print(SINGLE_LINE)
    print(MSG_RODAPE.center(40))
    print(DOUBLE_LINE)

def emitir_recibo(valor, operacao):
    cabecalho_padrao()
    value = f"Valor: R$ {valor}"
    datahora = f"Data: {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}" 
    print(operacao.title().center(40))
    print("\n" + value.center(40))
    print("\n" + datahora.center(40))
    rodape_padrao()
    sleep(3)

def validar_entrada(entrada):
    valor = entrada.replace(".", "").replace(",", ".")
    try:
        valor_validado = float(valor)
        if valor_validado > 0:
            return valor_validado
        else:
            return 0
    except ValueError:
        return 0

def formatar_linha_extrato(valor, operador):
    datahora = f"{datetime.today().strftime('%d-%m-%y %H:%M:%S')}"  
    valor = f"R$ % 10.2f" % valor                      
    registro = f"{datahora}        {valor} {operador}\n"
    return registro 

def contar_transacoes_hoje():
    data_atual = datetime.today().strftime('%d-%m-%y')
    transacoes_hoje = sum(1 for item in extrato if item.startswith(data_atual))
    return transacoes_hoje

def depositar(saldo, valor, extrato, operador, operacao, /):
    valor = validar_entrada(valor)

    print(SINGLE_LINE)
    if valor > 0:
        saldo += valor
        operador = "+"
        extrato = formatar_linha_adicionar_extrato(valor,operador)
        print("Aguarde seu recibo")
        sleep(3)
        emitir_recibo(valor, operacao)
    else:
        print("Valor inválido, operação cancelada")
        sleep(3)
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, qtde_saques, limite_saques, operador, operacao):
    valor = validar_entrada(valor)
    excedeu_saldo = saldo < valor
    excedeu_limite = valor > limite
    excedeu_saques = qtde_saques >= limite_saques
    print(SINGLE_LINE)

    if excedeu_saldo:
        print("Saldo insuficiente.")
        sleep(3) 
    elif excedeu_limite:
        print(f"Valor acima do limite de R$ {limite} por saque.")
        sleep(3)
    elif excedeu_saques:
        print(f"Limite de ({limite_saques}) saques excedido.")
        sleep(3)
    elif valor > 0:
        saldo -= valor
        extrato = formatar_linha_extrato(valor,operador)
        qtde_saques += 1
        print("Aguarde seu recibo")
        sleep(3)
        emitir_recibo(valor, operacao)
    else:
        print("Valor inválido, operação cancelada!")
        sleep(3)

    return saldo, extrato

def exibir_extrato(saldo, /, *,extrato):
    print("Sem transações para exibir" if not extrato else extrato)
    print(SINGLE_LINE)
    print("Saldo atual:             R$ % 10.2f" % saldo)
    rodape_padrao()
    print(input("\n\nPressione qualquer tecla"))

def validar_usuario(cpf, usuarios, /):
    usuario_encontrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_encontrado[0] if usuario_encontrado else None

def criar_usuario(usuarios):
    print("Informe o documento somente números.")
    cpf = input("CPF: ")

    usuario = validar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário já possui cadastro!")
        sleep(3)
        return

    print("Informe o nome completo sem abreveaturas.")    
    nome = input("Nome: ")
    print("Informe a data de nascimento.")
    data_nascimento = input("dd-mm-aaaa: ")
    print("Informe o endereço.")
    logradouro = input("Logradouro, n°: ")
    complemento = input("Complemento: ")
    bairro = input("Bairro: ")
    cidade_estado = input("Cidade/UF: ")

    if complemento:
        endereco = f"{logradouro} - {complemento} - {bairro} - {cidade_estado}"
    else:
        endereco = f"{logradouro} - {bairro} - {cidade_estado}"

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")
    sleep(3)

def listar_usuarios(usuarios):
    if len(usuarios) > 0:
        print("CPF" + " " * 9 + "Nome")
        for usuario in usuarios:
            linha = f"{usuario["cpf"]} {usuario["nome"]}"
            print(linha)
            print(SINGLE_LINE)
    else:
        print("\nNão existem usuários cadastrados!")
        print(SINGLE_LINE)

    print(input(PRESS_ANY_KEY))


def criar_conta(agencia, numero_conta, usuarios, contas, /):
    print("Informe o documento somente números.")
    cpf = input("CPF: ")
    usuario = validar_usuario(cpf, usuarios)

    if usuario:
        formatar_conta = f"{numero_conta:09}"
        contas.append({"agencia": agencia, "numero_conta": formatar_conta, "usuario": usuario})
        print("Conta criada com sucesso!")

    print("Usuário não possui cadastro, operação cancelada!")

    sleep(3)

def listar_contas(contas):
    if len(contas) > 0:
        print("Agência "+"C/C"+" " * 7 + "Titular")
        for conta in contas:
            linha = f"{" " * 3 + conta["agencia"] + " " + conta["numero_conta"] + " " + conta["usuario"]["nome"]}"
            print(linha)
            print(SINGLE_LINE)
    else:
        print("\nNão existem contas cadastradas!")
        print(SINGLE_LINE)

    print(input(PRESS_ANY_KEY))