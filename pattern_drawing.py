size = int(input("Enter the size of the pattern:"))
rows = 0
while rows<size:
    line = 0
    while line <size:
        print("*",end="")
        line +=1
    print()
    rows+=1
