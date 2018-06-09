"""

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.

"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        # Edge case no element
        if len(strs) == 0:
            return result
        shortest = min([len(s) for s in strs])
        i = 0
        while(i < shortest):
            chars = [s[i] for s in strs]
            # Fast way to check all element in list equals.
            if chars[1:] == chars[:-1]:
                result += chars[0]
                i += 1
            else:
                break
        return result

# 97.87%