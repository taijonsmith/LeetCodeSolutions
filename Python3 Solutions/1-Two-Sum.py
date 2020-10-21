#Link to problem https://leetcode.com/problems/two-sum/
import itertools


class Solution:
    def __init__(self): #values in these variables can be edited to test other solutions
        nums = [2, 7, 11, 15] #must be of type List[int]
        target = 9 #must be of type int
        result = self.twoSum(nums, target) #must be of type List[int]
        print('Answer: ', result)

    def twoSum(self, nums: [int], target: int) -> [int]:
        result = []
        found = False
        for i1, i2 in itertools.combinations(nums, 2):
            if not found:
                item_1 = 0
                item_2 = 0
                if i1 + i2 == target:
                    found = True
                    if i1 == i2:
                        result = [i for i, e in enumerate(nums) if e == i1]
                    else:
                        item_1 = nums.index(i1)
                        item_2 = nums.index(i2)
                        result = [item_1, item_2]
                    break
        return(result)

Solution()