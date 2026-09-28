class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}

        for i in nums:
            count[i] = 1 + count.get(i, 0)

        sorted_count = sorted(count.items(), key=lambda item: item[1], reverse = True)

        res = []

        for i, cnt in sorted_count[:k]:
            res.append(i)
        return res