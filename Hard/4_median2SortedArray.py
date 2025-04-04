from typing import List
import numpy as np

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    # total = sorted(nums1 + nums2)
    # size = len(total) // 2

    # print("total: ", total, " size: ", size)
    
    # if len(total) % 2 == 0:
    #     print("condition 1")
    #     return (total[size-1] + total[size]) / 2
    # else:
    #     print("condition 2")
    #     return total[size]
    if len(nums1) > len(nums2):
        # nums1 is smaller array
        nums1, nums2 = nums2, nums1  

    m, n = len(nums1), len(nums2)
    low, high = 0, m

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (m + n + 1) // 2 - partitionX

        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == m else nums1[partitionX]

        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == n else nums2[partitionY]

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (m + n) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1

    return 0.0



# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

print(findMedianSortedArrays([1,2],[3,4]))