class Solution(object):
    def canWinNim(self, n):
        """
        This function tests whether you can win a game of Nim based on being able to take 1, 2, or 3 stones
        per turn and you always go first. Assuming you play well, as long as the number of starting stones is
        not divisible by 4, then you can win the game. For example:
        n = 4
        No matter if you take 1, 2, or 3 stones, there will be 1 to 3 leftover, so your opponent will win.
        n = 7
        You can take 3 leaving 4, so no matter how many your opponent takes, you can win.
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0
