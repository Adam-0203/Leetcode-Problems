class Solution(object):
    def reverseList(self, head):
        
        node1 = None
        node2 = head

        while node2:
            node3 = node2.next
            node2.next = node1
            node1 = node2
            node2 = node3
        
        return node1
