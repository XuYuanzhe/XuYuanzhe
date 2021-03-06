"""
第⼀题（必答）
某企业拥有4条流⽔⽣产线A、B、C、D，每条流⽔线⽬前每⽉的⽣产量在10、7、
5、4吨。现企业需要优化各流⽔线，故实⾏每⽉末从⽣产最多的流⽔线中抽出3吨
的⽣产⼒，分配到剩余的3条流⽔线⾥，既其余每条流⽔线多⽣产1吨，这称为⼀次
⽣产⼒优化（既经过第⼀个⽉后的优化，各流⽔线⽣产吨数在：7、8、6、5）
那么请问，经过五年的⽣产⼒优化调整后，哪个流⽔线⽣产⼒最⾼，可每⽉⽣产多
少吨
编程求解该问题，并思考是否为最优解。
"""


def main():
    periodic = [
        {'A': 7, 'B': 8, 'C': 6, 'D': 5},
        {'A': 8, 'B': 5, 'C': 7, 'D': 6},
        {'A': 5, 'B': 6, 'C': 8, 'D': 7},
        {'A': 6, 'B': 7, 'C': 5, 'D': 8}
    ]
    month = 5 * 12
    status = periodic[month % 4]
    print('⽣产⼒最⾼流⽔线: %s' % max(status, key=status.get))
    print('每⽉⽣产: %s' % status[max(status, key=status.get)])


if __name__ == '__main__':
    main()
