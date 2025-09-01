class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists)>1:
            a,b = 0,1
            while b<len(lists):
                lists[a] = self.mergeTwoLists(lists[a],lists[b])
                lists.pop(b)
                a += 1
                b += 1
        return lists[0]
        

    def mergeTwoLists(self, list1, list2):
        res = None
        currentNode = None
        node1 = list1
        node2 = list2

        if not node1:
            return list2
        elif not node2:
            return list1

        while node1 and node2:
            if node1.val <= node2.val:
                if not res:
                    node = ListNode(node1.val)
                    res = node
                    currentNode = res
                    node1 = node1.next
                else:
                    node = ListNode(node1.val)
                    currentNode.next = node
                    currentNode = currentNode.next
                    node1 = node1.next
            else:
                if not res:
                    node = ListNode(node2.val)
                    res = node
                    currentNode = res
                    node2 = node2.next
                else:
                    node = ListNode(node2.val)
                    currentNode.next = node
                    currentNode = currentNode.next
                    node2 = node2.next


        while node1:
            node = ListNode(node1.val)
            currentNode.next = node
            currentNode = currentNode.next
            node1 = node1.next

        while node2:
            node = ListNode(node2.val)
            currentNode.next = node
            currentNode = currentNode.next
            node2 = node2.next
        
        return res
        
            
        
