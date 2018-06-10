"""

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

    Only constant extra memory is allowed.
    You may not alter the values in the list's nodes, only nodes itself may be changed.

"""
import time

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    ## Following are added by Rocky to provide easy tests.
    @classmethod
    def fromstr(cls, input):
        input.replace(" ","")
        nums = input.split("->")
        out = cls(int(nums[0]))
        pointer = out
        for each in nums[1:]:
            each = int(each)
            if each > 9 or each < 0:
                print("ERROR in input")
                return
            pointer.next = cls(each)
            pointer = pointer.next
        return out

    def __str__(self):
        me = self
        mystr = []
        while True:
            mystr.append(str(me.val))
            if me.next is None:
                break
            me = me.next
            mystr.append("->")
        return "".join(mystr)

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Edge case
        if head == None:
            return head
        # Use recursion and new pointer to process k 
        res = ListNode(0)
        res.next = head
        head = res
        def reverseK(head, k):
            probe = head
            # Save the middle nodes reference in a list
            li = []
            # Send a probe to go to k length
            for _ in range(k):
                print("probe at %d" % probe.val)
                if probe.next:
                    probe = probe.next
                    li.append(probe)
                else:
                    return False
            # Get the next group if there is.
            if probe.next:
                probe = probe.next
            else:
                probe = False
            # If it gets here, it means length is enough
            li = li[::-1]
            head.next = li[0]
            for i in range(len(li)):
                print("Moving element %d" % li[i].val)
                if i > 0:
                    li[i-1].next = li[i]
            if probe:
                li[-1].next = probe
                return li[-1]
            else:
                li[-1].next = None
                return False
        while True:
            print("head at %d" % head.val)
            head = reverseK(head, k)
            if not head:
                break
        return res.next

    def test(self):
        node = ListNode.fromstr("1->2")
        print(self.reverseKGroup(node, 2))

soln = Solution()
soln.test()

# 71.78%

# COMPLETELY HOMEBREWED
