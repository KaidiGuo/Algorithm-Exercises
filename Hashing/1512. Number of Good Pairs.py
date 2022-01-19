import math
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        groups = collections.Counter(nums).values()
        # result = sum([ n * (n-1)/2 for n in groups])
        result = sum([math.comb(n,2) for n in groups])
        return int(result)

# Build in wheel for calculating the combinations.