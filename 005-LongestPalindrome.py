"""

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"

"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Maximum in dynamic method
        maxlen = 0
        maxstr = ''
        # For each letter and in betweens in the string, expand around, going through the series.
        for i in range(len(s)):
            # Do two things, start from within the letter, or the in between after it.
            j = 0
            # First loop, get the palindrome around each letter.
            while True:
                if i-j == -1 or i+j == len(s):
                    break
                if s[i-j] == s[i+j]:
                    if 2*j + 1 > maxlen:
                        maxlen = 2*j + 1
                        maxstr = s[i-j:i+j+1]
                    j += 1
                else:
                    break
            # Second loop, get the palindrome around in betweens after the letter
            k = 0
            while True:
                if i-k == -1 or i+k+1 == len(s):
                    break
                if s[i-k] == s[i+k+1]:
                    if 2*k + 2 > maxlen:
                        maxlen = 2*k + 2
                        maxstr = s[i-k:i+k+2]
                    k += 1
                else:
                    break
        return maxstr

    def test(self):
        input = "cbbd"
        print(self.longestPalindrome(input))

soln = Solution()
soln.test()