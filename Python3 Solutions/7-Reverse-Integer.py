#Link to problem https://leetcode.com/problems/reverse-integer/

class Solution:
    def __init__(self): #value in x can be edited to test other solutions
        x = 120 #must be of type int
        result = self.reverse(x) #must be of type int
        print('Answer: ', result)

    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
        arr_x = [z for z in str(x) if z != '-']  #removes dash character from arr_x
        rev_arr_x = arr_x[::-1] #flip array values' list order
        for x in range(len(rev_arr_x)):
            if len(rev_arr_x) > 1 and rev_arr_x[0] == '0':
                rev_arr_x.pop(0)
        if neg == True:
            rev_arr_x.insert(0, '-')
        reverse_x = ''.join(z for z in rev_arr_x)
        if int(reverse_x) > (pow(2, 31) - 1) or int(reverse_x) < pow(-2, 31):
            return 0
        else:
            return reverse_x

Solution()