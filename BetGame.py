import random

dinheiro = 250.0
loop = 's'    

while loop == 's':
    print("Tigrin\n")

    print("Você tem: R$ ", dinheiro)
    aposta = float(input("Quanto você quer apostar?\n>> "))
    
    while aposta > dinheiro:
        print("Dinheiro insuficiente!!!")
        aposta = float(input("Quanto você quer apostar? \n>> "))
    
    vezes = int(input("Quantas vezes você quer jogar?\n>> "))
    while (aposta * vezes) > dinheiro:
        print("Dinheiro insuficiente!!!")
        vezes = int(input("Quantas vezes você querjogar? \n>> "))
    
    escolha = int(input("Qual cor você vai apostar? (1 = red, 2 = black, 3 = white)\n>> "))
    while escolha != 1 and escolha != 2 and escolha != 3:
        print("Insira um valor válido!!!")
        escolha = int(input("Qual cor você vai apostar? (1 = red, 2 = black, 3 = white)\n>> "))

    for i in range(vezes):
        dinheiro -= aposta
        roleta = random.choices(['red', 'black', 'white'], [48, 48, 4], k = 1)
        print(roleta)
        
        if 'white' in roleta:
            if escolha == 3:
                dinheiro += aposta * 128
        
        elif 'red' or 'black' in roleta:
            if escolha == 1 or escolha == 2:
                dinheiro += aposta * 2
    if dinheiro <= 0:
        print("Você torrou tudo '-' toma 250 kkkk \n")
        dinheiro = 250
