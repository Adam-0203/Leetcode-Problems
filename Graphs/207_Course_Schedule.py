class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[]  for i in range(numCourses)}
        for x,y in prerequisites:
            preMap[x].append(y)

        def dfs(root):
            if not preMap[root]:
                return True


            for nei in preMap[root]:
                if nei in visited:
                    return False

                visited.add(nei)
                if not dfs(nei):
                    return False
                visited.remove(nei)

            preMap[root] = []
            return True


        for i in range(numCourses):
            visited = {i}
            if not dfs(i):
                return False
        return True
