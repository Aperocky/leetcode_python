"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

class Solution:

    # One pass solution
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = dict()
        for i in range(len(nums)):
            if not nums[i] in hashtable:
                hashtable[nums[i]] = i
            comp = target - nums[i]
            if comp in hashtable and not hashtable[comp] == i:
                return [hashtable[comp], i]

        raise Exception('no match found')

    def test(self):
        nums = [2, 7, 11, 15]
        target = 9
        print(self.twoSum(nums, target))

soln = Solution()
soln.test()

""" METHOD OVERVIEW

In this solution, the hashtable is presented as a O(1) check.

Single pass mean that the processing is on the same time as the creation of the hash table.

"""
