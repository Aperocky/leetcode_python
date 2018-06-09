"""

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""

"""

LOGIC:

Since the two are sorted, we use binary search.

"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        k = len(nums1) + len(nums2)
        if k%2 == 1:
            return self.findKth(nums1, nums2, k//2)
        else:
            return (self.findKth(nums1, nums2, k//2) + self.findKth(nums1, nums2, k//2-1)) / 2


    # Finding the kth ranged number among two lists
    def findKth(self, A, B, k):
        if len(A) > len(B):
            A, B = B, A
        print(A, B, k)
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])
        i = len(A)//2
        j = k - i
        if A[i] > B[j]:
            return self.findKth(A[:i], B[j:], i)
        else:
            return self.findKth(A[i:], B[:j], j)

    def test(self):
        nums1 = [1, 3]
        nums2 = [2]
        print(self.findMedianSortedArrays(nums1, nums2))

soln = Solution()
soln.test()

""" METHOD OVERVIEW:

THIS USE RECURSION ON BINARY SEARCH TO PIN POINT THE EXACT ELEMENT.

"""
