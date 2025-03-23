import re
from time import sleep
from params import menu, saldo, limite_transacoes, limite, extrato, qtde_saques, usuarios, contas, LIMITE_SAQUES, MSG_OPERACAO, GOODBYE_MSG, KNOWN_LIMITS, AGENCIA
from funcoes import cabecalho_padrao, rodape_padrao, contar_transacoes_hoje, depositar, sacar, exibir_extrato, criar_usuario, listar_usuarios, criar_conta, listar_contas

padrao = r"\[([a-zA-Z])\]\s+(.+)"
opcoes = dict(re.findall(padrao, menu))

while True:
    cabecalho_padrao()
    opcao = input(menu).strip().lower()
    if opcao in opcoes:

        if opcao == "d":
            total_transacoes = contar_transacoes_hoje()
            if total_transacoes < limite_transacoes:
                operacao = opcoes[opcao]
                print(operacao.title().center(40))
                valor = input(MSG_OPERACAO).strip()
                operador = "+" if opcao == "d" else "-"
                saldo, extrato = depositar(saldo, valor, extrato, operador, operacao)
            else:
                print("Limite de transações excedido.\nTente novamente amanhã.")
                sleep(3)

        elif opcao == "s":
            total_transacoes = contar_transacoes_hoje()
            if total_transacoes < limite_transacoes:
                operacao = opcoes[opcao]
                print(operacao.title().center(40))
                valor = input(MSG_OPERACAO).strip()
                operador = "+" if opcao == "d" else "-"

                saldo, extrato = sacar(
                    saldo=saldo, 
                    valor=valor, 
                    extrato=extrato,
                    limite=limite,
                    qtde_saques=qtde_saques,
                    limite_saques=LIMITE_SAQUES, 
                    operador=operador, 
                    operacao=operacao
                )
            else:
                print("Limite de transações excedido.\nTente novamente amanhã.")
                sleep(3)

        elif opcao == "b":
            cabecalho_padrao()
            operacao = opcoes[opcao]
            print(operacao.title().center(40))
            print("Saldo atual:             R$ % 10.2f" % saldo)
            rodape_padrao()
            print(input("\n\nPressione qualquer tecla"))

        elif opcao == "e":
            cabecalho_padrao()
            operacao = opcoes[opcao]
            print(operacao.title().center(40))

            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            cabecalho_padrao()
            operacao = opcoes[opcao]
            print(operacao.title().center(40))
            criar_usuario(usuarios)

        elif opcao == "v":
            cabecalho_padrao()
            operacao = opcoes[opcao]
            print(operacao.title().center(40))
            listar_usuarios(usuarios)

        elif opcao == "c":
            cabecalho_padrao()
            operacao = opcoes[opcao]
            print(operacao.title().center(40))
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA, numero_conta, usuarios, contas)

        elif opcao == "l":
            cabecalho_padrao()
            operacao = opcoes[opcao]
            print(operacao.title().center(40))
            listar_contas(contas)

        elif opcao == "k":
            cabecalho_padrao()
            msg_centralizada = "\n".join(line.center(40) for line in KNOWN_LIMITS.strip().split("\n"))
            print(msg_centralizada)       
            rodape_padrao()
            print(input("\n\nPressione qualquer tecla"))

        elif opcao == "q":
            cabecalho_padrao()
            msg_centralizada = "\n".join(line.center(40) for line in GOODBYE_MSG.strip().split("\n"))
            print(msg_centralizada)
            rodape_padrao()
            break

        else:
            print("Opção inválida,\npor favor\nselecione uma operação válida.")

    else:
        print("Opção inválida,\npor favor\nselecione uma operação válida.")
