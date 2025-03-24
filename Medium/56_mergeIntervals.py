from typing import List

# fastest
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         merged=[]
#         intervals.sort(key=lambda x:x[0])
#         prev=intervals[0]
#         for interval in intervals[1:]:
#             if interval[0]<=prev[1]:
#                 prev[1]=max(prev[1],interval[1])
#             else:
#                 merged.append(prev)
#                 prev=interval
#         merged.append(prev)
#         return merged


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key= lambda i : i[0])
    output = [intervals[0]]
    
    for start, end in intervals[1:]:
        lastEnd = output[-1][1]

        if start <= lastEnd:
            output[-1][1] = max(lastEnd, end)
        else:
            output.append([start, end])
        
    return output


print(merge([[1,3],[2,6],[8,10],[15,18]]))