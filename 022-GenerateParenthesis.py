"""

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def recv(res, stri, n, i):
            # Base case:
            if n == i:
                stri = stri + [")"] * (2*n - len(stri))
                res.append(''.join(stri))
            else:
                if i > len(stri)/2:
                    recv(res, stri + [")"], n, i)
                recv(res, stri + ["("], n, i+1)
        result = []
        recv(result, [], n, 0)
        return result

    def test(self):
        n = 3
        print(self.generateParenthesis(n))

soln = Solution()
soln.test()

# 97.85%

# COMPLETELY HOMEBREWED!