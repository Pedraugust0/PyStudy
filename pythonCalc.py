goBack = "n"
while(goBack == "n"):
    print("_--Python Calculator--_ \n \n")
    num1 = input("Put your first number: \n")
    operation = input("Put the operator: + - * / ^ \n")
    num2 = input("Put the second number: \n")

    def calculation(operation):
        match operation:
            case "+":
                return int(num1) + int(num2)
            case "-":
                return int(num1) - int(num2)
            case "*":
                return int(num1) * int(num2)
            case "/":
                return int(num1) / int(num2)
            case "^":
                return pow(int(num1), int(num2))
            case _:
                return "None"

    Result = calculation(operation)
    print ("\n Result of ", num1, operation, num2, "=", Result)
    goBack = input("\n Do you wanna exit? y/n \n")
