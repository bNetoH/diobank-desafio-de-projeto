# DioBank - Simulador de Operações Bancárias

Projeto proposto no desafio: Suzano - Python Developer da Dio.me.

## Objetivo:

Simular operações bancárias básicas, permitindo depósitos, saques, visualização de saldo e a visualização de extratos financeiros diretamente pelo terminal.

## 📌 Funcionalidades

- **Depósito**: Permite adicionar valores ao saldo da conta.
- **Saque**: Permite saques de acordo com as regras de limites por transação e a quantidade de operações diárias.
- **Saldo**: Exibe o saldo atual.
- **Extrato**: Exibe o histórico de transações e o saldo atual.
- **Cadastrar Cliente**: Permite cadastrar usuário(cliente).
- **Listar Clientes**: Exibe a lista de clientes.
- **Cadastrar Conta**: Permite cadastrar conta e vincular a mesma a um cliente.
- **Listar Contas**: Exibe lista de contas com seus respectivos titulares.
- **Conhecer Limites**: Exibe regras de limites para saques e limite global das transações.
- **Sair**: Mensagens de agradecimento e mensagens informativas sobre segurança e boas práticas bancárias.

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
========================================
              DioBank.com
----------------------------------------

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

=>
```

2. Extrato

```
========================================
              DioBank.com
----------------------------------------
                Extrato
23-03-25 00:47:51        R$     100.00 +
23-03-25 00:48:06        R$    1000.00 +
23-03-25 00:48:15        R$    1000.00 +
23-03-25 00:50:45        R$     400.00 +
23-03-25 00:51:03        R$      55.00 +
23-03-25 00:51:13        R$     343.00 +
23-03-25 00:51:24        R$     500.00 -
23-03-25 00:51:33        R$     500.00 -
23-03-25 00:51:43        R$     500.00 -
23-03-25 00:52:14        R$     600.00 +
----------------------------------------
Saldo atual:   R$    1998.00
----------------------------------------
             Volte sempre!
========================================


Pressione qualquer tecla
```

3. Conhecer Limites

```
========================================
              DioBank.com
----------------------------------------
O valor limite para saques é de R$ 500
             por operação.

E ainda,  as operações  de  saque  estão
         limitadas a 3 por dia.

O limite global das transações depósitos
somados aos saques, é de 10 transações
                por dia.
----------------------------------------
             Volte sempre!
========================================


Pressione qualquer tecla
```

4. Listar Clientes

```
========================================
              DioBank.com
----------------------------------------
            Listar Clientes
CPF         Nome
13613613613 Clientisvaldo Silva
----------------------------------------


Pressione qualquer tecla para voltar
```

5. Listar Contas

```
========================================
              DioBank.com
----------------------------------------
             Listar Contas
Agência C/C       Titular
   0001 000000001 Clientisvaldo Silva
----------------------------------------


Pressione qualquer tecla para voltar
```

## 📌 Melhorias Futuras

- [ ] Suporte para múltiplos usuários.
- [ ] Persistência de dados entre sessões.
- [ ] Interface gráfica.

## 📄 Licença

Este projeto é de código aberto e pode ser modificado conforme necessário.

---

✉️ Dúvidas ou sugestões? Entre em contato!
