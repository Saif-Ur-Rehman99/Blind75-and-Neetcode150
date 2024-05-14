def lengthOfLongestSubstring(string: str)-> str:
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
        