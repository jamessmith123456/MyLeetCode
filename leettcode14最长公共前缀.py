# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:31:13 2019

@author: ZhuangChi
"""

编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。








"""
执行结果：通过
执行用时 :36 ms, 在所有 Python 提交中击败了22.84%的用户
内存消耗 :11.8 MB, 在所有 Python 提交中击败了33.64%的用户
"""

class Solution(object):
    def longestCommonPrefix(self,strs):
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        
        first = strs[0]
        second = strs[1]
        
        temp = ""
        for i in range(min(len(first),len(second))):
            if first[i] == second[i]:
                temp += first[i]
            else:
                break
        result = temp
        strs.remove(first)
        strs.remove(second)
        #或者按索引进行删除strs.pop(0) strs.pop(1)  或者del()
        
        while strs!=[]:
            result = ""
            new_str = strs[0]
            for i in range(min(len(temp),len(new_str))):
                if temp[i]==new_str[i]:
                    result += temp[i]
                else:
                    break
            temp = result
            strs.remove(new_str)
        
        return result
            






"""
下面是别人的两种解法：
"""
"""
python中map()函数的用法：
python中的map()函数是一个内置的高阶函数，一般用法是map(function, iterable)。需要传入一个函数，
这个函数可以是内置的，也可以是自己定义，也可以是匿名函数。第二个参数是一个可迭代对象，如列表，字符串等等。
返回的是一个map对象，注意不是列表不能直接输出，可以通过for循环或者list()来显示。（python2返回的是列表）
不多说，直接上代码，一看就明白了。
def square(x):
    return x*x
a=map(square,[1,2,3]) 
print(a)        
#输出为<map object at 0x0033CFB0>   可以看出map返回的实际上是一个map对象
print(list(a))  
#输出为[1, 4, 9]   通过list（）方式 显示出来   

#也可以通过for循环来取出内容
ls=[]
for i in a:
    ls.append(i)
print(ls)
#输出为[1, 4, 9]

其实map,不止能传入一个可迭代对象做为参数。也可以传入两个。看例子就可以体会到这用法
ls1='ABC'
ls2='abc'
print(list(map(lambda x,y:x+y,ls1,ls2)))
#['Aa', 'Bb', 'Cc']

若是传入的多个可迭代对象长度不相同，则按最短的长度进行处理(这是针对python3的)。具体用法如下：
ls1='ABC'
ls2='ab'
print(list(map(lambda x,y:x+y,ls1,ls2)))
#['Aa', 'Bb']

"""

"""
set （集合）。集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。集合对象还支持 union（联合），
intersection（交），difference（差）和 sysmmetric difference（对称差集）等数学运算。

大括号或 set() 函数可以用来创建集合。　
set集合类需要的参数必须是迭代器类型的，如：序列、字典等，然后转换成无序不重复的元素集。由于集合是不重复的，
所以可以对字符串、列表、元组进行去重操作。

创建空集合
s=set()  输出：set()

元组：set(()) set()
列表：set([]) set()
字典：set({}) set()

创建非空集合
即列表，元组，字典不在是空值，举两个例子
s1=set([1,2,3,4])  输出：{1，2，3，4}
s3=set({'a':2,'b':3,'c':4})  输出：{'c','a','b'}  
注：字典转set集合，需要注意的是，只取了字典的key，相当于将字典中的dict.keys()列表转成set集合

集合的操作
集合添加
集合的添加有两种方式，分别是add和update。但是它们在添加元素时是由区别的：

add()方法
把要传入的元素作为一个整体添加到集合中，如：

s=set('one') 输出：{'e', 'o', 'n'}
s.add('two') 输出：{'e', 'two', 'o', 'n'}

update()方法
是把要传入的元素拆分成单个字符，存于集合中，并去掉重复的字符。可以一次添加多个值，如：
s=set('one') 输出：{'e', 'o', 'n'}
s.update('two') 输出：{'e', 'n', 't', 'w', 'o'}


集合删除
集合的删除操作使用的方法跟列表是一样的，使用的也是remove方法。如：

setVar.remove(element)
setVar :为一个set类型的变量
element :表示要查找并删除的元素
函数作用：
在集合setVar中查找element元素，如果存在则删除；如果没找到，则报错。
s=set('one') 输出：{'e', 'o', 'n'}
s.remove('e') 输出：{'n', 'o'}

setVar.discard(element)
setVar :为一个set类型的变量
element :表示要查找并删除的元素
函数作用：
在集合setVar中查找element元素，如果存在则删除；如果没找到，则什么也不做。
sList
set([1, 2, 3, 4, 5])
sList.discard(1)
sList
set([2, 3, 4, 5])




s.pop()
s：为set类型的变量
函数作用：
删除并返回set类型的s中的一个不确定的元素，如果为空引发KeyError错误。
额,我的理解是随便删除？？（我实际测试了一下，每次删除的都是第一个）
sList
set([2, 3, 4, 5])
sList.pop()



s.clear()
s：set类型的变量
函数作用：
清空s集合中的所有元素
sList  输出：set([3, 4, 5])
sList.clear()
sList 输出：set([])

集合的遍历
集合的遍历跟序列的遍历方法完全一样。
s=set('one') 输出：{'e', 'o', 'n'}
for i in s:
    print(i)
e
o
n

for idex,i in enumerate(s):
        print (idex,i)
... ... 
0 e
1 o
2 n

集合其他方法
函数	说明
len(s)	                     set 的长度
x in s	                     测试 x 是否是 s 的成员
x not in s	                 测试 x 是否不是 s 的成员
s.issubset(t)	             测试是否 s 中的每一个元素都在 t 中
s.issuperset(t)	             测试是否 t 中的每一个元素都在 s 中
s.union(t)	                 返回一个新的 set 包含 s 和 t 中的每一个元素
s.intersection(t)	         返回一个新的 set 包含 s 和 t 中的公共元素
s.difference(t)	             返回一个新的 set 包含 s 中有但是 t 中没有的元素
s.symmetric_difference(t)	 返回一个新的 set 包含 s 和 t 中不重复的元素
s.copy()	                 返回 set “s”的一个浅复制





集合的一些操作符
既然是集合，那就会遵循集合的一些操作方法，如求交集、并集、差集等。

交集
Python中求集合的交集使用的符号是“&”，返回连个集合的共同元素的集合，即集合的交集。
st1 = set('python')  输出：set(['h', 'o', 'n', 'p', 't', 'y'])
st2 = set('htc') 输出：set(['h', 'c', 't'])
st1 & st2 输出：set(['h', 't'])

并集（合集）
Python中求集合的并集用的是符号“|”，返回的是两个集合所有的并去掉重复的元素的集合。
st1 = set('python')  输出：set(['h', 'o', 'n', 'p', 't', 'y'])
st3 = set('two') 输出：set(['o', 't', 'w'])
st1 | st3 输出：set(['p', 't', 'w', 'y', 'h', 'o', 'n'])

差集
Python中差集使用的符号是减号“-”。
st1 输出：set(['1', '3', '2', '5', '4', '7', '6'])
st2 = set('4589') 输出：set(['9', '8', '5', '4'])
st1 - st2 输出：set(['1', '3', '2', '7', '6'])

集合的不同
查看两个集合的不同之处，使用的difference函数，等价于差集。如：
s1.difference(s3) 
这种不同指的是集合s3相对于集合s1，不同的地方，也就是所有在集合s1中，而不再集合s2中的的元素组成的新集合。
s1 输出：set([1, 2, 3, 4, 5])
s2 输出：set([1, 2, 3, 4]
s1.difference(s2) 输出：set([5])
s3 输出：set(['1', '8', '9', '5'])
s1.difference(s3) 输出：set([1, 2, 3, 4, 5])  靠，吗的，这里面s3中的是字符串，而不是数字 '1'和1不一样，我说咋这么难理解..


集合的范围判断
集合可以使用大于（>）、小于（<）、大于等于（>=）、小于等于（<=）、等于（==）、不等于（！=）来判断某个集合是否完全包含
于另一个集合，也可以使用子父集判断函数。
定义三个集合s1，s2，s3：
s1＝set([1, 2, 3, 4, 5])
s2＝set([1, 2, 3, 4])
s3＝set(['1', '8', '9', '5'])


大于（>）或大于等于（>=）
s1 > s2
True
s1 > s3
False
 s1 >= s2
True
表示左边集合是否完全包含右边集合，如集合s1是否完全包含集合s2。


小于（<）或 小于等于（<=）
s2 < s1
True
s1 < s3
False
s3 < s1
False
表示左边的集合是否完全包含于右边的集合，如集合s1是否完全包含于集合s2。


等于（==）、不等于（！=）
s1 == s2
False
s2 == s3
False
s1 != s2
True
判断两个集合是否完全相同。


不可变集合frozenset
Python中还有一种不可改变的集合，那就是frozenset，不像set集合，可以增加删除集合中的元素，该集合中的内容是不可改变的，
类似于字符串、元组。
f = frozenset() 输出：frozenset([])
f = frozenset('asdf') 输出：frozenset(['a', 's', 'd', 'f'])
f = frozenset([1,2,3,4]) 输出：frozenset([1, 2, 3, 4])
f = frozenset((1,2,3,4)) 输出：frozenset([1, 2, 3, 4])
f = frozenset({1:2, 'a':2, 'c':3}) 输出：frozenset(['a', 1, 'c'])
如果试图改变不可变集合中的元素，就会报AttributeError错误。
不可变集合，除了内容不能更改外，其他功能及操作跟可变集合set一样。
"""



"""
zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表。具体意思不好用文字来表述，直接看示例：
1.示例1：
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
xyz = zip(x, y, z)
print xyz
运行的结果是：
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]


2.示例2：
x = [1, 2, 3]
y = [4, 5, 6, 7]
xy = zip(x, y)
print xy
运行的结果是：
[(1, 4), (2, 5), (3, 6)]

3.示例3：
x = [1, 2, 3]
x = zip(x)
print x
运行的结果是：
[(1,), (2,), (3,)]
从这个结果可以看出zip函数在只有一个参数时运作的方式。

4.示例4：
x = zip()
print x
运行的结果是：
[]
从这个结果可以看出zip函数在没有参数时运作的方式。



5.示例5：
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
xyz = zip(x, y, z)
u = zip(*xyz)
print u
运行的结果是：
[(1, 2, 3), (4, 5, 6), (7, 8, 9)]

一般认为这是一个unzip的过程，它的运行机制是这样的：
在运行zip(*xyz)之前，xyz的值是：[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
那么，zip(*xyz) 等价于 zip((1, 4, 7), (2, 5, 8), (3, 6, 9))
所以，运行结果是：[(1, 2, 3), (4, 5, 6), (7, 8, 9)]
注：在函数调用中使用*list/tuple的方式表示将list/tuple分开，作为位置参数传递给对应函数
（前提是对应函数支持不定个数的位置参数）


这里额外补充python的*号的用法
传递实参和定义形参（所谓实参就是调用函数时传入的参数，形参则是定义函数是定义的参数）的时候，你还可以使用两个特殊的
语法：``*`` ** 。

调用函数时使用* **

test(*args)：* 的作用其实就是把序列 args 中的每个元素，当作位置参数传进去。比如上面这个代码，如果 args 等于 (1,2,3) ，
那么这个代码就等价于 test(1, 2, 3) 。
test(**kwargs)：** 的作用则是把字典 kwargs 变成关键字参数传递。比如上面这个代码，如果 kwargs 等于 
{'a':1,'b':2,'c':3} ，那这个代码就等价于 test(a=1,b=2,c=3) 。


定义函数参数时使用* **
def test(*args):
    ...定义函数参数时 * 的含义又要有所不同，在这里 *args 表示把传进来的位置参数都装在元组 args 里面。比如说上面这个函数，
    调用 test(1, 2, 3) 的话， args 的值就是 (1, 2, 3) 。:

def test(**kwargs):
    ...类似的， ** 就是针对关键字参数和字典的了。 调用 test(a=1,b=2,c=3) 的话， kwargs 的值就是 {'a':1,'b':2,'c':3}了。

普通的参数定义和传递方式和 * 们都可以和平共处，不过显然 * 必须放在所有位置参数的最后，而 ** 则必须放在所有关键字参数的
最后，否则就要产生歧义了。






6.示例6：
x = [1, 2, 3]
r = zip(* [x] * 3)
print r
运行的结果是：
[(1, 1, 1), (2, 2, 2), (3, 3, 3)]
它的运行机制是这样的：
[x]生成一个列表的列表，它只有一个元素x
[x] * 3生成一个列表的列表，它有3个元素，[x, x, x]
zip(* [x] * 3)的意思就明确了，zip(x, x, x)
"""
python两种让你拍大腿的解法，时间复杂度你想象不到，短小精悍。 
1、利用python的max()和min()，在Python里字符串是可以比较的，按照ascII值排，举例abb， aba，abac，
最大为abb，最小为aba。所以只需要比较最大最小的公共前缀就是整个数组的公共前缀

    def longestCommonPrefix(self, strs):
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i,x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1

2、利用python的zip函数，把str看成list然后把输入看成二维数组，左对齐纵向压缩，然后把每项利用集合去重，
之后遍历list中找到元素长度大于1之前的就是公共前缀

    def longestCommonPrefix(self, strs):
        if not strs: return ""
        ss = list(map(set, zip(*strs)))
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res             