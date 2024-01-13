from collections import Counter

"""
There are n = 3 connections, the positions of data centers, center = [1, 2, 2] and the positions of the server
destinations destination = [5 2 4].
The most efficient deliveries are:
The center at location 1 makes the first connection to the server at location 2.
The center at location 2 makes the second connection to the server at location 4.
The center at location 2 makes the third connection to the server at location 5.
The minimum total lag is = abs(1- 2)+ abs(2 - 4) + abs(2 -5)= 1 + 2+ 3 = 6
"""


def solution(centers: list, deliveries: list):
    centers.sort()
    deliveries.sort()
    print(centers, deliveries)
    res = 0
    for i in range(len(centers)):
        res += abs(centers[i] - deliveries[i])
    print(res)
    return res


"""
Amazon games is organizing a tournament of pair games where two teams of two players each compete against one another.
There are two groups group1 and group2 of size n each, 
The skill levels of the ith players of the groups are group1[i] and group2[j].
For each pair of indices, (i, j)(0 <=i<j< n) the pair of players(group1[i] group1[j]) compete in the pair game with 
(group2[i] group2[j]).
The winner of the game is group1 if group1[i] + group1[j]> group2[i]+group2[j] and vice-versa.
Given group1, and group2, find the number of games group1 will win. Since the answer can be large, 
report it modulo 109 + 7.
"""


def solution2():
    def count_winning_games(group1, group2):
        # how to be more efficiently?
        MOD = 10 ** 9 + 7
        n = len(group1)
        for i in range(n):
            # O（n）
            group1[i] = group1[i] - group2[i]
        group1.sort()

        def binary_search(idx, lst):
            # 搜比-lst[idx]大的即可, O(logn)
            left, right = idx + 1, n - 1
            while left != right:
                mid = (left + right + 1) // 2
                if lst[mid] < -lst[idx]:
                    left = mid
                else:
                    right = mid - 1
            if lst[left] == lst[right]:
                return left
            else:
                return False

        res = 0
        for i in range(n - 1):
            num = binary_search(i, group1)
            if num:
                res += n - num - 1
        return res % MOD

    # Example usage:
    grp1 = [1, 2, 3, 7, 9, 10]
    grp2 = [3, 2, 1, 8, 1, 12]
    count_winning_games(grp1, grp2)


"""
Amazon has millions of products sold on its e-commerce website, and each product is identified by its product code.
Given an array of n productCodes and order, a string that represents the precedence of characters, 
sort the productCodes in lexicographically increasing order per the precedence.
Note: Lexicographical order is defined in the following way. 
When we compare strings s and t first we find the leftmost position with differing characters: si != ti, 
if there is no such position (e. s is a prefix of t or vice versa) the shortest string is less. 
Otherwise, we compare characters si and ti according to their order in the given precedence order
Example:
If n=2, order = "abcdefghiiklmnoparstuvwxvz", and product Codes is ["adc", "abc"], 
the sorted order is["abc" "adc"]. Consider the strings "adc" and "abc", 
the first point of difference is at position 1 (assuming start index is 0), and d>b 
according to the given precedence order.
Function Description:
Complete the function sortProductCodes in the editor below
sortProductCodes has the following parameter(s): 
string order: the new precedence order 
string productCodes[n]: the array to sort
Returns:
string[n]: the productCodes array in sorted order
Constraints
1<=n<=5000
1<=length(productCodes[i])<=100
length(order)= 26
order and all productCodes[i] contain lowercase English letters only.
"""


def solution3(order: str, productCodes: list):
    hash_map = {c: i for i, c in enumerate(order)}

    def get_order(x):
        return [hash_map.get(c) for c in x]

    productCodes.sort(key=lambda x: get_order(x))
    return productCodes


"""
Amazon is developing an efficient string matching library. 
Develop a prototype service that matches a simple pattern with text.
There are two arrays of strings text and pat, each of size n 
Each string in pat is a regex expression that contains exactly one wildcard character (*)

A wildcard character(*) matches any sequence of zero or more lowercase letters. 
A regex matches some string if it is possible to replace the wildcard character with some sequence of characters
such that the regex expression becomes equal to the string. No other character can be changed. 
For example, regex "abc*bcd" matches "abcbcd", "abcefgbcd" and "abccbcd" 
whereas it does not match the strings "abcbd""abzbcd", "abcd"

For every i from 1 to n, your task is to find out whether pat[i] matches text[i] 
Return the answer as array of strings of size n where the th string is "YES" if pat[i] matches text[i], and "NO" otherwise
Note: The implementation shall not use any in build regex libraries

Example:
Given n = 2, text= ["code", "coder"], pat=["co*d","co*er”]
text[0]= "code" pat[0]= "co*d" "NO" the suffixes do not match
text[1]= "coder", pat[1]= "co*er”,"YES", the prefixes and suffixes match
Here prefix of a string is defined as any substring that starts at the beginning of the string and suffix of 
a string is defined as any substring that ends at the end of the string.

Function DescriptionComplete the function matchStrings in the editor below
matchStrings has the following parameters:
string text[n]: the strings to test
string pat[n]: the patterns to match
Returns:
string[n]: "YES" or "NO" answers to the queries
"""


def solution4(text: list, pat: list) -> list:
    def match(str1, str2) -> bool:
        # dp
        dp = [[False] * (len(str2) + 1) for _ in range(len(str1) + 1)]
        dp[0][0] = True
        for i in range(1, len(str2) + 1):
            if str2[i - 1] == '*':
                dp[0][i] = True
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif str2[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        print(dp)
        return dp[-1][-1]

    res = []
    for i in range(len(text)):
        if match(text[i], pat[i]):
            res.append("YES")
        else:
            res.append("NO")
    print(res)
    return res


"""
Get Mean Rank Count
Amazon Academy recently organized a scholarship test on its platform.

There are n students with roll numbers 1, 2, ..., n who appeared for the test, where the rank secured by the 
ith student is denoted by rank[i]. Thus, the array rank is a permutation of length n. Groups can only be formed with 
students having consecutive roll numbers, in other words, a subarray of the original array. For each value x (1 <= x 
<= n), find the number of groups that can be formed such that they have a mean rank equal to x. 

More formally, given a permutation of length n, find the number of subarrays of the given array having a mean value 
equal to x, for each xin the range [1, n]. 

Notes

1. The mean value of an array of k elements is defined as the sum of elements divided by k.
2. A permutation of length nis a sequence where each number from qtonappears exactly once.
3. A subarray of an array is a contiguous section of the array.
Function Description

Complete the function getMeanRankCount in the editor. getMeanRankCount has the following parameter: 
int rank[n]: the ranks of the students. 

Returns:
int[n]: the ith integer (where 1 <= i <= n) denotes the number of groups with a mean rank of i."""


def solution5(rank: list):
    # 前缀和？nlogn
    preSum = [0] * (len(rank) + 1)
    for i in range(1, len(preSum)):
        preSum[i] = preSum[i - 1] + rank[i - 1]

    def get_count(idx):
        count = 0
        for m in range(1, len(preSum)):
            for n in range(m):
                if (preSum[m] - preSum[n]) / (m - n) == idx:
                    count += 1
        return count

    res = []
    for i in range(1, rank[-1] + 1):
        res.append(get_count(i))
    return res


"""Check Similar Passwords Amazon would like to enforce a password policy that when a user changes their password, 
the new password cannot be similar to the current one. To determine whether two passwords are similar, they take the 
new password, choose a set of indices and change the characters at these indices to the next cyclic character exactly 
once. Character 'a' is changed to "b", 'b' to 'c' and so on, and 'z' changes to 'a'. The password is said to be 
similar if after applying the operation, the old password is a subsequence of the new password. 

The developers come up with a set of n password change requests, where newPasswords denotes the array of new 
passwords and oldPasswords denotes the array of old passwords. For each pair newPasswords[i] and oldPassword[i], 
return "YES" if the passwords are similar, that is newPasswords[i] becomes a subsequence of oldPasswords[i] after 
performing the operations, and "NO" otherwise. 

Note

A subsequence is a sequence that can be derived from the given sequence by deleting zero or more elements without 
changing the order of the remaining elements. 

Function Description

Complete the function checkSimilarPasswords in the editor.

checkSimilarPasswords has the following parameters:

string newPasswords[n]: newPasswords[i] represents the new password of the ith pair
string oldPasswords[n]: newPasswords[i] represents the old password of the ith pair
Returns

string[n]: the ith string represents the answer to the ith pair of passwords.

Example 1:

Input:  newPasswords = ["baacbab", "accdb", "baacba"], oldPasswords = ["abdbc", "ach", "abb"]
Output: ["YES", "NO", "YES"] 
Explanation:


Consider the first pair: newPasswords[0] = "baacbab" and oldPasswords = "abdbc". Change "ac" to "bd" at the 3rd and 
4th positions, and "b" to "c" at the last position. The answer for this pair is YES. 

The newPasswords[1] = "accdb" and oldPasswords = "ach". It is not possible to change the character of the new 
password to "h" which occurs in the old password, so there is no subsequence that matches. The answer for this pair 
is NO. 

newPasswords[2] = "baacba" and oldPasswords  = "abb".
The answer for this pair is YES.

Eventually, we return ["YES", "NO", "YES"].
"""


def solution6(newPasswords: list, oldPasswords: list):
    def check(char, counter) -> bool:
        for c in char:
            if c in counter:
                if counter[c] == 0:
                    if c == 'z':
                        next_ch = 'a'
                    else:
                        next_ch = chr(ord(c) - 1)
                    if next_ch in counter:
                        if counter[next_ch] == 0:
                            return False
                        else:
                            counter[next_ch] -= 1
                    else:
                        return False
                else:
                    counter[c] -= 1
            else:
                if c == 'z':
                    next_ch = 'a'
                else:
                    next_ch = chr(ord(c) - 1)
                if next_ch in counter:
                    if counter[next_ch] == 0:
                        return False
                    else:
                        counter[next_ch] -= 1
                else:
                    return False
        return True

    res = []
    for i in range(len(newPasswords)):
        count = Counter(list(newPasswords[i]))
        if check(oldPasswords[i], count):
            res.append("YES")
        else:
            res.append("NO")
    return res


"""Location Of Data After Transfers X stores its data on different servers at different locations. From time to time, 
due to several factors, X needs to move its data from one location to another. This challenge involved keeping track 
of the locations of X's data and report them at the end of the year. At the start of the year, X's data was located 
at n different locations. Over the course of the year, X's data was moved from one server to another m times. 
Precisely, in the ith operation, the data was moved from movedFrom[i] to movedTo[i]. Find the locations of the data 
after all m moving operations. Return the locations in ascending order. Note: 

It is guaranteed that for any movement of data :

There is data at movedFrom[i].
There is no data at movedTo[i].
Returns
int[]: the locations storing data after all moves are made, in ascending order.

Example 1:

Input:  locations = [1,7,6,8], movedFrom = [1, 7, 2], movedTo = [2, 9, 5]
Output: [5, 6, 8, 9] 

Explanation: Data begins at locations listed in locations. Over the course of the year, the data was moved three 
times. Data was first moved from movedFrom[0] to movedTo[0], from 1 to 2. Next, it is moved from 7 to 9, and finally 
from location 2 to 5. In the end, the locations where data is present are [5,6,8,9] in ascending order. 
      
Example 2:

Input:  locations=[1, 5, 2, 6] , movedFrom=[1, 4, 5, 7] , movedTo=[4, 7, 1, 3]
Output: [1, 2, 3, 6] 

      
Example 3:

Input:   locations=[1, 2, 3] , movedFrom=[1, 2] , movedTo=[5, 6]
Output:  [3, 5, 6] 

"""


def solution7(locations, movedFrom, movedTo):
    data_locations = set(locations)

    for move_from, move_to in zip(movedFrom, movedTo):
        data_locations.discard(move_from)
        data_locations.add(move_to)

    result = sorted(list(data_locations))
    return result
