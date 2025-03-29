def lengthOfLastWord(s: str) -> int:
    s = s.rstrip().split(" ")
    return len(s[-1])
        




# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

print(lengthOfLastWord(s="   fly me   to   the moon  "))