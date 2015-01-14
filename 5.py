#problem 5

def main(n):
	number=n
	count=0
	while(number>0):
		# if number%2!=0 or number%3!=0 or number%5!=0 or number%7!=0 or number%11!=0 or number%13!=0:
		# 	number=number+1
		for i in range(1, n+1):
			if number%i==0:
				count=count+1
				if count==n:
					return number
					break
			if count!=i:
				#print "---<<<<<<<%d ---%d" %(count, i)
				break
		#print "Number--->{}".format(number)
		count=0
		number=number+1

if __name__ == '__main__':
	print "The Value is: ",main(20)


