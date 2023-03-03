#fazer um programa que : EXERCICIO 6
# ler ototal da conta 
# acrescentar 20% da gorjeta 
# E taxa fixa do couver

print('Bem vindo ao bar do BOCA !')
print('''vamos começar :
saiba que aqui voçê paga uma pequena taxa de couver;
O couver é para ajudar com a contratação de nossos Artistas, ok''')

c_v= int(input('digite o valor R$' ))
print('valor do couver é R$' , c_v , 'ok')

#be_b= <bebidas>
be_b= int(input( 'digite o valor das brbidas R$'))
#print('Valor das bebidas é R$', be_b, 'ok')
#t_g= <tira gsto>
t_g=float(input( 'digite o valor do tira gost R$'))
#print('valor dos tira gosto é R$', t_g, 'ok')

#tot_p= <total parcial>
tot_p= be_b + t_g
print('A conta parcial são as bebidas e os tira gosto,' ) #.format (tot_p,t_g,tot_p))
print('valor parcial é R$' ,tot_p)

#gor_j<=> gorjeta 
gor_j=(be_b + t_g) *1/5
print( ' a gorjeta valoriza o nosso atendimento e é 20% da conta parcial') 
print('sua gorjeta é de R$', gor_j)
#C_total<=> conta total =  bebidas + tira gosto + couver + gorjeta
C_total= (be_b + t_g + c_v + gor_j )
print(" Sua conta total é R$" ,C_total)
print('Volte sempre e traga mais um ! ')





