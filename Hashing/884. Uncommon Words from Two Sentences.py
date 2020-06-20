
"""
in Python, dictionary is realized using hashing. so the time complicity is close to O(1)
in Python, class collections.Counter([iterable-or-mapping]) is a child class of dictionary, hence also realized with hashing
"""

# use collections.Counter()
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        st = A+" "+B
        records=Counter(st.split(" "))# or Counter(st.split())
        return [word for word in records if records[word]==1 ]
