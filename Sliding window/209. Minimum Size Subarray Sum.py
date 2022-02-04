class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result_len = float('inf')
        sum = 0
        s,e = 0,0
        for e in range(len(nums)):
            sum += nums[e]
            while sum >=target:
                result_len = min(result_len, e - s + 1)
                sum -= nums[s]
                s += 1
        return 0 if result_len==float("inf") else result_len