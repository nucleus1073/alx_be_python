length=int(input("Enter the size of the pattern: "))
count=length
while (count!=0):
    for j in range(0, length):
        for i in range (0,length):
            print("*", end="")
        count=count-1
        print ("\n")