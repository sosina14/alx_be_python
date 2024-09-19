num = int (input("Enter the size of the pattern: "))
i=0
while i < num:
    j= 0
    for j in range(1, num):
        print("*", end="")
        j+=1
    print("*")
    i+=1
