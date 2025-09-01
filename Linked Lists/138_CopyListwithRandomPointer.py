class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        dic = {}
        currentNode = head

        while currentNode:
            dic[currentNode] = Node(currentNode.val)
            currentNode = currentNode.next

        for key,value in dic.items():
            if key.next:
                value.next = dic[key.next]
            if key.random:
                value.random = dic[key.random]

        return dic[head]


        
