class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.hashmap = {}

        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                    if self.nums[i] + self.nums[j] == target:
                        return [i,j]
        return []