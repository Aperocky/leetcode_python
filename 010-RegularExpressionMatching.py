"""

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Note:

    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

"""

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # The dictionary object that all consults to.
        memory = {}
        # Function that make calls to the memory unit.
        def memoryCall(i, j):
            print(s[i:], p[j:])
            print(i, j)
            # Use recursive call to determine what (i, j) is.
            # If not (i,j) in memory dictionary, create one
            if not (i,j) in memory:
                # Check case: If i or j longer than s or p, this should return False
                if i > len(s) or j > len(p):
                    memory[i, j] = False
                # Establish base case, where i, j both arrived at the end of the s, p
                # Since we move from s, i should arrive there first.
                elif i == len(s):
                    # i and j both arrived at the end of s,p. This means a match existed.
                    # Edge case: i arrived at end of s, p still has 'a*' remaining.
                    if j < len(p)-1 and p[j+1] == '*':
                        memory[i,j] = memoryCall(i, j+2)
                    # Else, return whether p reached the end
                    else:
                        memory[i,j] = j == len(p)
                        print(p)
                else:
                    # Make sure j is within bound
                    if j == len(p):
                        return False
                    # Ascertain if the next character fits.
                    matched = s[i] == p[j] or p[j] == '.'
                    # Cases that the following character in pattern is a STAR.
                    if j < len(p) - 1 and p[j + 1] == '*':
                        # Since the following characters are a pattern, we could apply none, or more.
                        if matched:
                            # (i, j+2) for skipping current letter
                            # (i+1, j) for going to next letter
                            # This cover all cases because going to next and skipping is equivalent to i+1, j+1.
                            memory[i,j] = memoryCall(i, j+2) or memoryCall(i+1, j)
                        else:
                            # If it's not a match, we must go to next
                            memory[i,j] = memoryCall(i, j+2)
                    else:
                        # no such pattern.
                        if matched:
                            # Just go to next.
                            memory[i,j] = memoryCall(i+1, j+1)
                        else:
                            memory[i,j] = False
            return memory[i,j]

        return memoryCall(0,0)

    def test(self):
        s = ""
        p = "c*c*" 
        print(self.isMatch(s,p))

soln = Solution()
soln.test()