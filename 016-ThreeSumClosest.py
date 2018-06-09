"""

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[-1]
        for i,v in enumerate(nums[2:]):
            j, k = 0, i+1
            while (j < k):
                # print(i, j, k)
                result = v + nums[j] + nums[k]
                if result == target:
                    return target
                if abs(result - target) < abs(res-target):
                    res = result
                if result < target:
                    j += 1
                if result > target:
                    k -= 1
        return res

    def test(self):
        nums = [-1, 2, 1, -4]
        target = 1
        print(self.threeSumClosest(nums, target))

soln = Solution()
soln.test()

""" METHOD OVERVIEW

This utilized ROLLING sorted for approximates.

with pins on each edge approaching we can find the closest approximate.

"""
