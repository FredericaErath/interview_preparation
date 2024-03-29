"""
小红喜欢偶数，即一个数从因数分解的角度来看，其中的偶数因子越多，她就越喜欢这个数。也就是，x = p1*p2*...*pk其中都是偶数，
那么k的最大值就是小红对这个数的喜欢程度。小红想知道区间[l,r]的数中，小红对哪个数的喜欢程度最高，输出小红的喜欢程度。

输入
一行两个整数l,r，表示区间[l,r]。
·1<=l<=r<=10**9
输出
输出一个整数，表示小红对这个数的喜欢程度

样例
输入:
3 10
输出:
3
提示:
小红最喜欢的数是8，喜欢程度是3，因为8=2x2x2。
"""


def solution1(l, r):
    pass


"""
小红的数组
小红有一个数组a，每次可以进行以下两种操作:
1.选择一个下标i，将ai加2，即ai=ai+2
2.选择一个下标i，如果ai = ai+1，将ai和a(i+1)加1，即ai = ai+1,a(i+1) = a(i+1) +1; 否则不能进行操作.
小红可以进行若干次操作，小红想知道能否通过若干次操作使得数组a中所有元素相等。

输入
第一行一个整数t，表示数据组数。
接下来t组数据，每组数据第一行一个整数n，表示数组长度接下来一行n个整数a1,a2,...,an，表示数组a的初始值。
1<t<10
1<n<10**5
1<ai<10**9
输出
输出t行，每行一个字符串，如果能使得数组a中所有元素相等，输出”YES”，否则输出“NO”。
"""


def solution2(t, nums):
    # [[3, [1,2,3]], [3, [1,1,3]], [3, [2,2,3]]]
    # 判断原数列是否存在相邻差为偶数的数对

    pass


"""
Leetcode 898
按位或的性质？
#从x = nums[i]出发，OR的结果至多有多少种
#关键:1不能变成0，0可以变成1
#至多能变多少次? 变29次，总共30种
"""


def solution3():
    pass
