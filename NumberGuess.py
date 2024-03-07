import random

tabela = [0,1,2,3,4,5,6,7,8,9,10]
num_ran = random.randint(0,10)
num_check = 0

while 1:
    print("Escolha um número de 0 a 10")
    print(tabela)
    num_guess = int(input(">> "))
    
    if num_guess < num_ran: #Caso o número adivinhado seja menor que o número random
        while num_guess > -1:
            tabela[num_guess] = '>'
            num_guess -= 1
            num_check += 1
        
    elif num_guess > num_ran: #Caso o número adivinhado seja maior que o número random
        while num_guess < 11:
            tabela[num_guess] = '<'
            num_guess += 1
            num_check += 1
    
    elif num_guess == num_ran: #Caso você acerte o número
        print("Você ganhou!!!")
        num_resto = 11 + (num_check * 2)
        pontos = 111 - num_resto
        print("Pontuação: ", pontos ," Pontos\n")
        input("Aperte enter para sair")
        break
