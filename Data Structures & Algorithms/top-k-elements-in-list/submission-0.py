class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top = {}

        for i in nums:
            if i not in top:
                top[i] = 1
            else:
                top[i] += 1
        print(top)

        res = sorted(top, key=top.get, reverse=True)[:k]

        return res