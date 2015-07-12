import math

def isPrime(x):
	if (x == 2):
		return True
	elif (x % 2) == 0:
		return False
	counter = 3
	while counter <= math.sqrt(x):
		if x % counter == 0:
			return False
		counter += 2
	return True

def isPalindrone(x):
	number = str(x)
	if len(number) % 2 == 0: #even
		divAmount = len(number)//2
	else:
		divAmount = int(len(number)/2)
	for index in range(divAmount):
		if number[index] != number[-(index + 1)]:
			return False
	return True

def stringToArray(strIn, rows, columns):
	strIn = strIn.split(" ")
	finalArray = []
	for y in range(rows):
		rowArray = []
		for x in range(columns):
			currentItem = int(strIn[x + y * columns])
			rowArray.append(currentItem)
		finalArray.append(rowArray)
	return finalArray
