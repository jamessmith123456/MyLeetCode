# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 10:45:11 2019

@author: ZhuangChi
"""

"""
5. 最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""


"""
执行结果：通过
执行用时 :5600 ms, 在所有 Python 提交中击败了13.68%的用户
内存消耗 :11.9 MB, 在所有 Python 提交中击败了32.27%的用户

#基本思路就是：将原本的字符串中间插入一个固定的字符比如* 这样就省去了后面判断奇偶的麻烦
#然后遍历每一个字母(包括后添加的*) 以该字母为中心，逐渐向两边扩展；寻找该字母为中心的最长回文子串
#如果遇到更长的，就更新

class Solution(object):
    def longestPalindrome(self,s):
        snew = '*'
        for i in range(len(s)):
            snew += s[i]
            snew += '*'
        result = None
        len_result = 0
        for i in range(len(snew)):
            temp_result = snew[i]
            temp_len_result = 1

            for j in range(1,min(i,len(snew)-i-1)+1):
                
                if snew[i-j] == snew[i+j]:
                    temp_result = snew[i-j] + temp_result + snew[i-j]
                    temp_len_result += 2
                else:
                    break
            if temp_len_result > len_result:
                result = temp_result
                len_result = temp_len_result
        
        #result.replace('*','')
        F = ''
        for i in range(len(result)):
            if result[i]!='*':
                F += result[i]
        return F
"""

   

#上面的解法是自己的，没做出来；这里参考别人的解法
class Solution(object):
    def longestPalindrome(self,s):
        str_length = len(s)
        max_length = 0
        start = 0
        for i in range(str_length):
            if i - max_length >= 1 and s[i - max_length - 1:i + 2] == s[i - max_length - 1:i + 2][::-1]:
                start = i - max_length - 1
                max_length += 2
                continue
            if i - max_length >= 0 and s[i - max_length:i + 2] == s[i - max_length:i + 2][::-1]:
                start = i - max_length
                max_length += 1
        return s[start:start + max_length+1]