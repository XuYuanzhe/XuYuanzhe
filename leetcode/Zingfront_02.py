"""
第⼆题（必答）
给定⼀个数组，例如[15, 2, 8, 13]，找到符合下⾯⽅式的结果，并打印出来
例如：
1）从数组每位元素当前位置开始，往后找到⼤于⾃⼰本身的第⼀位元素，并返回
1）如果没有找到，返回-1
结果如下
15 -> -1
2 -> 8
8 -> 13
13 -> -1
返回结果：
要求：写出解题思路并给出时间复杂度，并说明最坏情况（可考虑栈）

时间复杂度：nlogn
解题思路：遍历数组，双指针向中间查询大于idx值的元素，若未找到返回-1。
    在两指针相遇前，左指针指向的数的index永远小于右指针，故无需对比
    两指针距离idx的距离，左指针找到big_num及⼤于⾃⼰本身的第⼀位元
    素。右指针在慢慢靠近idx，所以需要不停更新big_num。
最坏情况：递减数组最右元素大于最左元素
"""


def foo(nums):
    if not nums:
        return

    for idx, num in enumerate(nums):
        i = idx + 1
        j = len(nums) - 1
        big_num = -1
        while i <= j:
            left = nums[i]
            right = nums[j]
            if left > num:
                big_num = left
                break
            if right > num:
                big_num = right
            i += 1
            j -= 1
        print(f'{num} -> {big_num}')


if __name__ == '__main__':
    foo([5, 1, 3, 2, 4, 6, 9, 7, 8])
