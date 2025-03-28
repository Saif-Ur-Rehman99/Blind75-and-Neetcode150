from typing import List

def removeElement(nums: List[int], val: int) -> int:
    
    for _ in range(nums.count(val)):
        nums.remove(val)
    
    return len(nums)

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

print(removeElement([3,2,2,3], 3))