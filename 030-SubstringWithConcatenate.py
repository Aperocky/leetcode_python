"""

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:

Input:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
Output: []

"""

# Implement rolling windows of size words append together.

class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # Match windowed string against words
        def matchstring(subs, wod, minkey, maxkey):
            wd = dict(wod)
            cont = True
            start = minkey
            while len(wd) > 0:
                while True:
                    if start > maxkey:
                        return False
                    tryword = subs[:start]
                    if tryword in wd:
                        wd[tryword] -= 1
                        if wd[tryword] == 0:
                            wd.pop(tryword)
                        subs = subs[start:]
                        start = minkey
                        break
                    start += 1
            if subs == '':
                return True
            return False
        # Implement rolling windows
        # Total length
        tl = len(''.join(words))
        if len(s) < tl:
            return []
        if tl == 0:
            return []
        nums = []
        wd = {}
        # Turn words into a dictionary
        for word in words:
            if word in wd:
                wd[word] += 1
            else:
                wd[word] = 1
        maxkey = max([len(word) for word in wd.keys()])
        minkey = min([len(word) for word in wd.keys()])
        for i in range(len(s) - tl + 1):
            print(i)
            if matchstring(s[i:i+tl], wd, minkey, maxkey):
                # print("index %d" % i)
                nums.append(i)
        return nums

    def test(self):
        s = "barfoothefoobarman"
        words = ["foo","bar"]
        print(self.findSubstring(s, words))

soln = Solution()
soln.test()

# 50.17%

# Homebrewed!