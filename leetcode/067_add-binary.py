"""
二进制求和
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。
输入: a = "1010", b = "1011"
输出: "10101"
"""


class Solution:
    def addBinary(self, a, b) -> str:
        return '{:b}'.format(int(a, 2) + int(b, 2))

