
def primefactors(number):
	primelist=[]
	count=0
	for i in range(1, number):
		for x in range(1,i):
			if i%x==0 and x<i and x>1:
				count=-1
		if count!=-1:
			primelist.append(i)
			
	return primelist


if __name__ == '__main__':
	resultList=primefactors(44)
	for i in resultList:
		print "\n", i
	print max(resultList)
