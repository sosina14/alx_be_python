def perform_operation(num1,num2, operation ):
 
    match operation:
        case "add":
            add = num1 + num2 
            print(f"Result: {add}")
    
        case "subtract":
            subtract = num1 - num2 
            print(f"Result: {subtract}")
    
        case "multiply":
            multiply = num1 * num2 
            print(f"Result: {multiply}")
        
        case "divide":
            divide = num1/num2
            if num2 != 0:
                print(f"Result: {divide}")
               
            else:
                print("")
    
    return (num1, num2, operation)
#perform_operation(num1, num2, operation)
