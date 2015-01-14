#problem 48
def main():
	power=0
	suml=0
	for i in range (1, 1001):
		power=i**i
		suml=suml+power

	return suml

if __name__=='__main__':
	print "Sum is, ", main()
