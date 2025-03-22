menu = """
[d] Depósito
[s] Saque
[e] Extrato
[c] Conhecer Limites
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
qtde_saques = 0
LIMITE_SAQUES = 3
single_line = "-" * 30
double_line = "=" * 30
BANK_TITLE = "DioBank.com"
MSG_RODAPE = "Volte sempre!" 
MSG_OPERACAO = "Digite o valor: "
GOODBYE_MSG = """
Para sua segurança, NUNCA 
aceite ajuda de estranhos 
nos caixas eletrônicos.

Mantenha sua SENHA sempre
em segurança.
"""
KNOWN_LIMITS = f"O valor limite para saque é de\nR$ {limite} por operação.\n\nAs operações de saque estão\nlimitadas a {LIMITE_SAQUES} por dia."


