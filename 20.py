#problem 20, factorial and the sum of the digits of the factorial

#factorial function
def factorial(n):

	if n==0:
		return 1
	else:
		return n*factorial(n-1)

#Main Program
def main():
	suml=0
	fact_ans=factorial(100)
	fact=str(fact_ans)
	fact=list(fact)
	
	for digit in fact:
		digit=int(digit)
		suml+=digit

	print "The factorial, {} and sum, {}".format(fact_ans, suml)


if __name__ == '__main__':
	main()

