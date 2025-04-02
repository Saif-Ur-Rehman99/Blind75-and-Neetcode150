def mySqrt(x: int) -> int:
    if x == 0 or x == 1:
        return x

    left, right = 0, x
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            ans = mid
            left = mid + 1 
        else:
            right = mid - 1

    return ans


# Input: x = 4
# Output: 2

print(mySqrt(8))