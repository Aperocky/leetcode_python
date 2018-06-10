"""

Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

Note:

    Your algorithm should use only constant extra space.
    You may not modify the values in the list's nodes, only nodes itself may be changed.

"""

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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        res = ListNode(0)
        res.next = head
        head = res
        while(True):
            # 0->1->2->3 to 0->1->3 ; 2
            second = head.next.next
            head.next.next = head.next.next.next
            # 0->1->3 ; 2 to 0, 2->1->3
            second.next = head.next
            # 0, 2->1->3 to 0->2->1->3
            head.next = second
            # Move to next round
            head = head.next.next
            # Make sure there are two more.
            if head.next is None:
                break
            elif head.next.next is None:
                break
        return res.next

    def test(self):
        head = ListNode.fromstr("1->2->3->4")
        print(self.swapPairs(head))

soln = Solution()
soln.test()

# Beats 99.56%

# HOMEBREW SOLUTION!