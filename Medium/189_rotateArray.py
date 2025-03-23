from typing import List

# Complexity O(k*n)
def rotate_1(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in reversed(nums[-k:]):
        nums.insert(0,i)
        nums.pop()
    
    return nums


# Complexity O(n)
def rotate2(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    shifted_array = nums.copy()
    for i in range(len(nums)):
        idx = (i+k) % len(nums)
        shifted_array[idx] = nums[i]
    
    return shifted_array


# Complexity O(n)
def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    pairs = [(0, len(nums)-1), (k, len(nums)-1), (0, k-1)]
    for pair in pairs:
        l, r = pair
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    return nums    


example1 = [1,2,3,4,5,6,7] # [5,6,7,1,2,3,4]
example2 = [-1,-100, 3,99] # [3, 99,-1,-100]
print(rotate(example1, k=3))