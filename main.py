import re
from datetime import datetime
from time import sleep
from params import menu, saldo,limite,extrato,qtde_saques,LIMITE_SAQUES,single_line,MSG_OPERACAO,GOODBYE_MSG,KNOWN_LIMITS
from funcoes import cabecalho_padrao,rodape_padrao,emitir_recibo,validar_entrada,formatar_linha_adicionar_extrato

padrao = r"\[([a-zA-Z])\]\s+(.+)"
opcoes = dict(re.findall(padrao, menu))

while True:
    cabecalho_padrao()
    opcao = input(menu).strip().lower()
    if opcao in opcoes:

        if opcao == "d":
            operacao = opcoes[opcao]
            print(operacao.title().center(30))
            entrada = input(MSG_OPERACAO).strip()

            valor = validar_entrada(entrada)
            print(single_line)

            if valor > 0:
                saldo += valor
                operador = "+" if opcao == "d" else "-"
                formatar_linha_adicionar_extrato(valor,operador)
                print("Aguarde seu recibo")
                sleep(3)
                emitir_recibo(valor, operacao)
            else:
                print("Valor inválido, operação cancelada")
                sleep(3)

        elif opcao == "s":
            operacao = opcoes[opcao]
            print(operacao.title().center(30))
            entrada = input(MSG_OPERACAO).strip()

            valor = validar_entrada(entrada)
            print(single_line)

            if valor > 0:
                if valor > 500: 
                    print(f"Valor acima do limite de\nR$ {limite} por saque.")
                    sleep(3)
                elif qtde_saques >= LIMITE_SAQUES:
                    print(f"Limite({LIMITE_SAQUES}) de saque atingido.")
                    sleep(3)
                elif saldo < valor:
                    print("Saldo insuficiente.")
                    sleep(3) 
                else:
                    saldo -= valor
                    operador = "+" if opcao == "d" else "-"
                    formatar_linha_adicionar_extrato(valor,operador)
                    qtde_saques += 1
                    print("Aguarde seu recibo")
                    sleep(3)
                    emitir_recibo(valor, operacao)
            else:
                print("Valor inválido,\noperação cancelada!")
                sleep(3)

        elif opcao == "e":
            cabecalho_padrao()
            operacao = opcoes[opcao]
            print(operacao.title().center(30))
            for item in extrato:
                print(item)
            print(single_line)
            print("Saldo atual:   R$ % 10.2f" % saldo)
            rodape_padrao()
            print(input("\n\nPressione qualquer tecla"))

        elif opcao == "c":
            cabecalho_padrao()            
            print(KNOWN_LIMITS)
            rodape_padrao()
            print(input("\n\nPressione qualquer tecla"))
        elif opcao == "q":
            cabecalho_padrao()
            msg_centralizada = "\n".join(line.center(30) for line in GOODBYE_MSG.strip().split("\n"))
            print(msg_centralizada)
            rodape_padrao()
            break

        else:
            print("Opção inválida,\npor favor\nselecione uma operação válida.")

    else:
        print("Opção inválida,\npor favor\nselecione uma operação válida.")
