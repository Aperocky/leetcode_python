"""

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        head = res
        while l1 or l2:
            if l1 and l2:
                if l1.val > l2.val:
                    head.next = l2
                    head = head.next
                    l2 = l2.next
                else:
                    head.next = l1
                    head = head.next
                    l1 = l1.next
            elif l1:
                head.next = l1
                break
            else:
                head.next = l2
                break
        return res.next

# 16.12%