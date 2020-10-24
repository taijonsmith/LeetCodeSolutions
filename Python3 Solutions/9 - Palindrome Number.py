#Link to problem https://leetcode.com/problems/palindrome-number/

class Solution:
    def __init__(self): #value in x can be edited to test other solutions
        x = -121 #must be of type int
        result = self.isPalindrome(x) #must be of type bool
        print('Answer: ', result)

    def isPalindrome(self, x: int) -> bool:
        if not isinstance(x, int) or x < 0:
            return False
        d_stripped = [d for d in str(x)]
        d_flipped = d_stripped[::-1]
        if (d_flipped == d_stripped):
            return True
        else:
            return False
        
Solution()