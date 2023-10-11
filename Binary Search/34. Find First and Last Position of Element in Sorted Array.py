# very similar to the basic binary search
# the only difference is the target value can repeat n times in the list, so once you locate the mid that eaqual to the target number
# you need two pointers from the mid to find the left and right boundary index that gives you the same value as the target

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = l +(r-l)//2
            if nums[mid] == target:
                l = mid
                r = mid
                
                while l >=0 and nums[l] == target :
                    l -= 1                   
                   
                while r <=len(nums)-1 and nums[r] == target :
                    r +=1
            
                return [l+1,r-1]
            elif nums[mid] > target:
                r = mid -1
            elif nums[mid] < target:
                l = mid + 1
        return [-1,-1]