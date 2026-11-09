

# nums = [3,4,5,6], target = 7

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen: 
                #Round 1: i = 0, n =3 -> 7-3 = 4 in seen?
                #Round 2: i, 1, n=4 -> 7 - 4 = 3 in seen? -> True
                return [seen[target-n], i ] # lookup for the number 3 in seen and found 
                                            # its in index 0, i is the current index = 1
                                            #-> [0, 1]
                

            seen[n] = i # add the current number and index to the map {3: 0}


