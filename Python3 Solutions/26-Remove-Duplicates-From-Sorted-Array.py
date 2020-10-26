#Link to problem https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def __init__(self): #value in x can be edited to test other solutions
        nums = [0,0,1,1,1,2,2,3,3,4] #must be of type List[int]
        result = self.removeDuplicates(nums) #must be of type int
        print('Answer: ', result)

    def removeDuplicates(self, nums: [int]) -> int:
        if not nums:
            return 0
        p1 = 0 #p1 and p2 act as pointers for the indexes used during the sort
        print('Before modification: ', nums)
        for p2 in range(1, len(nums)):
            if nums[p1] != nums[p2]:
                p1 += 1
                nums[p1] = nums[p2]
        print('After modification: ', nums)
        return p1 + 1 #returns number of distinct elements

Solution()