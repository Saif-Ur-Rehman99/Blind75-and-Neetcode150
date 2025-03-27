
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    
    div = 1
    while x >= 10 * div:
        div *= 10
    
    while x:
        r_num = x % 10
        l_num = x // div

        if r_num != l_num:
            return False
        
        x = (x%div)//10
        div = div / 100
    

    return True

        


print(isPalindrome(22))
