"""

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

"""

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Use O(N) dynamic method.
        # Utilize Steps.

        # Edge case
        if numRows > len(s) or numRows == 1:
            return s
        # Initiate empty lists 
        l = [''] * numRows
        index, step = 0, 1
        # Append to strings in list
        for letter in s:
            l[index] += letter
            if index == numRows - 1:
                step = -1
            elif index == 0:
                step = 1
            index += step
        return ''.join(l)

    def test(self):
        s = "PAYPALISHIRING"
        numRows = 3
        print(self.convert(s, numRows))

soln = Solution()
soln.test()
            

