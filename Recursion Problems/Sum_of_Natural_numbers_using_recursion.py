# find sum of natural numbers n using recursion 

def recurSum(n): 
	if n <= 1: 
		return n 
	return n + recurSum(n - 1) 

n = 5
print(recurSum(n)) 
