class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = {}
        for x,y in prerequisites:
            if x==y:
                return False
            if x in dic:
                dic[x].append(y)
            else:
                dic[x] = [y]

        res = True
        
        courses = {i for i in range(numCourses)}
        path = []

        def is_cycle(root):
            courses.remove(root)
            if root in dic:
                for x in dic[root]:
                    nonlocal res
                    if res:
                        if x in path:
                            res = False
                        if x not in seen:
                            seen.add(x)
                            path.append(root)
                            is_cycle(x)
                            path.pop()

        seen = set()
        while courses:
            course = next(iter(courses))
            seen.add(course)
            is_cycle(course)
            if not res:
                return res
        
        return res
