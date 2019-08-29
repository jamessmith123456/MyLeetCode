# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 00:45:32 2019

@author: ZhuangChi
"""

"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。


示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
"""


难点在于无法根据不确定长度的字符串中字符个数来确定for循环的代码层数
解决：每次只取前一次的暂时结果，与当前的做组合，存储为中间结果



"""****************************************************************************
下面的代码存在非常致命的错误！电脑死机了两次！41行针对temp_result进行了for循环 而44行又改变了temp_result
(实际上temp_result变长了)  这就导致了无限循环！
****************************************************************************"""
class Solution(object):
    def letterCombinations(self, digits):
        num_str_dict = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        temp_result = ['']
        if digits == '':
            result = []
        for num in digits:
            result = []
            for s in num_str_dict[num]:
                for j in temp_result:
                    result.append(j+s)
                    temp_result = result
        
        return result



"""
执行结果：通过
执行用时 :20 ms, 在所有 Python 提交中击败了84.49%的用户
内存消耗 :11.7 MB, 在所有 Python 提交中击败了26.65%的用户  
""" 
class Solution(object):
    def letterCombinations(self, digits):
        num_str_dict = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        temp_result = ['']
        if digits == '':
            result = []
        for num in digits:
            result = []
            for s in num_str_dict[num]:
                for j in temp_result:
                    result.append(j+s)
            temp_result = result
        
        return result

"""
下面是参考别人的代码
"""
class Solution:
    def letterCombinations(self, digits):
        KEY = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        if digits == '':
            return []
        ans = ['']
        for num in digits:
            ans = [pre+suf for pre in ans for suf in KEY[num]] #跟我的想法一样思路 不过人家聪明一点 这样可以省点内存
                                                               #不对!好像不是这样！ []也是开辟了一个内存...然后复制给ans
                                                               #跟我的一样..
        return ans



BFS+hash table来完成？？？
