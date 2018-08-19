
def countLeft(x):
	if x == '(':
		global leftCount
		leftCount += 1
	return leftCount

def countRight(x):
	if x == ')':
		global rightCount
		rightCount +=1
	return rightCount

def compareTuple(x):
	if x[0] ==x[1]:
		return True
	else: 
		return False

def findKInArrayS(s):
	leftArray = list(map(lambda x: countLeft(x), s))
	rightArray = list(map(lambda x: countRight(x), s[::-1])) 
	rightArray.reverse()
	comparsionArray = list(zip(leftArray, rightArray))
	resultArray = list(map(lambda x: compareTuple(x), comparsionArray))
	# check edge cases
	if True in resultArray:
		return resultArray.index(True)
	else:
		return int(len(resultArray)/2)


s = '(())))('
s1 = ')())('
s2 = ')('
s3 = '))('
leftCount = 0
rightCount = 0

print(findKInArrayS(s3))

