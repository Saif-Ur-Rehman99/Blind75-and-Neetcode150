
def addBinary(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]

# Input: a = "11", b = "1"
# Output: "100"

# Input: a = "1010", b = "1011"
# Output: "10101"


print(addBinary(a="1010", b="1011"))