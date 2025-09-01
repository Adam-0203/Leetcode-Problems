class Solution(object):
    def groupAnagrams(self, strs):
        if len(strs)==1:
            return [[strs[0]]]
        
        def hash_map(stringos):
            res = {}
            for x in stringos:
                if x in res:
                    res[x] += 1
                else:
                    res[x] = 1
            return frozenset(res.items())
        
        res = {hash_map(strs[0]):[strs[0]]}
        
        for i in range(1,len(strs)):
            hashing = hash_map(strs[i])
            if hashing in res:
                res[hashing].append(strs[i])
            else:
                res[hashing] = [strs[i]]

        return res.values()


        
