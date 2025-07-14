import random
def gerador():
    quantidade = input('quantos caracteres?\n=> ')
    #garantir que o usuario coloque o valor esperado
    while not quantidade.isdigit():
        print('apenas numeros')
        quantidade = input('quantos caracteres?\n=> ')

    quantidade = int(quantidade)
    #limitar a senha ate 100
    while quantidade > 100:
        print('o maximo permitido é 100')

        while not quantidade.isdigit():
            print('apenas numeros')
            quantidade = input('quantos caracteres?\n=> ')
        quantidade = int(quantidade)

    senha = ''
 
    for _ in range(quantidade):
        dig = str(random.randint(0, 9))
        senha += dig

    return(senha)
