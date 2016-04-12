'''
This problem wanted the length of a list returned, after all the duplicates had been removed
We were not supposed to create a new list, we needed to work with the one given
the solution, runs a comparison using the j variable, and moves dups to the end of the list
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        j = 0
        for i in range(0, len(nums)):
            if nums[i] != nums[j]:
                nums[i], nums[j+1] = nums[j+1], nums[i]
                j = j + 1
        return j+1
