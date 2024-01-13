"""1、最少数字
小明用计算机随机生成了N个正整数，他希望从这N个数中选取若干个数，使得它们的和等于M。
这些随机生成的数字可能会相同，但是每个数字最多只允许使用一次。
当然这样的选取方案可能不存在，也可能有多个。
现在希望你编写一个程序，能够找出数字个数最少选取方案，输出对应的最少数字的个数，如果无解输出“NO solution”

输入
单组输入，每组输入2行
第1行包合两个正整数N和M，分别表示初始输入的正整数个数和目标数字和。(N < 103,M < 105)第2行为N个正整数，两两之甸用空格隔开(每一个正整数均小于等于105)
输出
输出数字个数最少的选取方案中所包含的最少数字个数，如果无解输出“No solution”。

样例
输入:
5 5
1 3 2 1 1
输出:
2
"""


def solution1(n, target, nums):
    # 01背包
    dp = [10 ** 9] * (target + 1)
    dp[0] = 0
    for i in range(n):
        for j in range(target, nums[i] - 1, -1):
            dp[j] = min(dp[j], dp[j - nums[i]] + 1)
    print(dp)
    return dp[-1] if dp[-1] != 10 ** 9 else "No solution"


solution1(5, 5, [1, 3, 2, 1, 1])

"""
2、搭建电路
小明迷上了一个搭建电路的游戏。在游戏中，两个电子元件之间只能存在唯一通路，
每次在两个电子元件之间增加一条有效电路(两个元件之间先前没有电路相连)都将获得相应的积分奖励。(初始状态时电子元件之间均未连接)。
已知电子元件数量n和部分电子元件之间的奖励积分值，如何构建一个有效电路将所有元件全部连接起来，并且可以得到最多的积分奖励

输入
第1行输入两个正整数n和m，其中n表示电子元件数量(n <= 100)，m表示提供了m对电子元件之间的奖励积分值(m<=1000)。两个正整数之间用空格隔开。
第2行到第m+1行对应m对电子元件及其对应的奖励积分值，
每一行包含三个正整数，第1个和第2个整数表示电子元件编号(从1开始)第3个整数表示两个元件之间搭建电路的奖励积分num(0< num<10**9)。整数之间用空格隔开

输出
输出占1行，输出一个正整数，即最多可以得到的积分奖励值。如果没有办法把所有元件全部连接起来，则输出“No solution."(注意，tion后有英文句号)。

样例
输入:
3 3
1 2 10
1 3 20
2 3 30
输出:
50
"""


def solution2(n, m, ls_tree):
    # 最小生成树 kruskal
    # n, m = map(int, input().split())
    # ls_tree = [map(int, input().split()) for _ in range(m)]
    ls_tree.sort(key=lambda x: -x[2])
    # 并查集
    fa = [i for i in range(n + 1)]

    def get_f(x):
        # 获取父亲节点
        if fa[x] == x:
            return fa[x]
        else:
            fa[x] = get_f(fa[x])
            return fa[x]

    def merge(i, j):
        fa[get_f(i)] = get_f(j)

    cnt = ans = 0
    for u, v, w in ls_tree:
        if get_f(u) != get_f(v):
            merge(u, v)
            ans += w
            cnt += 1
    print(cnt, ans)
    return ans if cnt == n - 1 else "No solution."


"""
最少数字
小明用计算机随机生成了N个正整数，他希望从这N个数中选取若干个数，使得它们的和等于M。这些随机生成的数字可能会相同，但是每个数字最多只允许使用一次。
当然这样的选取方案可能不存在，也可能有多个。
现在希望你编写一个程序，能够找出数字个数最少的选取方案，输出对应的最少数字的个数，如果无解输出“No solution"。
输入
单组输入，每组输入2行
第1行包含两个正整数N和M，分别表示初始输入的正整数个数和目标数字和(N< 10M105)第2行为N个正整数，两两之间用空格隔开(每一个正整数均小于等于105)。
输出
输出数字个数最少的选取方案中所包含的最少数字个数，如果无解输出“No solution”
样例
输入:
5 5
1 3 2 1 1
输出:
2
"""
# 还是01背包 略


"""
导演在组织进行大运会开幕式的排练，其中一个环节是需要参演人员围成一个环形。
演出人员站成了一圈，出于美观度的考虑，导演不希望某一个演员身边的其他人比他低太多或者高太多。
现在给出n个参演人员的身高，问在他们站成一圈时，相邻演员的身高差的最大值至少是多少? 请你帮忙计算。

输入
输入包括两行，第一行有1个正整数，代表人数n.
第二行有n个空格隔开的正整数h;表示第i个演员的身高
数据保证2<n<10**5,1<hi<10**9
输出
输出包括一个正整数，表示答案

样例
输入:
5
2 1 1 3 2
输出:
1
提示:
排为1，2，3，2，1即可。

输入:
2
10 20
输出:
10
提示:
排为10，20即可。
"""


def solution3(n, heights):
    if n == 1:
        return heights[0]
    if n == 2:
        return abs(heights[1] - heights[0])
    heights.sort(reverse=True)
    # 双指针重构数组，大数在中间
    min_gap = -1
    mid1 = mid2 = heights[0]
    if n % 2 == 0:
        left, right = 0, 1
    else:
        left, right = 1, 2
    while left < n and right < n:
        min_gap = max(min_gap, mid1 - heights[left], mid2 - heights[right])
        mid1 = heights[left]
        mid2 = heights[right]
        left += 2
        right += 2
    print(min_gap)
    return min_gap


solution3(3, [2, 3, 1])
