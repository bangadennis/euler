#Problem Week 1-A Divisibility Test
#Author Dennis Banga

#function to find multiples and sum them up
def multipleSum(n):
	
	sumt=0
	for i in range(1, n):
		if i%7==0 or i%11==0:
			sumt=sumt+i
	
	return sumt



print multipleSum(10000);
	
	
