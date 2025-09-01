class Solution(object):
    def removeNthFromEnd(self, head, n):
        late = None
        onTime = head
        counter = -1

        while onTime:
            onTime = onTime.next
            counter += 1

            if counter == n:
                late = head
            elif counter > n:
                late = late.next
            

        if not late:
            head = head.next
            return head
        
        late.next = late.next.next
        return head
