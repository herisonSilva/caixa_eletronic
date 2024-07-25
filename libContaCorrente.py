from datetime import datetime
extratoCC = []  # Armazena as transações realizadas na conta corrente
saldocc = 0  # armazena o valor do saldo.


# 4 funções a serem feitas (depósito, saque, extrato, saldo.)
def deposito(valor_dep):  # armazena e realiza a transação de depósito e atualiza.
    global saldocc
    extratoCC.append(f'{datetime.now().strftime("%d/%m/%y %H:%M:%S")} Depósito efetuado: R$ {valor_dep:.2f}')
    saldocc = saldocc + valor_dep  # atualiza o valor do saldo.
    return print(f'Depósito de: R$ {valor_dep:.2f} efetuado com sucesso.')


def saque(valor_saq):  # armazena e realiza a transação de saque e atualiza o saldo.
    global saldocc
    if valor_saq > saldocc:
        return print('Saldo insulficiente.')
    else:
        extratoCC.append(f'{datetime.now().strftime("%d/%m/%y %H:%M:%S")} Saque efetuado: R$ {valor_saq:.2f}')
        saldocc = saldocc - valor_saq  # atualiza o valor do saldo.
        return print(f'Saque de: R$ {valor_saq:.2f} efetuado com sucesso.')


def extrato():  # exibe todas as transações realizadas na conta.
    for transacao in extratoCC:
        print(transacao)
    return print(f'saldo disponível: R$ {saldocc:.2f}')


def saldo():  # exibe o saldo atualizado.
    return print(f'Seu saldo atual é: R$ {saldocc:.2f}')


def menu():  # Menu 'gestão de conta corrente' como solicitado no exemplo.
    print('\n*GESTÃO DE CONTA CORRENTE*')
    print('*' * 26)
    print('** 1) Depósito na Conta **')
    print('** 2) Saque da Conta    **')
    print('** 3) Extrato da Conta  **')
    print('** 4) Saldo da Conta    **')
    print('** 5) Sair              **')
    print('*' * 26)
