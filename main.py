import gerador1
import gerador2

print('bem vindo ao gerador de senhas')
print('1 - gerar apenas numeros \n2 - gerar com letras \n3 ')

funcao = (input('escolha qual vai ser oque vc quer\n=> '))
#ver se é um numero
while not funcao.isdigit():
    print('apenas numeros amigo')
    funcao = (input('escolha qual vai ser oque vc quer\n=> '))

#gerar apenas numeros
if funcao == 1:
    print(gerador1.gerador()) #coloquei assim caso futuro decido salvar ou qulquer coisa com essa senha criada

#gerar numeros e caracteres escolhidos por usuarios
elif funcao == 2:
    print(gerador2.gerador_letras())