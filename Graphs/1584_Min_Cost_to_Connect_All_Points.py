class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0

        def distance(A,B):
            xA,yA = A[0],A[1]
            xB,yB = B[0],B[1]

            val = abs(xA-xB)+ abs(yA-yB)
            return val

        graph = []

        for _ in range(len(points)):
            graph.append([])
        
        for i in range(len(points)):
            graph[i].append(0)
            for j in range(i+1,len(points)):
                manhattan = distance(points[i],points[j])
                graph[i].append(manhattan)
                graph[j].append(manhattan)
        
        visited = set()
        frontiere = [(0,0)]
        heapq.heapify(frontiere)

        while len(visited) != len(points):
            val = heapq.heappop(frontiere)
            while val[1] in visited:
                val = heapq.heappop(frontiere)
            
            visited.add(val[1])
            res += val[0]

            for i in range(len(points)):
                if i not in visited:
                    heapq.heappush(frontiere,(graph[val[1]][i],i))

        return res
