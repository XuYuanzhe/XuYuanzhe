"""
两数之和
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [nums.index(target - num), i]
            lookup[num] = i
        return None


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 26
    so = Solution()
    n = so.twoSum(nums, target)
    print("结果: ", n)
