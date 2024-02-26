goBack = "n"
while(goBack == "n"):

    print("Choose which option you want to use: \n 1) Calculator \n 2) multiplication table \n 3) exit")
    usr_choose = input(">> ")
    if usr_choose == "1":
        print("_--Python Calculator--_ \n \n")
        print("If you want to use decimal use . instead of , (ex: 50.5 instead of 50,5)")
        calc_num1 = input("Put your first number: \n")
        operation = input("Put the operator: + - * / ^ \n")
        calc_num2 = input("Put the second number: \n")
        def calculation(operation):
            match operation:
                case "+":
                    return float(calc_num1) + float(calc_num2)
                case "-":
                    return float(calc_num1) - float(calc_num2)
                case "*":
                    return float(calc_num1) * float(calc_num2)
                case "/":
                    return float(calc_num1) / float(calc_num2)
                case "^":
                    return pow(float(calc_num1), float(calc_num2))
                case _:
                    return "None"
        Result = calculation(operation)
        print ("\n Result of ", calc_num1, operation, calc_num2, "=", Result)

    elif usr_choose == "2":
            multiplier = 1
            print("_--Multiplication Table--_ \n")
            print("Which number table you want to use?")
            table_num1 = input(">> ")
            print("\n How many times you want to multiply it?")
            table_loop = input(">> ")
            for x in range(int(table_loop)):
                print(table_num1 ,"*" ,multiplier ,"=" ,int(table_num1) * multiplier)
                multiplier += 1
        elif usr_choose == "3":
            goBack = input("Do you wanna exit? y/n \n >> ")
