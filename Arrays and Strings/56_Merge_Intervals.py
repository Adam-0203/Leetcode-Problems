class Solution(object):
    def merge(self, intervals):
        if len(intervals) == 1: return intervals

        def overlap(arr1,arr2):
            if arr1[0]<=arr2[0]<=arr1[1]:
                return [arr1[0],max(arr1[1],arr2[1])]
            return None

        L = len(intervals)
        intervals.sort(key=lambda x: x[0])

        index = 1
        for i in range(L-1):
            val = overlap(intervals[index-1],intervals[index]) 
            if val:
                intervals[index-1] = val
                intervals.pop(index)
            else: 
                index+=1



        return intervals



        
