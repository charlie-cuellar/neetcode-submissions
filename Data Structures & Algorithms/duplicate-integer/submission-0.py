class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mahp = {}
        for i, num in enumerate(nums):
            if num in mahp:
                return True
            mahp[num] = i
        return False