"""
快速排序
"""


def quick_sort(arr):
    if not arr:
        return []
    else:
        first = arr[0]
        left = quick_sort([l for l in arr[1:] if l < first])
        right = quick_sort([r for r in arr[1:] if r >= first])
        return left + [first] + right
