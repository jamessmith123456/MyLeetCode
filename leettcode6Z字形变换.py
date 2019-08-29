# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 00:41:45 2019

@author: ZhuangChi
"""
"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""

#我的想法是一个周期就是一列加上斜的一条线(减去最后一个位置)
"""
执行结果：通过
执行用时 :864 ms, 在所有 Python 提交中击败了5.04%的用户
内存消耗 :13.5 MB, 在所有 Python 提交中击败了5.03%的用户
import math
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        cycle_length = numRows + (numRows-2)
        cycle_pos = []
        for i in range(numRows):
            cycle_pos.append(i)
        for i in range(1,numRows-1):
            cycle_pos.append(numRows-1-i)
        #cycle_pos:[0,1,2,3,2,1]
        #这里学一下python的三目运算符写法：a = (x if (x>y) else y)
        cycle_number = math.floor(len(s)/cycle_length)
        
        #擦 终于找出问题了 len(s)%cycle_length==0 时 last_cycle_columns也是1 这怎么可以呢
        if len(s)%cycle_length != 0:
            last_cycle_columns = 1 if (len(s)%cycle_length)<= numRows else 1+((len(s)%cycle_length)-numRows)
        else:
            last_cycle_columns = 0
            
        columns = int(cycle_number*(1+numRows-2) + last_cycle_columns)
        
        
        allZ = []
        for i in range(numRows):
            temp_row = []
            for j in range(columns):
                temp_row.append('')
            allZ.append(temp_row)
        
        for i in range(len(s)):
            t = i+1
            row_index = cycle_pos[i%cycle_length]
            temp_cycle_number = math.floor(t/cycle_length)
            if t%cycle_length!=0:
                temp_last_cycle_columns = 1 if (t%cycle_length)<= numRows else 1+((t%cycle_length)-numRows)
            else:
                temp_last_cycle_columns = 0

            column_index = int( temp_cycle_number *(1+numRows-2) + temp_last_cycle_columns )-1
    
            allZ[row_index][column_index] = s[i]
            
        result = ''
        for i in range(numRows):
            for j in range(columns):
                result += allZ[i][j]
        return result
"""


class Solution(object):
    def convert(self, s, numRows):
        allZ = []
        
        #下面逐步确定每一行的内容
        


