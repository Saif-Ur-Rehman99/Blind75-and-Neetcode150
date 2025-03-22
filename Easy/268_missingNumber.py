from typing import List

def missingNumber(nums: List[int]) -> int:
    for i in range(0, len(nums)+1):
        if i not in nums:
            break
    return i


# def missingNumber(nums: List[int]) -> int:
#     res = len(nums)
#     for i, v in enumerate(nums):
#         res = res ^ i
#         res = res ^ v
    
#     return res

a = [3,0,1]
b = [0,1]
c = [9,6,4,2,3,5,7,0,1]

print(missingNumber(c))
