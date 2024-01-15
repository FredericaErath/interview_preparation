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

    memo = []

    def find(node1, node2):
        nonlocal step
        memo.append(node2)
        if node2 in memo:
            return -1
        if node1 == node2:
            return node1
        node1 = find(node1, nums[node2 - 1])
        step += 1
        return node1

    a = find(s, t)
    b = find(t, s)
    if a == -1 or b == -1:
        return -1
    else:
        return min(a, b)


print(solution2(5, 2, 1, [5, 3, 2, 1, 4]))

"""
3、小红的前缀和之和
给定两个正整数n,x，小红希望你构造一个长度为n的数组，满足sum(i)=x。
sum(i)即数组的前项之和。换言之，小红希望你构造一个长度为n的数组满足，n个前缀和之和等于x。
要求数组的元素仅由1和2组成。

输入
两个正整数nt
·1<n<10**5
·1<z<10**18
输出
如果无解，请输出-1。
否则输出n个正整数，每个正整数为1或者2。有多解时输出任意即可

样例
输入:
3 8
输出:
1 2 1
提示:
三个前缀和分别是1,3,4,1+3+4=8，符合条件。
"""


def solution3(n, target):
    # 枚举
    if (1 + n) * n < target < (1 + n) * n // 2:
        return [-1]
    # 数组每一个都减去1， 填入0/1
    target -= (1 + n) * n // 2
    res = []
    for i in range(n):
        if n - i > target:
            res.append(1)
        else:
            res.append(2)
            target -= n - i
    return [-1] if target > 0 else res


"""
4、不相交区间
现有一个长度为n的数组a和m个区间, 你可以选择任意个区间，选择的区间不能相交。如果选择一个区间[l, r]。那么可以获得》ai的分数。-
请你计算出你可以获得的最大分数
请注意，如果区间右端点在数组的范围之外，则该区间不可选取假设两个区间分别是l1,r1]和/2,r，如果它们满足<r或rr2，则认为这两个区间相交

输入
第一行两个整数n,m，表示数组的长度和区间的个数
第二行n个整数ai，表示数组的元素
接下来m行每行两个整数li,ri，表示每一个区间
1<n,m,ai< 105
1<l<r<105
输出
输出一个整数，表示可以获得的最大分数。

样例
输入：
5 3
1 2 3 4 9
1 4
2 3
4 5

输出：
18

输入：
5 3
9 2 3 4 1
1 4
2 3
4 5

输出：
18
"""
# def solution4(n, m, nums, intervals):
#     # dp?
