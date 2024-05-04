def revrerseIntegrer(number: int) -> int:
    
    MIN = -2147483647
    MAX =  2147483648

    num = abs(number)

    reverse = 0 
    while num > 0:
        digit = num % 10
        if ((reverse > MAX // 10) or (reverse == MAX // 10)) and (digit >= MAX % 10):
            return 0
        if ((reverse < MIN // 10) or (reverse == MIN // 10)) and (digit <= MIN % 10):
            return 0
        reverse = (reverse * 10) + digit
        num = num // 10

    return reverse * -1 if number < 0 else reverse 

print(revrerseIntegrer(-7463847412))
