class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Input: nums = [1, 2, 3, 3]
        seen = set()
        for nums in nums:
            if nums in seen:
                return True
            seen.add(nums)
        return False

