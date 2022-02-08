class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        s = 0
        dict = collections.Counter()
        result = 0
        for i in range(len(fruits)):
            dict[fruits[i]] += 1
            while len(dict) >2:
                dict[fruits[s]] -= 1
                if dict[fruits[s]] ==0:
                    dict.pop(fruits[s])             
                s += 1
            result = max (result, i - s +1)
        return result
        