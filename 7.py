#problem 7

def sumprimenumber():
	result=[2]
	suml=0
	number=3
	n=0
	while(number<=600851475143):
		for i in range(2, number):
			count=0
			if i>20 and (number%3==0 or number%5==0 or number%7==0 or number%11==0 or number%13==0 or number%17==0 or number%19==0):
				count=-1
				break
			if number%i==0 and i<20:
				count=-1
				break
		if count!=-1:
			result.append(number)
			#if len(result)==10001:
				#return result[10000]
			print("Number---->>>>{}").format(number)	
		number+=2
	i=0
	for n in result:
		# if i<len(result)-1:
		# 	diff=result[i+1]-result[i]
		# else:
		# 	diff=0
		#print "Prime---->>>>{} and--->{}".format(n,diff)
		suml=suml+n
		i=i+1

	#print "Maximum Diff=={} and Minimum Diff=={}".format(max(diff), min(diff))
	return suml

def main():
	result=sumprimenumber()
	print "The sum of primeNumbers is, {}".format(result)

if __name__ == '__main__':
	main()