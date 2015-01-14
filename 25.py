import sys
sys.setrecursionlimit(10000)

def fibonnaci(fb1, fb2, n):

	#print fb1,"\n"
	#print fb2,"\n"

	strfb1=str(fb1)
	lengthfb1=len(strfb1)

	if lengthfb1==1000:
		print lengthfb1
		print "Length is {}, Value is {}".format(n, fb1)
		return
	fibonnaci(fb2, fb1+fb2, n+1)
	
def main():
	fibonnaci(1, 1, 1)


if __name__ == '__main__':
	main()