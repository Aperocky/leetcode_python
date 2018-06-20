"""

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

"""

# Use a stack
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # This creates a stack with all the index that are NOT a valid parenthesis.
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append((i, True))
            else:
                if not stack:
                    stack.append((i, False))
                if stack[-1][1]:
                    stack.pop()
                else:
                    stack.append((i, False))
        stack = [s[0] for s in stack]
        lenstack = len(stack)
        stack.append(len(s))
        maxstack = stack[0]
        for i in range(lenstack):
            maxstack = stack[i+1] - stack[i] - 1 if maxstack < stack[i+1] - stack[i] - 1 else maxstack
        return maxstack

    def test(self):
        inp =  ""
        print(self.longestValidParentheses(inp))

soln = Solution()
soln.test()

# 80.67 %

