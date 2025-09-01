class Solution:
    def mergeKLists(self,lists):
        lista = [[lists[i].val,i] for i in range(len(lists)) if lists[i]]
        heapq.heapify(lista)
        current = None
        res = None
        begin = 0
        index = 0
        value = 0

        def find():
            nonlocal index
            nonlocal value
            
            if len(lista):
                value,index = heapq.heappop(lista)
                return True
            return False

        while find():
            if not begin:
                current = ListNode(value)
                res = current
                begin = 1
            else:
                current.next = ListNode(value)
                current = current.next
            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(lista,[lists[index].val,index])


        return res
