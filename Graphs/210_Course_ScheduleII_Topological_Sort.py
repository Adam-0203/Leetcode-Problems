class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        deja = set()
        res = []
        not_needed = {i for i in range(numCourses)}
        preMap = {i:[]  for i in range(numCourses)}
        for x,y in prerequisites:
            preMap[x].append(y)
            if y in not_needed:
                not_needed.remove(y)

        def dfs(root):
            if not preMap[root]:
                if root not in deja:
                    res.append(root)
                    deja.add(root)
                return True


            for nei in preMap[root]:
                if nei in visited:
                    return False

                visited.add(nei)
                if not dfs(nei):
                    return False
                visited.remove(nei)

            res.append(root)
            deja.add(root)
            preMap[root] = []
            return True


        for i in not_needed:
            visited = {i}
            if not dfs(i):
                return []

        if len(res)==numCourses:
            return res
        return []
