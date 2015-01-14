#Collatz function
list=[]
def collatz(num):
	global list
	list.append(num)
	if num==1:
		return len(list)

	#Even

	if num%2==0:
		return collatz(num/2)
	else:
		return collatz(3*num+1)

def main(size):
	dictd={}
	count=1
	print collatz(13)
	terms=0
	for count in range(1, size):
		global list
		list=[]
		dictd[count]=collatz(count)

	maxiterms=max(dictd.values())

	for key, value in dictd.items():
		#print key, value
		if value == maxiterms:
			print "This Number, {} has the Maxiterms ,{}".format(key,value)

if __name__ == '__main__':
	main(1000000)





