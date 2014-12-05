
def multiples(n):
	sumt=0
	for i in range(1, n):
		if i%3==0 or i%5==0:
			sumt=sumt+i

	
	return sumt


print multiples(1000);
	
	