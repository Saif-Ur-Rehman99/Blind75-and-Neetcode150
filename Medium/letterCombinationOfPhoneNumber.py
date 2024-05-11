from typing import List

def letterCombination(digits: str)-> List[str]:
    result = []
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def backTrack(i, current_string):
        
        if len(digits) == len(current_string):
            result.append(current_string)
            return
        
        # for combinations of character
        for j in mapping[digits[i]]:
            backTrack(i + 1, current_string + j)
        
    if digits:
        backTrack(0, "")
    
    return result


print(letterCombination('12'))



