"""

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        size = 1
        if x < 0:
            size = -1
            x = -x
        mystr = str(x)
        mystr = mystr[::-1]
        new = int(mystr)
        if new > 2**31 - 1:
            return 0
        elif new < -2**31:
            return 0
        else:
            return size * new

    def test(self):
        x = 2389375291
        print(self.reverse(x))

soln = Solution()
soln.test()
        
