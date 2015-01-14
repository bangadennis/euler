#sum
sum1=0
data=open("data13.txt", "r")
data1=data.readlines(50)
i=0
while(i<100):
	line=int(data1[i])
	print("Line {}--->{}").format(i, line)
	sum1=sum1+line
	i=i+1
	

print "The sum is: {}".format(sum1)

data.close()