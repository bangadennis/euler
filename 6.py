#problem 6

def sumofsquare(n):
	sumsq=0
	for num in range(1, n+1):
		sumsq=sumsq+(num**2)

	return sumsq

def squareofsum(n):
	suml=0
	for num in range(1, n+1):
		suml=suml+num

	squaresum=suml**2

	return squaresum

def main(n):
	diff=squareofsum(n)-sumofsquare(n)
	return diff

if __name__ == '__main__':
	print "The difference is, ", main(100)