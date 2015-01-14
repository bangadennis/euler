#problem 16.

from math import pow

def main(power):
	result=2**power
	result=str(result)
	data=list(result)
	sum1=0
	i=0
	while(i<len(data)):
		l=int(data[i])
		sum1=sum1+l
		i=i+1

	return sum1

if __name__ == '__main__':
	print main(1000)