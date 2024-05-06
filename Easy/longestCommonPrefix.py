from typing import List

def longestCommonPrefix(string: List[str])-> str:
    result = ""
    sorted_list = sorted(string)

    first_element = sorted_list[0]
    last_element = sorted_list[-1]

    for i in range(len(first_element)):
        if first_element[i] != last_element[i]:
            break
        result += first_element[i]

    return result
