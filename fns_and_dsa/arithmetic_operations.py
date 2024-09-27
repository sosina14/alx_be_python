def perform_operation(num1,num2, operation ):
 
    match operation:
        case "add":
            add = num1 + num2 
            return add
    
        case "subtract":
            subtract = num1 - num2 
            return subtract
    
        case "multiply":
            multiply = num1 * num2 
            return multiply
        
        case "divide":
            if num2 == 0:
                return "Number can't divide by zero"
            else:
                divide = num1/num2
                return divide
    
   # return (num1, num2, operation)
#perform_operation(num1, num2, operation)
