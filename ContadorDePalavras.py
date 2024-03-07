loop = "n"
while loop == "n":
    print("Contador de palavras \n")

    word = input("Insira uma palavra/frase: \n >> ")
    leng = len(word)
    space = 0

    if word[-1] == " ":
        space -= 1
    elif word[-leng] == " ":
        space -= 1

    for i in range(leng):
        if word[i] == " ":
            space += 1
        i += 1

    print("\nPalavra/Frase: ",word)
    print("Qtd Palavras: ", space + 1)
    print("Qtd letras: ", leng - space)
    print("Qtd Caracteres: ", leng)

    loop = input("Sair? s/n\n>> ")
    print("\n")
