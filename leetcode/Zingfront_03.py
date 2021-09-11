"""
第三题（选答）
有⼀段12组成的字符串，例如"1212111212"，可进⾏0或多次的⼀下规律：从某⼀位
置分隔成两个字符串，两个字符串同时翻转后在拼接。找出最⻓的连续12相间的⻓度
~~
例如:
1212111212  假设从第五、六位分隔 12121, 11212 翻转后 12121 , 21211 拼接后
1212121211 这个时候的连续12相间的⻓度为9，也是最⻓的连续12相间的
"""


def get_long(one_two_str):
    if one_two_str[0] == one_two_str[1]:
        return one_two_str

    for i in range(len(one_two_str) - 1):
        if one_two_str[i] == one_two_str[i+1]:
            left_str = one_two_str[:i+1]
            right_str = one_two_str[i+1:]
            new_str = left_str[::-1] + right_str[::-1]
            return get_long(new_str)


if __name__ == '__main__':
    get_long('1212111212121212112')
