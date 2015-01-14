#problem 9

def pythagorean():

	for a in range(0, 1000):
		for b in range(0, 1000):
			for c in range(0, 1000):
				if a+b+c==1000 and (a**2)+(b**2)==(c**2 )and c>b and b>a:
					return a, b, c
					break

def main():
	a, b, c =pythagorean()
	print "a={}, b={}, c={}".format(a, b, c)
	product=a*b*c
	print "product is:", product

if __name__ == '__main__':
	main()
