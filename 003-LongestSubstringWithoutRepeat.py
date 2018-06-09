"""

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class Solution:

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dict = dict()
        start = 0
        maxlength = 0
        # Use Dictionary as in twosum and threesum.
        for i in range(len(s)):
            if s[i] in s_dict and start <= s_dict[s[i]]:
                start = s_dict[s[i]] + 1
            else:
                maxlength = max(maxlength, i - start + 1)
            s_dict[s[i]] = i
        return maxlength

    def test(self):
        str1 = "abcabcbb"
        str2 = "bbbbb"
        str3 = "pwwkew"
        print(self.lengthOfLongestSubstring(str1))
        print(self.lengthOfLongestSubstring(str2))
        print(self.lengthOfLongestSubstring(str3))

soln = Solution()
soln.test()
