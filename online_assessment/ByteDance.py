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
    # TODO: ?
    if s == t:
        return 0
    if nums[s - 1] == s or nums[t - 1] == t:
        return -1

    step = 0

    def find(node1, node2, cnt):
        if node1 == node2:
            return cnt
        if cnt > n:
            # 死循环
            return -1
        cnt += 1
        if nums[node2 - 1] == node1 or node2 == nums[node1 - 1]:
            return cnt
        else:
            cnt = min(find(nums[node1 - 1], nums[node2 - 1], cnt), find(nums[node2 - 1], nums[node1 - 1], cnt))
            return cnt

    a = find(s, t, step)
    print(a)
    return a


# print(solution2(6, 1, 4, [3, 6, 4, 1, 2, 5]))

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
现有一个长度为n的数组a和m个区间, 你可以选择任意个区间，选择的区间不能相交。如果选择一个区间[l, r]。那么可以获得ai的分数为数组区间[l,r]之和。
请你计算出你可以获得的最大分数
请注意，如果区间右端点在数组的范围之外，则该区间不可选取.假设两个区间分别是l1,r1和l2,r2，如果它们满足l1<=l2<=r1或l2<=r1<=r2，
则认为这两个区间相交

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


def solution4(n, m, nums, intervals):
    # TODO: 没懂
    # dp 选或不选， leetcode 689? 前i个元素中，一个最优秀的选法所得到的最大分数和
    intervals.sort(key=lambda x: x[0])
    g = [[] for _ in range(n + 1)]
    # 前缀和
    preSum = [0] * (n + 1)
    for i in range(1, n + 1):
        preSum[i] = preSum[i - 1] + nums[i - 1]

    for i in range(m):
        l, r = intervals[i]
        if r <= n:
            g[r].append(l)
    print(g)

    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        for l in g[i]:
            dp[i] = max(dp[i], dp[l - 1] + preSum[i] - preSum[l - 1])

    return dp[-1]


# print(solution4(5, 3, [1, 2, 3, 4, 9], [[1, 4], [2, 3], [4, 5]]))
"""
1、小红操作数组
小红拿到了一个数组，她准备进行任意次以下操作：
选择一个正整数x，使得数组的每个ai都变成x%ai。
小红希望最终数组的每个元素都相等且大于0。她想要你告诉她能否达成目的。

输入
有多组测试用例，第一行输入一个整数t，表示用例组数。
接下来每2*t行，表示一组用例。对于每组用例：
第一行输入一个正整数n，代表数组的大小。
第二行输入n个正整数ai，代表小红拿到的数组。
1<=t,n,ai<=10**5
保证n的总和不超过10**5。

输出
如果可以使得所有数相等且大于0，输出 "Yes"。否则输出 "No"。

样例：
输入：
3
2
3 6
3
1 2 3
2
3 3

输出：
Yes
No
Yes
"""


def solution5(n, nums):
    # x = 1
    return 1 not in nums or n == 1


"""
2、小红的有根树
小红拿到了一棵有根树，其中根是1号节点。小红准备给每个节点染成红色或者绿色或者蓝色。但是有以下两个要求：
1. 每个节点和它的父亲颜色不同。 （如果它存在父亲）
2. 每个节点和它的父亲的父亲颜色不同。 （如果它存在父亲的父亲）
请你输出任意一种染色方案。

输入
第一行输入一个正整数m，代表节点的数量。
接下来的n-1行，每行输入两个正整数u和v，代表节点u和节点v有一条边连接。
1<=n<=10**5
1<u,v<=n
输出
一个长度为n的、仅由'R','G','B' 三种字母组成的字符串。第i个字符为'R' 代表号节点被染成红色，为'G' 代表染成绿色，'B' 代麦染成蓝色。
如果有多解，输出任意即可。

样例
输入：
4
1 2
3 4
1 3

输出：
BGRG

"""


def solution6(m, maps):
    # dfs
    # construct tree
    tree = [[] for _ in range(m)]
    tree = [[1]] + tree
    for i in range(len(maps)):
        tree[maps[i][0]].append(maps[i][1])
        tree[maps[i][1]].append(maps[i][0])

    res = [""] * m
    t = "RGB"
    tree[1].append(0)
    print(tree)

    def dfs(node, father, depth):
        res[node - 1] = t[depth % 3]
        for k in range(len(tree[node])):
            if tree[node][k] == father:
                continue
            dfs(tree[node][k], node, depth + 1)

    dfs(1, 0, 0)
    return "".join(res)


# solution6(4, [[1, 2], [3, 4], [1, 3]])

"""
小红想用山楂制作糖葫芦，一串糖葫芦用一串字符串表示，糖葫芦的甜度为串上所有字符的甜度之和。字符的甜度为这个字符与字符'a'的差值。
即'a'的甜度为0，'b'的甜度为 1 ..... 'z' 的甜度为 25。小红有n个山植按顺序从1到n依次摆放，山植被表示为一个字符，山植的甜度即为字符的甜度。
小红制作糖葫芦时，需要取出一段连续的山楂制作成糖葫芦。
小红想知道，在所有可能被制成的糖葫芦中，甜度第k大的糖葫芦甜度为多少？
若有一根糖葫串本身或翻转后与另一串糖葫芦相同，则这两串糖葫芦被视为是相同的糖葫芦。
例如，糖葫芦 "abc" 与 "cba" 被认为是相同的糖动芦。

输入
第一行输入两个整数 n, k (1<=n<=200,1<=k<=n*(n+1)/2)
第二行输入一个长度为n的字符串，表示山楂的摆放顺序。

输出
一行一个整数，表示甜度第k大的是多少。若可能产生的糖葫芦数小于k-1，则输出 -1。

样例
输入：
3 4
abc

输出：
1

提示：
可能制作的糖葫芦串为a,b,c,ab,bc,abc。甜度分别为0,1,2,1,3,3，其中第4甜的糖葫芦串甜度为1。

输入：
3 4
aba

输出：
0

提示：
可以制作的糖葫芦只有4种："a"、"b"、"ab"、"aba"甜度分别是0,1,1,2，第4甜的糖葫芦甜度为0。请注意，"ba"和"ab"被视为同一种
"""

import heapq


def solution7(n, k, string):
    # 穷举组合求分数

    # TODO: 用堆求topk优化？
    class Num:
        def __init__(self, scores, num):
            self.score = scores
            self.num = num

        def __lt__(self, other):
            if self.score < other.score:
                return True
            else:
                return False

    nums = []
    memo = set()
    for i in range(n):
        for j in range(i, n):
            tmp = string[i:j + 1]
            if tmp in memo or tmp[::-1] in memo:
                continue
            memo.add(tmp)
            score = 0
            for t in tmp:
                score += ord(t) - ord('a')
            nums.append(Num(score, tmp))
    nums.sort(reverse=True)
    if len(nums) < k - 1:
        return -1
    return nums[k - 1].score


print(solution7(3, 4, "abc"))

"""
小红拿到了一个数组，她可以进行以下操作：选择两个相同的元素 x，将它们删除，并将2x添加进数组。这种操作称为一次 “合并”。
小红在进行合并之前可以先往数组里添加任意一个元素。之后小红希望最大化 “合并” 的次数。请你帮帮小红。

输入
第一行输入一个正整数n，代表数组的大小。
第二行输入n个正整数ai，代表小红拿到的数组。
1<=n<=10**5
1<=ai<=10**9

输出
输出两个整数，第一个数为添加的元素，第二个数为合并的最大次数。
如果有多种添加的方案，输出任意一个即可。

样例
输入：
3
1 1 3

输出：
3 2

提示：
添加3后，数组变成[1,1,3,3]，可以合并两次。
添加2也是可以的，依然可以合并2次。
"""


def solution8(n, nums):
    # 优先合并已经是两个的 可以更高效吗？
    counter = Counter(nums)
    step = 0

    def merge(counters, num, times):
        if counters[num] <= 1:
            return times
        else:
            cnt = counters[num] // 2
            times += cnt
            counters[num] = counters[num] % 2
            counters[2 * num] = counters[2 * num] + cnt
            times = merge(counters, counters[2 * num], times)
            return times

    keys = list(counter.keys())
    for i in keys:
        if counter[i] > 1:
            step = merge(counter, i, step)

    nums = [i for i in counter if counter[i] != 0]
    print(nums, step)
    nums.sort(reverse=True)
    max_step = 0
    res = -1
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            tmp = nums[i]
            time = 0
            while tmp % 2 == 0 and tmp // 2 in nums:
                time += 1
                tmp = tmp // 2
            if time > max_step:
                max_step = time
                res = tmp
    if max_step != 0:
        max_step += 1
    return [res if res != -1 else nums[0], step + max_step]


# print(solution8(3, [1, 2, 3, 4]))

"""
5、小红统计子数组
小红拿到了一个大小为n的数组，她想知道，有多少个连续子数组满足，该子数组所有元素的乘积是k的倍数？

输入
第一行输入两个正整数n和k。
第二行输入n个正整数ai。
1<n<10**5
1<ai<10**6
1<k<10**12

输出
满足条件的子数组数量。

样例：
输入：
3 6
2 3 4

输出：
3
"""

import numpy as np


def solution9(n, k, nums):
    # 前缀积, 子数组需要时连续的 TODO: preprod有可能很大？
    preProd = [1]*(n+1)
    for i in range(1, n+1):
        preProd[i] = preProd[i-1]*nums[i-1]
    print(preProd)

    cnt = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            if preProd[j] / preProd[i-1] % k == 0:
                cnt += 1

    print(cnt)
    return cnt


solution9(3, 6, [2, 3, 4])
