# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        num2 = 0

        while(l1):
            num1 *= 10
            num1 += l1.val
            l1 = l1.next

        while(l2):
            num2 *= 10
            num2 += l2.val
            l2 = l2.next
        
        num3 = num1 + num2
        num3 = str(num3)

        temp = ListNode(0)
        re = temp
        
        for i in num3:
            temp.next = ListNode(int(i))
            temp = temp.next

        return re.next