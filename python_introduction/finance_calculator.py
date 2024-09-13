#User Input for Financial Details:
monthly_income = float ( input ("Enter your monthly income:" ))
monthly_expenses = float (input ( "Enter your total monthly expenses: " ))

#Calculate Monthly Savings:
monthly_savings = float ( monthly_income - monthly_expenses )

#Calulating projected savings:
projected_savings = (monthly_income - monthly_expenses ) * 12 +  (monthly_income- monthly_expenses)  * 12 * 0.05

#Output Results:
print (f"Your monthly savings is ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
