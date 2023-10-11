'''
pre calculate all the accumulated sum, thus when changing the i and j, we don't need to use a for loop to do sum again,
we just need to use the j sum substract i sum
'''

lass NumArray:

    def __init__(self, nums: List[int]):
        self.presum = nums  # pass by pointer!
        for i in range(len(nums)-1):
            self.presum[i+1] += self.presum[i]
      
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0: return self.presum[right]
        return self.presum[right] - self.presum[left-1]