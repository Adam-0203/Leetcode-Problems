# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        current_node = head
        while current_node and current_node.next:
            
            if current_node.next.val != current_node.val:
                current_node = current_node.next

            else:
                current_node.next = current_node.next.next


        return head


        
