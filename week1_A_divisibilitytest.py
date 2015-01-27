#SciCodeJam Problem
#Problem Week 1-A Divisibility Test
#Author Dennis Carnegie B

#function to find multiples of 7 and 11, 
#and summing them up
def multipleSum(size):
	sumt=0
	for i in range(1, size):
		if i%7==0 or i%11==0:
			sumt=sumt+i
	
	return sumt

#Main Function
def main():
	print multipleSum(10000);


if __name__ == '__main__':
	main()


	
	
