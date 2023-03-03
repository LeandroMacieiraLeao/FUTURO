# crie um programa que leia dois valores e mostre um menu como o ao lado 
#com varias opcoes 

from time import sleep

n1 = int(input('primeiro valor:'))
n2 = int(input('segundo valor:'))
opcao = 0
while opcao != 6:

    print("""  [1] soma
    [2]multiplicar
    [3]maior
    [4]dividir
    [5]novos números
    [6]sair do programa""")

    opcao = int(input('>>>Qual é a sua opcao'))
    if opcao == 1:
        soma = n1+n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))

    elif opcao == 2:
        produto = n1*n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))

    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2 ,maior))
    
    elif opcao == 4:
        divisão = n1 / n2
        print('O resultado da divisão de {} / {} é {}'.format(n1, n2, divisão))
        
    elif opcao == 5:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input(' Segundo valor:'))

    elif opcao == 6:
        print('finalizando programa')
    else:
        print(' opcao invalida. Tente novamente')
        print('=-='*10)
        sleep(2)
        print("Fim do programa ! Volte sempre")
