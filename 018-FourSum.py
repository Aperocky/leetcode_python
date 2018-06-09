"""

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""

class Solution:

    # Why only restrict to 4 sum? EACH ADDITION WILL INCREASE COMPLEXITY BY *N.
    def nSum(self, nums, target, N, result, results):
        # print(result, N)
        if N < 2 or len(nums) < 2:
            return
        if N == 2:
            i, j = 0, len(nums) - 1
            while i < j:
                # print(i, j)
                if nums[i] + nums[j] == target:
                    results.append(result + [nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while nums[i] == nums[i-1]:
                        # print("i = %d, j = %d" % (i,j))
                        i += 1
                        if i >= j-1:
                            break
                    while nums[j] == nums[j+1]:
                        # print("i = %d, j = %d" % (i,j))
                        j -= 1
                        if j <= i+1:
                            break
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -= 1
        else:
            for i,v in enumerate(nums[:-N+1]):
                if target < v*N:
                    break
                if i == 0 or not nums[i] == nums[i-1]:
                    self.nSum(nums[i+1:], target - v, N-1, result + [v], results)


    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        # print(nums)
        results = []
        self.nSum(nums, target, 4, [], results)
        return results

    def test(self):
        nums = [0,1,5,0,1,5,5,-4]
        target = 11
        print(self.fourSum(nums, target))

soln = Solution()
soln.test()

""" METHOD OVERVIEW:

Using recursive to reduce everything to twoSum and then use twoSumself.

Theoretically we could also use dictionary look up. but since the list is sorted we use two pointers.

"""
