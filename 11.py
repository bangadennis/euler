#problem 11 20 by 20 matrix of data

def main():
	myFile=open("problem11.txt", "r")
	matrix=[[][]]
	for lineCount in range(1,21):
		line = myFile.readline()
		line=line.split(" ")
		count=0
		for char in line:
			if count<16:
				print int(char)
			count=count+const

			print "\n"
	 
if __name__ == '__main__':
	main()