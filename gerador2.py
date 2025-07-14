import random

def gerador_letras():
    quantos = input('quantos numeros (so os numeros contado a sua palavra nao conta)?\n=> ')
    # repetir caso a variavel quantos não for int   
    while not quantos.isdigit():
        print('apenas numeros')
        quantos = input('quantos numeros (so os numeros contado a sua palavra nao conta)?\n=> ')

    quantos = int(quantos)
    # limitar a senha a um valor maximo de 100
    while quantos > 100:
        print('o maximo permitido é 100')
        while not quantos.isdigit():
            print('apenas numeros')
            quantos = input('quantos numeros (so os numeros contado a sua palavra nao conta)?\n=> ')
    
    palavra = input('fale uma palavra ou letras aleatorias que vc quer que apareça na senha \n=> ')
    
    s_n = input('vc quer embaralhar essas letras ou nao? (s) ou (n) \n=> ').lower().strip()
    while s_n not in ('s','n','sim','nao','não'):
        print('valor invalido')
        s_n = input('vc quer embaralhar essas letras ou nao? (s) ou (n) \n=> ').lower().strip()
    
    senha_f1 = '' #para o codigo fuciona, nao sei explicar :/
    
    if s_n in ['s','sim']:
         
        for _ in range(quantos):
            dig = str(random.randint(0, 9)) #tem que colocar as letras ainda
            senha_f1 += dig
    
        list_palavra = list(palavra)
        senha_f2 = list_palavra + list(senha_f1)   
        random.shuffle(senha_f2)
        
        senha_final = ''.join(senha_f2) #transformar a senha_f2 em string
        
    
    else:
        for _ in range(quantos):
            dig = str(random.randint(0, 9)) #tem que colocar as letras ainda
            senha_f1 += dig 
    
        palavra_lista = [palavra]
        senha_f2 = palavra_lista + list(senha_f1)
        random.shuffle(senha_f2)
    
        senha_final = ''.join(senha_f2)
    
    return(senha_final)
    
