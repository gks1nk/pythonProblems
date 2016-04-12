'''
This problem gave a list of integers representing a number
the number 1245, would be a list = [1,2,4,5]
the question was to add 1 to the number, but keep the format in place
a 9 could not become a 10
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for x in range(len(digits)-1, -1, -1):
        	if x == 0 and digits[x] >= 9:
        		digits[x] = 0
        		digits.insert(0, 1)
        	else:
        		if digits[x] >= 9:
        			digits[x] = 0
        		else:
        			digits[x] += 1
        			break
        return digits
