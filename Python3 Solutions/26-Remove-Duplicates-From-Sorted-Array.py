#Link to problem https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def __init__(self): #value in x can be edited to test other solutions
        nums = [1,1,2] #must be of type List[int]
        result = self.removeDuplicates(nums) #must be of type int
        print('Answer: ', result)

    def removeDuplicates(self, nums: [int]) -> int:
        print(nums)
        for index, n in enumerate(nums):
            print(index)
            if (index < len(nums) - 1 and n == nums[index + 1]):
                nums.remove(n)
        print(nums)
        return len(nums)

Solution()