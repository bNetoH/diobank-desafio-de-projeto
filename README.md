# DioBank - Simulador de Operações Bancárias

Projeto proposto no desafio: Suzano - Python Developer da Dio.me.

## Objetivo:

Simular operações bancárias básicas, permitindo depósitos, saques e a visualização de extratos financeiros diretamente pelo terminal.

## 📌 Funcionalidades

- **Depósito**: Permite adicionar valores ao saldo da conta.
- **Saque**: Permite saques de acordo com as regras de limites por transação e a quantidade de operações diárias.
- **Extrato**: Exibe o histórico de transações e o saldo atual.
- **Conhecer Limites**: Exibe regras de limites para saques.
- **Segurança**: Mensagens informativas sobre boas práticas bancárias.

## 🚀 Instalação e Execução

### Pré-requisitos

- Python 3.8+

### Passos

1. Clone este repositório:
   ```sh
   git clone https://github.com/bNetoH/diobank-desafio-de-projeto
   ```
2. Acesse a pasta do projeto:
   ```sh
   cd diobank-desafio-de-projeto
   ```
3. Execute o script principal:
   ```sh
   python main.py
   ```

## 🛠 Como Usar

1. Ao iniciar, um menu será exibido com as opções(vide exemplos[1])
2. Digite a letra correspondente para realizar a operação desejada.
3. Para depósitos e saques, informe o valor seguindo o formato brasileiro (exemplo: `100,50`).
4. O extrato exibirá todas as transações realizadas na sessão.
5. Para encerrar, basta selecionar `[q]`.

## 📝 Exemplos:

1. Menu

```
==============================
         DioBank.com
------------------------------

[d] Depósito
[s] Saque
[e] Extrato
[c] Conhecer Limites
[q] Sair

=>
```

2. Extrato

```
==============================
         DioBank.com
------------------------------
           Extrato
22-03-25       R$     500.50 +
22-03-25       R$     500.00 +
------------------------------
Saldo atual:     R$    1000.50
------------------------------
        Volte sempre!
==============================
```

## 📌 Melhorias Futuras

- [ ] Suporte para múltiplos usuários.
- [ ] Persistência de dados entre sessões.
- [ ] Interface gráfica.

## 📄 Licença

Este projeto é de código aberto e pode ser modificado conforme necessário.

---

✉️ Dúvidas ou sugestões? Entre em contato!
