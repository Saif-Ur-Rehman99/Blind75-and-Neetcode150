def longestPalindrome(string: str)-> str:
    pass

s = "cababa"
result = ""
result_length = 0


for i in range(len(s)):

    # odd length
    left_pointer, right_pointer = i, i
    while left_pointer >= 0 and right_pointer < len(s) and s[left_pointer] == s[right_pointer]:
        if (right_pointer - left_pointer + 1) > result_length:
            result = s[left_pointer:right_pointer + 1]
            result_length = right_pointer - left_pointer + 1
        left_pointer  -= 1
        right_pointer += 1
    
    # even length
    left_pointer, right_pointer = i, i + 1
    while left_pointer >= 0 and right_pointer < len(s) and s[left_pointer] == s[right_pointer]:
        if (right_pointer - left_pointer + 1) > result_length:
            result = s[left_pointer:right_pointer + 1]
            result_length = right_pointer - left_pointer + 1
        left_pointer  -= 1
        right_pointer += 1
    
    
print(result)