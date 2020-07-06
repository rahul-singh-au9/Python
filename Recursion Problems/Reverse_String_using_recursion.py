# Python program to reverse a string using recursion 
def reverse(string): 
	if len(string) == 0: 
		return
	
	temp = string[0] 
	reverse(string[1:]) 
	print(temp, end='') 

string = "i am studying at attainu"
reverse(string) 