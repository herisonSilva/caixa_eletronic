from libContaCorrente import *
codigo = 9999
while codigo != 5:
    try:
        menu()
        codigo = int(input('Digite o número de uma das opções acima: '))
        if codigo == 1:
            valor = eval(input('Digite o valor a ser depositado. R$: '))
            deposito(valor)

        elif codigo == 2:
            valor = eval(input('Digite o valor do saque. R$: '))
            saque(valor)

        elif codigo == 3:
            extrato()

        elif codigo == 4:
            saldo()

        elif codigo == 5:
            print('Fim do programa!')

        else:
            print('Código inválido!')

    except ValueError:
        print('Letras e números reais não são permitidos. Digite um número referente ao código do menu.')
    except KeyboardInterrupt:
        print('Operação cancelada!')
        codigo = 5
print('volte sempre!'.upper())
