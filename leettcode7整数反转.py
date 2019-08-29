# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 08:43:35 2019

@author: ZhuangChi
"""

"""
7.整数反转
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2**31,2**31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""



"""
关于python的简写：
y = [1,2,3,4,5,6]
[(i*2) for i in y ]
会输出  [2, 4, 6, 8, 10, 12]

一层for循环简写：
一层 for 循环的简写格式是：（注意有中括号）
[ 对i的操作 for i in 列表 ]

它相当于：
for i in 列表:
    对i的操作
    
两层for循环
两层的for循环就是：
[对i的操作 for 单个元素 in 列表 for i in 单个元素]

y_list = ['assss','dvv']
[print(i) for y in y_list for i in y]

他类似于：
y_list = ['assss','dvv']
for y in y_list:
    for i in y:
        print(i) 

if 简写
True的逻辑 if 条件 else False的逻辑
举个例子：
y = 0
x = y+3 if y > 3 else y-1

for 与 if 的结合怎么简写
x = [1,2,3,4,5,6,7]
[print(i) for i in x if i > 3 ]
它会输出：4 5 6 7

注：使用简写的方式无法对 if 判断为 False 的对象执行操作。
所以它的模板是：
[判断为True的i的操作 for i in 列表 if i的判断 ]


匿名函数lambda
匿名函数的使用方法是：
lambda 参数: 表达式
x = 3
(lambda k: k+3)(x)
"""


"""
下面是list和str的互相转化的优雅的方法：
nums = ['1','2','3']
"".join(nums)
输出：'123'

需要注意的是该方法需要list中的元素为字符型，若是整型，则需要先转换为字符型后再转为str类型。
nums = [1,2,3]
nums_str = "".join( [str(x) for x in nums] )
print(num_str)
123

str转list
假设有一个名为test_str的str，转换后的list名为test_list
则转换方法：
test_list=list(test_str)
例子：
string = "123"
'_'.join(['a','b','c'])
'a_b_c'

"""

"""
下面做的都是错的，题目理解错了 是整个数字进行反转  而不是每一位用最大值去减
class Solution(object):
    def reverse(self,x):
        x_string = str(x)
        if x<0:
            #x_string.lstrip('-')
            x_string = x_string[1:]
        
        All_digit = []
        for item in x_string:
            All_digit.append(int(item))
        
        max_digit = max(All_digit)
        min_digit = min(All_digit)
        
        for i in range(len(All_digit)):
            All_digit[i] = str(max_digit - All_digit[i] + 1)
        
        
        if x<0:
            result = '-'+''.join(All_digit)
        else:
            result = ''.join(All_digit)
            
        return int(result)
"""



"""
python中默认是从前往后遍历列表的，有时候需要从后往前遍历。根据 range 函数的用法：
range(start, end[, step])

python中从后往前遍历列表的方法为：

lists = [0, 1, 2, 3, 4, 5]
# 输出 5, 4, 3, 2, 1, 0
for i in range(5, -1, -1):
    print(lists[i])
 
# 输出5, 4, 3
for i in range(5, 2, -1):
    print(lists[i])




a = [1,3,6,8,9]
print("通过下标逆序遍历1：")
for i in a[::-1]:
    print(i, end=" ")
print("\n通过下标逆序遍历2：")
for i in range(len(a)-1,-1,-1):
    print(a[i], end=" ")
print("\n通过reversed逆序遍历：")
for i in reversed(a):
    print(i, end=" ")

"""

"""
list删除元素的方法：
1.remove() remove()方法接受的是具体的值  remove() 的参数是具体的元素值，而不是索引，如果知道索引，
           如何使用 remove 删除该索引上的元素值，l.remove(l[1])
2.pop()  pop方法接受的是索引  无参情况下默认删除最后一个元素 （栈的特性）   pop()方法有返回值 返回删除的元素值
         list 的 append()（添加到尾部），pop()（从尾部弹出），成功地将 list 变成了 stack
3.del(I[0]) 
"""




"""
执行结果：通过
执行用时 :32 ms, 在所有 Python 提交中击败了35.31%的用户
内存消耗 :11.7 MB, 在所有 Python 提交中击败了29.54%的用户
class Solution(object):
    def reverse(self,x):
        if x == 0:
            return 0
        x_string = list(str(x))
        if x<0:
            x_string = x_string[1:]
        
        x_string = x_string[::-1]
        
        if x_string[0] == '0':
            x_string.pop(0)
        
        result = int(''.join(x_string))
        
        if x<0:
            result = -result
        
        if result>2**31-1 or result<-2**31:
            return 0
        return result
"""

"""
执行结果：通过
执行用时 :24 ms, 在所有 Python 提交中击败了78.44%的用户
内存消耗 :11.9 MB, 在所有 Python 提交中击败了7.62%的用户
"""

class Solution:
    def reverse(self, x):
        s = str(x)[::-1].rstrip('-')
        if int(s) < 2**31:
            if x >=0:
                return int(s)
            else:
                return 0-int(s)
        return  0