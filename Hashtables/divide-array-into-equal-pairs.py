from typing import List
from collections import Counter

# def divideArray(nums: List[int]) -> bool:
#     frequecy_map = {}
#     for i in nums:
#         if i in frequecy_map:
#             frequecy_map[i] += 1
#         else:
#             frequecy_map[i] = 1
    
#     for i in frequecy_map.values():
#         if i % 2 != 0:
#             return False
    
#     return True
            
def divideArray(nums: List[int]) -> bool:
    counter = Counter(nums)
    for i in counter.values():
        if i % 2 != 0:
            return False
    return True

ans = divideArray(nums=[3,2,3,2,2,2])
print(ans)


