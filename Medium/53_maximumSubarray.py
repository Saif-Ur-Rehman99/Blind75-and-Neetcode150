from typing import List

def maxSubArray(nums: List[int]) -> int:
    
    maxSub = nums[0]
    currSum = 0

    for n in nums:
        if currSum < 0:
            currSum = 0
        currSum += n
        print("current-sum", currSum)
        maxSub = max(maxSub, currSum)
        print("max-sub", maxSub)

    return maxSub


# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1]

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))