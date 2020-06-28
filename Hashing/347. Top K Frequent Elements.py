"""
Use a hash map/dictionary/counter to store (element,frequency)
The key problem for this question is how to find the top k frequency and its element

Here I just sorted the frequency, pick the number k frequency,
iterate the dictionary, return all keys that have a value bigger or equal to that frequency
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        counts = sorted(dic.values())
        bound = counts[-k]
        result=[]
        for key in dic:
            if dic[key] >= bound:
                result.append(key)
        return result