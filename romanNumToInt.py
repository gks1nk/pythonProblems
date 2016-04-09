def romanToInt1(s):
    """
    :type s: str
    :rtype: int
    """
    intTotal = 0
    for x in range(0, len(s)):
    	if s[x] == "I" or s[x] == "i":
    		if x + 1 >= len(s):
    			intTotal += 1
    		elif s[x+1] == "V" or s[x+1] == "v" or s[x+1] == "X" or s[x+1] == "x":
    			intTotal -= 1
    		else:
    			intTotal += 1
    	elif s[x] == "V" or s[x] == "v":
    		intTotal += 5
    	elif s[x] == "X" or s[x] == "x":
    		if x + 1 >= len(s):
    			intTotal += 10
    		elif s[x+1] == "L" or s[x+1] == "l" or s[x+1] == "C" or s[x+1] == "c":
    			intTotal -= 10
    		else:
    			intTotal += 10
    	elif s[x] == "L" or s[x] == "l":
    		intTotal += 50
    	elif s[x] == "C" or s[x] == "c":
    		if x + 1 >= len(s):
    			intTotal += 100
    		elif s[x+1] == "D" or s[x+1] == "d" or s[x+1] == "M" or s[x+1] == "m":
    			intTotal -= 100
    		else:
    			intTotal += 100
    	elif s[x] == "D" or s[x] == "d":
    		intTotal += 500
    	elif s[x] == "M" or s[x] == "m":
    		intTotal += 1000
    return intTotal

def romanToInt2(s):
	rValues = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
	rNum = s.upper()
	intTotal = 0
	for x in range(0, len(rNum)):
		if x + 1 == len(rNum):
			intTotal += rValues[rNum[x]]
		else:
			if rValues[rNum[x+1]] > rValues[rNum[x]]:
				intTotal -= rValues[rNum[x]]
			else:
				intTotal += rValues[rNum[x]]
	return intTotal
