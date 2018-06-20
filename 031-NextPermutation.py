"""

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Edge case
        if len(nums) < 2:
            return False
        index = 1
        while index < len(nums):
            if nums[-index] > nums[-index-1]:
                break
            index += 1

        print(index)
        # This time, index = the place when list last increases:
        # 1, 3, 2, 4 -> index = 1
        # 1, 3, 4, 2 -> index = 2
        # Our goal is to put the number in front of that after the suitable place.
        # Edge case
        if index == len(nums):
            nums[:] = nums[::-1]
            return
        # Put the previous element after the next
        # 1, 3, 2, 4 -> 1, 3, 4, 2
        # 1, 3, 4, 2 -> 1, 4, 3, 2 (middle state)
        mover = index + 1
        moved = nums[-mover]
        while index > 0:
            if nums[-index] <= moved:
                break
            index -= 1
        print(nums)
        # Index can be 0
        print(mover)
        nums[-index-1], nums[-mover] = nums[-mover], nums[-index - 1]
        print(nums)
        # Reverse the last elements (mover - 1) elements
        nums[-mover+1:] = list(reversed(nums[-mover+1:]))

    def test(self):
        nums = [5,1,1]
        self.nextPermutation(nums)
        print(nums)

soln = Solution()
soln.test()

# 98.28%
# Homebrewed!
