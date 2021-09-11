"""
第四题（选答）
有两组数，第⼀组数顺序固定，请编程实现让第⼆组数 相邻数字间的⼤⼩关系和第⼀
组数相同，且
第⼆组相邻数字间的差值之和最⼤
下⾯给出⼀个示例
第⼀组数： 5 7 4 9
第⼆组数：1 2 3 4
第⼆组数排序结果：2 4 1 3
第⼆组数排序后的差值之和：7 = abs(2-4) + abs(4-1) + abs(1-3)
"""


def main(list1, list2):
    rv = [0] * len(list1)
    for i in range(len(list1)):
        if i - 1 >= 0:
            rv[i] += 1 if list1[i - 1] < list1[i] else -1
        if i + 1 < len(list1):
            rv[i] += 1 if list1[i + 1] < list1[i] else -1

    indexes = sorted(range(len(list1)), key=lambda idx: (rv[idx], list1[idx]))
    return [pair[1] for pair in sorted(list(zip(indexes, sorted(list2))))]


if __name__ == '__main__':
    main([4, 8, 7, 9, 3], [1, 2, 3, 4, 5])
