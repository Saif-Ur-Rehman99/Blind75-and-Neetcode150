from typing import List

def twoSum(array:List, target:int):
    hashmap = {}

    for idx, value in enumerate(array):
        difference = target - array[idx]
        if difference in hashmap:
            return [hashmap[difference], idx]
        hashmap[value] = idx
    
    return

print(twoSum([2,7,11,15], 9))