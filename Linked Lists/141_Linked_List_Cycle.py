# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        fast = head
        slow = head

        while fast: 
            if fast.next:
                fast = fast.next.next
            else:
                return False
            slow = slow.next

            if fast is slow:
                return True
        return False
