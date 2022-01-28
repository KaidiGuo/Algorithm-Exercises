# p1, the slow pointer is used to rewrite element into the list, starting index 0
# p2, is looping through the list
# if p2 meets any value that is the to-be-deleted target, p1 do nothing
# if p2 meets any keeping value, p1 write to current index, then move to next index

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1,p2=0,0
        for p2 in range(len(nums)):
            if val != nums[p2]:
                nums[p1] = nums[p2]
                p1 += 1
        return p1