def romanToInteger(string: str)-> int:
    roman = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
    }

    result = 0

    for i in range(len(string)):
        if i + 1 < len(string) and roman[string[i]] < roman[string[i+1]]:
            result -= roman[string[i]]
        else:
            result += roman[string[i]]

    return result


print(romanToInteger("III"))