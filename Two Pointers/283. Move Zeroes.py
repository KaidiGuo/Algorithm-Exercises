# nums[p2] = 0 is used to set allocated number to 0
# this row needs to be placed before nums[p1] = element
# because if there is only one element in the list, put nums[p2] = 0 later will overwrite the correct answer

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p1,p2=0,0
        for p2, element in enumerate(nums):
            if element != 0:
                nums[p2] = 0
                nums[p1] = element
                p1 += 1
               
        return nums