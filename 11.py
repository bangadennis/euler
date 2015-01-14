#problem 11 20 by 20 matrix of data

def main():
	myFile=open("problem11.txt", "r")

	for lineCount in range(1,21):
		line = myFile.readline()
		line=line.split(" ")
		count=0
		if lineCount in [1,4,8, 12,16,20]
			const=1
		if lineCount in [2,5,9,13,17]
			const=2
		if lineCount in [3,6,10,14,18]
			const=2
		if lineCount in [4,8,13,19]
			start=2
		for char in line:
			if count<16:
				print int(char)
			count=count+const

			print "\n"
	 
if __name__ == '__main__':
	main()