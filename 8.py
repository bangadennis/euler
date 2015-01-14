def main():
	f=open("1000.txt", "r")
	digits=[]
	
	while True:
		char=f.read(1)
		if not char: break
		base=ord('0')
		num=ord(char)-base
		if num>-1:
			digits.append(num)
			#print num
	f.close()
	suml=0
	i=0
	productlist=[]
	while(i<=len(digits)-13):
		product=1
		for n in range(0,13):
			product=product*digits[i+n]
		productlist.append(product)
		i+=1
	
	maxi=max(productlist)
	return maxi

if __name__ == '__main__':
	result=main()
	print "Product is, ", result


