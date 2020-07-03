n=int(input("please enter a number to print the pattern "))
def pattern(n):
    for i in range(1, n):
        for j in range(1, i + 1):
            print(j, end= " ")
        print(" ")
pattern(n+1)
