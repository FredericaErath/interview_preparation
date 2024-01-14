"""
小红的赛车队
假设有n个赛车队参加一场比赛，每个赛车队的车辆数为ai辆，要将这个赛车队分成小组，每个小组里的车辆总数不超过4辆，
并且不能把赛车队拆开。问最少需要多少个小组。

输入
行一个整数t，表示数据组数
每组数据第一行一个整数n，表示赛车队数
接下来一行n个整数ai，表示每个赛车队的车辆数。
1<t<100
1<n<10**3
1<ai<4
输出
输出t行，每行一个整数，表示最少需要的小组数

样例
输入:
1
4
1 2 3 4
输出:
3
提示:
前两个车队一组，第三个车队一组，第四个车队一组即可。
"""
from collections import Counter


def solution1(cars):
    cars.sort()
    # 4自己, 2+2, 1+3, 1+1+2
    cnt = 0
    counter = Counter(cars)
    # 4
    cnt += counter[4]
    # 3 + 1
    cnt += counter[3]
    if 1 in counter:
        if counter[3] >= counter[1]:
            counter[1] = 0
        else:
            counter[1] = counter[1] - counter[3]
    # 2 + 2
    if counter[2] > 1:
        cnt += counter[2] // 2
        counter[2] = counter[2] % 2
    cnt += counter[2]

    counter[1] = counter[1] - 2 * counter[2]
    # 2+1 // 2+1+1
    if counter[1] > 0:
        cnt += counter[1] // 4 + 1
    print(cnt)
    return cnt


"""
小红走迷宫
小红和朋友被困在了迷宫里，迷宫有n个传送阵，每个传送阵都有一个编号i(编号从1到n)，编号为的i传送阵会将小红传送到编号为ai的传送阵。
小红最初在编号为s的传送阵，朋友最初在编号为t的传送阵，小红和朋友都可以通过传送阵传送，每次传送都会花费一分钟(两人可以同时传送)。
现在小红想知道，小红和朋友最少需要多少分钟才能在同一个传送阵里见面，如果不能见面，输出-1。

输入
第一行输入三个整数n,s,t，表示传送阵的数量，小红最初所在的传送阵编号，朋友最初所在的传送阵编号.
第二行输入n个整数ai，表示编号为的传送阵会将小红传送到编号为ai的传送阵
1<n<10**5
1<s,t<n
1<ai<n
保证ai数组中的元素互不相同
输出
输出一个整数，表示小红和朋友最少需要多少分钟才能在同一个传送阵里见面，如果不能见面，输出-1.

样例
输入:
5 1 2
5 1 2 3 4
输出:
1
提示:
朋友可以通过一次传送到达小红所在位置
"""


def solution2(n, s, t, nums):
    # TODO: is it correct to use DSU?
    if s == t:
        return 0
    remove = set()
    for i in range(n):
        if nums[i] == i + 1:
            remove.add(i + 1)
    if s in remove or t in remove:
        return -1

    step = 0

    def find(node1, node2):
        nonlocal step
        if node1 == node2:
            return node1
        node1 = find(node1, nums[node2 - 1])
        step += 1
        return node1

    find(s, t)

    return min(len(nums) - len(remove) - step, step)


print(solution2(3, 2, 3, [1, 3, 2]))
