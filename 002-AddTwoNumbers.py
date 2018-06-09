"""

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    ## Following are added by me to add
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
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum, sig = self.addvals(l1.val, l2.val)
        result = ListNode(sum)
        pointer = result
        while True:
            prevsig = sig
            if l1.next is None and l2.next is None:
                if sig == 1:
                    pointer.next = ListNode(1)
                break
            elif l1.next is None:
                sum, sig = self.addvals(0, l2.next.val, prevsig)
                l2 = l2.next
            elif l2.next is None:
                sum, sig = self.addvals(0, l1.next.val, prevsig)
                l1 = l1.next
            else:
                sum, sig = self.addvals(l1.next.val, l2.next.val, prevsig)
                l1, l2 = l1.next, l2.next
            pointer.next = ListNode(sum)
            pointer = pointer.next
            prevsig = sig
        return result

    def addvals(self, num1, num2, prevsig=0):
        sum = num1 + num2 + prevsig
        if sum > 9:
            sng = sum%10
            return sng, 1
        return sum, 0

a = ListNode.fromstr("1->8")
b = ListNode.fromstr("0")
solution = Solution()
c = solution.addTwoNumbers(a, b)
print(c)
