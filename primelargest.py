
def primefactors(number):
	primelist=[]
	primefactors=[]
	n=1
	while(n<=number):
		print "===>>>>>>>>", n
		if number%n==0:
			print "added<<<=======", n
			primelist.append(n)
		n=n+1

	
	for num in primelist:
		count=0
		print "===>",num
		for i in range(1, num):
			print "<===",num
			if num%i==0 and i<num and i>1:
				count=-1
				break;
		if count==0:
			primefactors.append(num)

	return primefactors
				
	



if __name__ == '__main__':
	resultList=primefactors(600851475143)
	for i in resultList:
		print "\n", i
	if not resultList:
		print "AM Empty"
	else:
		print "Maximum Value of the primefactors is: "
		print max(resultList)
