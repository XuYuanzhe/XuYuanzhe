"""
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。
必须在不使用库的sort函数的情况下解决这个问题。

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

一个数组 里面包含012 要求左边放0右边放1 中间是2 并且时间复杂度O(n)
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, zero, two = 0, -1, len(nums)
        while i < two:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                two -= 1
                nums[i], nums[two] = nums[two], nums[i]
            else:
                zero += 1
                nums[i], nums[zero] = nums[zero], nums[i]
                i += 1
