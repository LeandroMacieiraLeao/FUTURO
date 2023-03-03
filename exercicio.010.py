# Maria precisa de um programa que calcule o perimetro do terreno
# para calcular o perimetro do terreno basta somar os quatros lados !

print('Bem vinda(o) vamos começar a medir o perimetro do seu terreno !')

print('''O perímetro é o comprimento do contorno de um polígono 
(figura plana e fechada), logo, 
para calcular o perímetro, 
basta somarmos a medida de todos os lados desse polígono.  ''')
print('vamos começcar:')

print('digite o seu nome')
nome=str(input( ))

print('digite o primeiro valor , valor igual a metro' )
l_n1=float( input( ))
print('digite o segundo valor')
l_n2=float(input( ))
print('digite o terceiro valor')
l_n3=float(input( ))
print('digite o quarto valor' )
l_n4=float(input( ))
opção=0
while opção != 2:

    P_ter=l_n1+l_n2+l_n3+l_n4
    print('O perimetro do terreno Sr ' ,nome, 'é' , P_ter )

    print('''Deseja calcular outro perimetro?
    [1]sim
    [2]não''')
    opção = int (input('>>>>>qual é sua opção?'))
    if opção ==1:
        print('digite o primeiro valor ' )
        l_n1=float(input( ))
        print('digite o segundo valor')
        l_n2=float(input( ))
        print('digite o terceiro valor')
        l_n3=float(input( ))
        print('digite o quarto valor' )
        l_n4=float(input( ))     
    elif opção == 2: 
        print('Obrigado por usar o nosso programa')   






