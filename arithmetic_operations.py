def perform_operation(num1:float,num2:float,operation:str):
    if operation == "add":
        print (num1+num2)
    elif operation == "subtract":
        print(num1-num2)
    elif operation == "multiply":
        print (num1*num2)
    elif operation == "divide":
        if num2 == 0:
            return "cannot divide by 0"
        return (num1/num2)
    else:
        return "invalid operation"

perform_operation(22,0,"divide")

