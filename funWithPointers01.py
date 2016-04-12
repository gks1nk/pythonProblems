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

'''
Another fun with pointers problem,
this one simply removes a single value from the list
'''
def removeElement(A, elem):
        j = len(A)-1
        for i in range(len(A) - 1, -1, -1):
            if A[i] == elem:
                A[i], A[j] = A[j], A[i]
                j -= 1
        return j+1
