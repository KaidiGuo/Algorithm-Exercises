# The biggest square must coming from the two head of the list
# Set two pointers to the start and tail
# Loop towards the center of the list

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        p1,p2 = 0,len(nums)-1
        result=[]
        while p1<=p2:
            r1 = nums[p1]**2
            r2 = nums[p2]**2
            if r1>=r2:
                result.append(r1)
                p1 += 1
            else:
                result.append(r2)
                p2 -=1
        return result[::-1]
        
        