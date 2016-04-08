class Solution(object):
    def addDigits(self, num):
        """
        This is a simple function for returning the digital root of a positive integer.
        For example: num = 11, so the digital root would be 1 + 1 = 2
        For a larger integer, we combine the integers down until we have a single number (1 to 9)
        For example: num = 12345, so the digital root would be:
        1 + 2 + 3 + 4 + 5 = 15
        1 + 5 = 6
        6 is the digital root of 12345.
        I completed this problem for leetcode.com
        :type num: int
        :rtype: int
        """
        sumNum = sum([int(char) for char in str(num)])
        if sumNum <= 9:
        	return sumNum
        else:
        	return self.addDigits(sumNum)
