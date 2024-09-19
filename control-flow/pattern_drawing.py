number = int (input("Enter the size of the pattern: "))

for i in range(1, number):
  # Outer loop controls the number of rows
  for j in range(1, number):
    # Inner loop prints asterisks for each row
    print("*", end="")
  print("*")  # Move to a new line after each row of asterisks
