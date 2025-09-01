class Solution(object):
    def groupAnagrams(self, strs):
        if len(strs)==1:
            return [[strs[0]]]
        
        def hash_map(stringos):
            res = [0]*26
            for x in stringos:
                res[ord(x)-ord('a')]+=1
            return tuple(res)
        
        res = {hash_map(strs[0]):[strs[0]]}
        
        for i in range(1,len(strs)):
            hashing = hash_map(strs[i])
            if hashing in res:
                res[hashing].append(strs[i])
            else:
                res[hashing] = [strs[i]]

        return res.values()


        
