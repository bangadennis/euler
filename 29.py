#problem 29

def main(n):
	result=[]
	for a in range(2, n):
		for b in range(2, n):
			power=a**b
			if power not in result:
				result.append(power)


	return len(result)


if __name__ == '__main__':
	print main(101)

