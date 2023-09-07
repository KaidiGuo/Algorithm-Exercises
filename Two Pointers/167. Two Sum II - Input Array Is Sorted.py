# Solution 1: Hash

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict ={}
        for i, number in enumerate(numbers):
            if target - number in dict:
                return [dict[target-number]+1, i+1]
            else:
                dict[number] = i

# Solution 2 : 2 pointer
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1