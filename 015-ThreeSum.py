"""

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

class Solution:

    # Single pass hash table on inner side.
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        nums.sort()
        for i,v in enumerate(nums[2:]):
            hashtable = dict()
            for j in nums[:i+2]:
                if j not in hashtable:
                    hashtable[-j-v] = True
                else:
                    result.add((v, -j-v, j))
        return list(map(list, result))

    def test(self):
        nums = [-1, 0, 1, 2, -1, -4]
        print(self.threeSum(nums))

soln = Solution()
soln.test()

""" METHOD OVERVIEW

This is the 3sum version of TwoSum.

For each in the list, do a twosum on the forecoming elements (It is also possible to do it on coming elements)

"""
