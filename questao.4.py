# programa de calculo de metros quadrados 
# metro quadrado =m² , largura x comprimento
# exercicio 3

from time import sleep

print('Bem vindo ! Vamos calcular a sua área quadrada ')

print("1° digite o nome do cliente")
nome=str(input( ))

print('digite o comprimento do terreno. digite ponto em vez de vírgula .')
comp=float(input( ))

print("digite a largura .")
laerg=float(input( ))

m_quad=comp*laerg
print(' O metro quadrado do cliente', nome,"é" ,m_quad ,'m²')

print('''Quer saber o valor do terreno ?
[ 1 ] Sim. 
[ 2 ] Não''')
      
opção = int(input('>>>>Qual sua Opção'))
if   opção ==1:
     print('Digite o valor do m²')
     vmq=float(input( ))

     vtmq=vmq*m_quad
     print('O valor do terreno é ',"R$", vtmq , )
     print('''deseja sair do programa ou calcular outros valores?
     [1] deseja calcular 
     [2] sair do programa ''')
     opção = int(input('>>>> informe os outros valores '))
     if opção ==1:
        print('digite o comprimento do terreno .')
        comp=float(input())
        print('digite a largura do terreno')
        larg=float(input())
        m_quad=comp*larg
        print('O m² sr,' , nome, "é de", m_quad ,)
        vtmq=vmq*m_quad
        print('O valor do terreno é ', "R$", vtmq, )
     elif opção ==2:
          print('obrigado por usar nossos serviços! volte sempre !')
          print('fimdo programa')

elif opção ==2:
     print('Obrigado por usar nossos serviços! Fim do Programa')

else :
        print('opção invalida. Tente novamente ok')
        print('=-='*10)
        sleep(2)
        print('Fim do Programa. Thank You')


