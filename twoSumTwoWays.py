'''
This is from an easy problem on leetcode.com.
I solved the problem the first way, but my processing time was slow.
After looking at the hashing solution written in java, I was able to write
my own version in python, that is twoSum2
'''

def twoSum1(self, nums, target):
  """
  :type nums: List[int]
  :type target: int
  :rtype: List[int]
  """
  for x in range(0, len(nums)):
    for y in range(x+1, len(nums)):
      if nums[x] + nums[y] == target:
        return [x, y]
        			
def twoSum2(self, nums, target):
  """
  :type nums: List[int]
  :type target: int
  :rtype: List[int]
  """
  #trying hash table way
  hshTble = {}
  for x in range(0, len(nums)):
    chkHash = target - nums[x]
    if chkHash in hshTble:
      return [hshTble[chkHash], x]
    hshTble[nums[x]] = x
