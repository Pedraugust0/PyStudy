goBack = "n"
while(goBack == "n"):
    print("_--Python Calculator--_ \n \n")
    print("If you want to use decimal use . instead of , (ex: 50.5 instead of 50,5)")
    num1 = input("Put your first number: \n")
    operation = input("Put the operator: + - * / ^ \n")
    num2 = input("Put the second number: \n")

    def calculation(operation):
        match operation:
            case "+":
                return float(num1) + float(num2)
            case "-":
                return float(num1) - float(num2)
            case "*":
                return float(num1) * float(num2)
            case "/":
                return float(num1) / float(num2)
            case _:
                return "None"

    Result = calculation(operation)
    print ("\n Result of ", num1, operation, num2, "=", Result)
