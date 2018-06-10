"""

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = [x for x in lists if x]
        def merge(head, li):
            while li:
                mini = min(li, key = lambda x: x.val)
                li.remove(mini)
                head.next = mini
                head = head.next
                mini = mini.next
                if mini:
                    li.append(mini)
        res = ListNode(0)
        head = res
        merge(head, lists)
        return res.next

# 0% but it works.

        