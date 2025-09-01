class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs : return ""
        elif not strs[0]: return ""
        mini = min([len(i) for i in strs])


        index = 0
        def check(index,mini):
            if index>=mini:
                return False
            temoin = strs[0][index]

            for mot in strs:
                if mot[index]!=temoin:
                    return False
            return True
        
        while check(index,mini):
            index += 1
        
        return strs[0][:index]


        
        
