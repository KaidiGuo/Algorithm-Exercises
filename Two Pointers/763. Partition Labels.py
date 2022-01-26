class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        p1,p2=0,0
        most_right = { c : i for i,c in enumerate(s)}
        result=[]
        for i,c in enumerate(s):
            p2 = max(p2, most_right[c])
            if i==p2:
                result.append(p2-p1+1)
                p1=i+1
        return result

# Create a dictionary, keep track of the right most index of each character
# Create two pointers, p1 and p2, starting from 0
# Loop through S
# Inside the loop, keep p2 always at the right most index of all looped characters (using max(p2,most_right{i}))
# When i fininally catchs up p2, means all of the looped characters, their last appearences are smaller than p2 
# You find the first segmentation/partition, now move p1 to i+1 for nect segmentation/partition