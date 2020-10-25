#Link to problem https://leetcode.com/problems/remove-element/

class Solution:
    def __init__(self): #value in x can be edited to test other solutions
        nums = [0,1,2,2,3,0,4,2] #must be of type List[int]
        val = 2 #must be of type int
        result = self.removeElement(nums, val) #must be of type int
        print('Answer: ', result)

    def removeElement(self, nums: [int], val: int) -> int:
        for x in nums[:]:
            if x == val:
                nums.remove(val)
        return len(nums)

Solution()