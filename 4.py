def reverse(test):
    n = len(test)
    x=""
    for i in range(n-1,-1,-1):
        x += test[i]
    return int(x)

def palindrome():
	list=[]
 	for n in range(999, 100, -1):
 		for i in range(999, 100, -1):
 			product=n*i
 			rev_product=reverse(str(product))
 			if product==rev_product:
 				print "{} * {}".format(n, i)
 				print "Largest is, ", product
 				list.append(product)

 	return list

 				

def main():
	result=palindrome()
	maxi=max(result)
	print "Largest palindrome", maxi

if __name__ == '__main__':
	main()


