class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], idx]
            hashmap[num] = idx
