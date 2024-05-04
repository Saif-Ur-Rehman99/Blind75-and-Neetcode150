def palindrome(number:int):
    temp = number

    reverse = 0
    while number > 0:
        digit = number % 10
        reverse = (reverse * 10) + digit
        number = number // 10
    
    return True if temp == reverse else False
        

print(palindrome(14341))
