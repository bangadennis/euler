import time 

def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

def primefactors(number):
	primefactors=[]
	primelist=sieve_for_primes_to(100000000)
	for n in primelist:
		#print "===>>>>>>>>", n
		if number%n==0:
			print "added<<<=======", n
			primefactors.append(n)

	return primefactors
				
	



if __name__ == '__main__':
	start_time=time.clock()
	start_tm=time.time()
	resultList=primefactors(600851475143)
	for i in resultList:
		print "\n", i
	end_time=time.clock()
	end_tm=time.time()
	if not resultList:
		print "AM Empty"
	else:
		print "Maximum Value of the primefactors is: "
		print max(resultList)
	print "\n<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>"
	print "Start Time is: %s" %(start_time)
	print "End Time is: %s" %(end_time)
	print "Difference in Time : %.5f" %(end_tm-start_tm)
