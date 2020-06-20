"""
1. if we know all the numbers are unique, we could easily enumerate the list, add (number: index) to a dictionary,
   at the same time search for (target-number) in the dictionary.
2. but now, the question is how to deal with inputs:[3,3] target:6 output:[0,1],
   since we cannot put two identical numbers with different index into a dictionary.
   The answer is, we do not need to actually add the current number n (diff = target-n) into the dic when we find the solution.
   we can simply search for the diff(= target-n) in the dic, if exist, just return the index of diff and current enumerate-index

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dd = {}
        for i,item in enumerate(nums):
            diff=target-item
            if diff in dd:
                return [dd[diff],i]
            if item not in dd:
                dd[item] = i