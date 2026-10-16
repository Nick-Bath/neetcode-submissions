class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexs = []
        for i in range(len(nums)):
            j = 0
            for j in range(len(nums)):
                if (nums[i] + nums[j]) == target and i != j:
                    indexs.append(i)
                    indexs.append(j)
                    return indexs