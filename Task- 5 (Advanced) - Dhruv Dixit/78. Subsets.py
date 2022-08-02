class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[x for y in [list(combinations(nums,i)) for i in range(len(nums)+1)] for x in y]
        return res