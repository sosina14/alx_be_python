def perform_operation(num1 , num2 , operation ):
    
    if operation == "add" :
        return num1 + num2
    elif operation == "subtruct":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2 
    elif operation == "divide":
        if num2 == 0:
           return "Number can't be divide by zero" 
        return num1/num2
    else:
        return "Error input"  
