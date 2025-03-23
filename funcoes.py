import os
from time import sleep
from datetime import datetime
from params import extrato,single_line,double_line,BANK_TITLE,MSG_RODAPE

def cabecalho_padrao():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(double_line)
    print(BANK_TITLE.center(40))
    print(single_line)

def rodape_padrao():
    print(single_line)
    print(MSG_RODAPE.center(40))
    print(double_line)

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

def formatar_linha_adicionar_extrato(valor, operador):
    datahora = f"{datetime.today().strftime('%d-%m-%y %H:%M:%S')}"  
    valor = f"R$ % 10.2f" % valor                      
    registro = f"{datahora}        {valor} {operador}"   
    extrato.append(registro)


def contar_transacoes_hoje():
    data_atual = datetime.today().strftime('%d-%m-%y')
    transacoes_hoje = sum(1 for item in extrato if item.startswith(data_atual))
    return transacoes_hoje



