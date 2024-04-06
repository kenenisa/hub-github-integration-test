# Problem: Two Sum - https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        df = defaultdict(int)
        n = len(nums)
        for i in range(n):
            a = target - nums[i]
            if a in df:
                return [i,df[a]]
            else:
                df[nums[i]] = i 