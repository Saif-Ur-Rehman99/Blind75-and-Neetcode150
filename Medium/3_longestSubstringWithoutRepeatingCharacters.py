def lengthOfLongestSubstring(s: str)-> str:
    character_set = set()
    left_pointer = 0
    count = 0
    for right_pointer in range(len(s)):
        while s[right_pointer] in character_set:
            character_set.remove(s[left_pointer])
            left_pointer += 1
        character_set.add(s[right_pointer])
        count = max(count, right_pointer - left_pointer + 1)
    return count

s= 'abcabcbb'



# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
