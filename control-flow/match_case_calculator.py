num1 = int(input ("Enter the first number: ")) 
num2 = int(input ("Enter the second number: "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

operation = input ("Choose the operation (+, -, *, /): ")
match operation:
    case "+" :
        print (f"The result [{add}].")
    case "-" :
        print (f"The result [{sub}].")
    case "*" :
        print (f"The result [{mul}].")
    case "/" :
        if num1 > num2 :
            print (f"The result [{div}].")
        elif num2 == 0:
            print ("Cannot divide by zero")
        else:
            print ("invalid input")

