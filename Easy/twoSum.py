from typing import List

def twoSum(array:List, target:int):
    hashmap = {}

    for i, value in enumerate(array):
        difference = target - array[i]
        if difference in hashmap:
            return [hashmap[difference], i]
        hashmap[value] = i


print(twoSum(array=[8 ,2, 4, 7, 3], target=7))
