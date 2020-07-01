s1= int(input ("please enter the score in first subject "))
s2= int(input ("please enter the score in second subject "))
s3= int(input ("please enter the score in third subject "))
s4= int(input ("please enter the score in fourth subject "))
s5= int(input ("please enter the score in the fifth subject "))
pers=s1+s2+s3+s4+s5/5
if ((s1 or s2 or s3 or s4 or s5)>100):
    print("enter a valid input")
    
elif (pers>=90):

    print ("the grade is A")

elif(70<=pers<90):
    print ("the grade is B")

elif(50<=pers<70):
    print ("the grade is C")

elif(30<=pers<50):
    print ("the grade is D")

else:
    print ("the grade is E") 
       