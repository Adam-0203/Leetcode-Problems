class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = {i:[] for i in range(1,n+1)}
        for source,target,time in times:
            graph[source].append((time,target))
        
        frontiere = [(0,k)]
        visited = set()

        while len(visited) != n and frontiere:
            time,node = heapq.heappop(frontiere)

            if node in visited:
                continue

            visited.add(node)

            for nei in graph[node]:
                if nei[1] not in visited:
                    heapq.heappush(frontiere,(time+nei[0],nei[1]))

        if len(visited)==n:
            return time
        return -1

        



