menu = """
[d] Depósito
[s] Saque
[b] Saldo
[e] Extrato
[u] Cadastrar Cliente
[v] Listar Clientes
[c] Cadastrar Conta
[l] Listar Contas
[k] Conhecer Limites
[q] Sair

=> """

contas = []
usuarios = []
limite_transacoes = 10
saldo = 0
limite = 500
extrato = []
qtde_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
single_line = "-" * 40
double_line = "=" * 40
BANK_TITLE = "DioBank.com"
MSG_RODAPE = "Volte sempre!" 
MSG_OPERACAO = "Digite o valor: "
GOODBYE_MSG = """
Para sua segurança, NUNCA aceite ajuda 
de estranhos nos caixas eletrônicos.

Mantenha sua SENHA sempre segurança.
"""
KNOWN_LIMITS = f"""
O valor limite para saques é de R$ {limite} 
por operação.

E ainda,  as operações  de  saque  estão 
limitadas a {LIMITE_SAQUES} por dia.

O limite global das transações depósitos 
somados aos saques, é de {limite_transacoes} transações 
por dia.
"""


