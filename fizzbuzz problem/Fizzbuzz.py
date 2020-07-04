if __name__ == "__main__":
    
    n=int(input("please input a num-"))
    for fizzbuzz in range(n+1):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("fizzbuzz")
            continue
        elif fizzbuzz % 3 == 0:
            print("fizz")
            continue
        elif fizzbuzz % 5 == 0:
            print("buzz")
            continue
        print(fizzbuzz)
	