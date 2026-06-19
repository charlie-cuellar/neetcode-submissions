class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mahp = {}
        for i, num in enumerate(nums):
            ans = target - num
            if ans in mahp:
                realans = [i, mahp[ans]]
            mahp[num] = i
        return sorted(realans)