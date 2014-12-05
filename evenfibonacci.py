

size=4000000
mylist=[1];
def fibonancciList(n, k):

	if k<=size:
		mylist.append(k)

		last=n+k
		fibonancciList(k, last)

	return mylist;


if __name__ == '__main__':
	list=fibonancciList(1, 2)
	sumt=0
	for i in list:
		if i%2==0:
			sumt=sumt+i

	print "\n",sumt




