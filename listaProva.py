person_name = ["Rogerin", "Pedro", "Rolando", "Fernanda"]
person_score = [46, 34, 22, 47]
person_age = [19, 18, 22, 19]
is_male = [True, True, True, False]
is_strong = [False, True, True, False]
var_list = 0 #Função q lista cada pessoa e suas características
negado = "Reprovado! Abaixo da pontuação média" #Criei a var so para testar a func upper

while(var_list <= 4):   #Loop para executar a lista 4 vezes
    print("---------------------------\n")
    print("Nome:", person_name[var_list])
    print("Pontuação:", person_score[var_list])
    print("Idade:", person_age[var_list])
    print("Homem? :", is_male[var_list])
    print("É forte? :", is_strong[var_list])
    
    if person_score[var_list] < 25:     #Checar se a nota é abaixo da média
        print(negado.upper()) #Teste de função de deixar as letras em maiúsculo
    var_list = var_list + 1
    print(" ") #Dar um espaço em cada lista para ficar bonito
