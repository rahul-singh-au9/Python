# Function to print all sub strings 
def subString(s, n): 
	for i in range(n): 
		for len in range(i+1,n+1): 
			print(s[i: len]) 

s = "abc" 
subString(s,len(s)) 
