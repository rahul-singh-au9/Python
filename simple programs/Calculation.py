calculation=int(input("please input 1 for addition, please input 2 for subtraction, please input 3 for multiplication, please input 4 for division "))
if(calculation ==1):


    print("please enter two numbers to add")

    num1=int(input("please enter first num "))
    num2=int(input("please enter second num "))

    print("output= ", num1+num2)

elif(calculation==2):
    
    print("please enter two numbers to subtract")

    num1=int(input("please enter first num "))
    num2=int(input("please enter second num "))

    print("output=", num1-num2)

elif(calculation==3):
    print("please enter two numbers to multiply")

    num1=int(input("please enter first num"))
    num2=int(input("please enter second num"))

    print("output=", num1*num2)

elif(calculation==4):
    print("please enter two number to divide")

    num1=int(input("please enter first num"))
    num2=int(input("please enter second num"))

    print("output=", num1/num2)

else:
    print("please enter a valid number")

    




