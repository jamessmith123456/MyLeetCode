# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 09:28:45 2019

@author: ZhuangChi
1.两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。   
"""

#####################################第1种写法#################################
"""
#按最简单的方法 就是 for i in range(len(number)):...然后就这样带下标进行遍历 很不优雅 下面这种写法优雅一点
class Solution(object):
    def twoSum(self,number,target):
        for id_A,item_A in enumerate(number):
            for id_B,item_B in enumerate(number):
                if id_A!=id_B and (item_A+item_B)==target:
                    return [id_A,id_B]



if __name__ == '__main__':
    number = [2,7,11,15]
    target = 9
    solution = Solution() # Java里面才有new这种写法 python不需要 solution = new Solution()
    result = solution.twoSum(number,target)
#上面的这种写法 耗时24ms/16ms/12ms 当提交后用一个很长的整数数组(12599个元素)进行测试时 超出时间限制!
"""


#####################################第2种写法#################################
"""
查看别人给出的Java解 使用hash表来减少时间 我感觉hash表(Java中的Map<>)有点儿像python中的字典?
学习一下python中字典的几种用法:
创建一个空字典
empty_dict = dict() 
print(empty_dict)
输出：[]

用**kwargs可变参数传入关键字创建字典
a = dict(one=1,two=2,three=3) 
print(a)
输出：{'one': 1, 'two': 2, 'three': 3}
    
传入可迭代对象
b = dict(zip(['one','two','three'],[1,2,3]))
print(list(zip(['one','two','three'],[1,2,3])))
print(b)
输出：[('one',1),('two',2),('three',3)]
输出：{'one':1,'two':2,'three':3}

传入可迭代对象 
c = dict([('one', 1), ('two', 2), ('three', 3)])
print(c)
输出：{'one':1,'two':2,'three':3}
    
c1 = dict([('one', 1), ('two', 2), ('three', 3),('three', 4),('three', 5)])
print(c1)#如果键有重复，其值为最后重复项的值。 
输出：{'one':1,'two':2,'three':5}

传入映射对象，字典创建字典  
d = dict({'one': 1, 'two': 2, 'three': 3}) 
print(d) 
输出：{'one':1,'two':2,'three':3}

print(a == b == c == d)
输出：true


#字典中添加元素
d = {'a': 1}
d.update(b=2)  #也可以 d.update({‘b’: 2})
print(d)
{'a': 1, 'b': 2}

d.update(c=3, d=4)    **kwargs参数
print(d)
{'a': 1, 'c': 3, 'b': 2, 'd': 4}

d.update({'f': 6, 'g': 7})  #即d.update(字典)  可映射对象
print(d)
{'a': 1, 'c': 3, 'b': 2, 'd': 4, 'g': 7, 'f': 6}


a = dict()
a.update([('a',1),('b',2)])  可迭代对象
print(a)
{'a':1,'b':2}

#字典中删除元素
pop(key)
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
x.pop(1)   # pop(key)
print(x)
{0: 0, 2: 1, 3: 4, 4: 3}

del dict[key]
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
del x[1]  #注意字典的引用：a[key]
print(x)
{0: 0, 2: 1, 3: 4, 4: 3}

方法
def remove_key(d, key):
    r = dict(d) 这里就是利用映射对象来创建字典(即字典创建字典)
    del r[key]
    return r
 
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(remove_key(x, 1))
print(x)

{0: 0, 2: 1, 3: 4, 4: 3}
{0: 0, 1: 2, 2: 1, 3: 4, 4: 3}


判断字典中是否含有某个元素的方法
a = dict(a=1,b=2)

'a' in a
True   判断a中是否存在某个键值

'1' in a.values()
True  判断a中是否存在某个值(不是key)


类似于list数据结构中的enumerate()
字典中的用法：
for key, value in my_dict.items():
    print(key,value)
    
    
总结：创建字典三种方式：1.传入**kwargs参数 2.传入可迭代对象 3.传入映射对象 也就是字典
      增加或删除三种方式：1.update(可使用**kwargs参数、可迭代对象、映射对象) 2.pop\del 3.方法(好处是不会改变原字典) 
      查看字典：1.in /not in(针对list也是一样的) 2.a.values()
"""


"""
根据字典的key求value很好求
但是根据value求key不能直接求得
1. print([for k,v in a.items() if v==1])

2.print(list(a.keys())[list(a.values()).index(1)])

3.new_a = {v:k for k,v in a.items()}
print(new_a[1])

"""
"""
class Solution(object):
    def twoSum(self,number,target):
        hashmap = dict()
        for id_A,item_A in enumerate(number):
            #先检测
            if (target-item_A) in hashmap.values():
                #该怎么从hashmap这个字典中根据值获取相应的键呢？
                return [id_A,list(hashmap.keys())[list(hashmap.values()).index(target-item_A)]]
            #在更新
            #hashmap.update(id_A=item_A) #这样写是不行的 会把id_A作为key键 而不是id_A所对应的1,2,3,4,5... 尝试用eval解决 不行
            #灵机一动 这里是采用了**kwargs可变参数来更新 试试可迭代对象 可以！
            #靠 ，这里纯粹是给自己找麻烦.... hashmap[id_A]=item_A 这样也是可以的...
            hashmap.update([(id_A,item_A)])
            #print(hashmap.items())

if __name__ == '__main__':
    number = [2,7,11,15]
    target = 9
    solution = Solution()
    result = solution.twoSum(number,target)
"""           
#执行结果：通过
#执行用时 :476 ms, 在所有 Python 提交中击败了54.96%的用户
#内存消耗 :12.9 MB, 在所有 Python 提交中击败了20.67%的用户




####################################官方解法1####################################
"""
#实际上面的第2种解法,就是我在看了Java最优解之后仿写的
#实现的并不好！本质上还是进行了多次循环！所以浪费了很多时间

class Solution(object):
    def twoSum(self,number,target):
        new_number = {v:k for k,v in enumerate(number)} #首先开辟O(n)的存储空间 来存储map
        
        for id_A,item_A in enumerate(number):
            if new_number.get(target-item_A)!=None and new_number.get(target-item_A)!=id_A:
                return [id_A,new_number.get(target-item_A)]
#执行结果：通过
#执行用时 :52 ms, 在所有 Python 提交中击败了80.25%的用户
#内存消耗 :13.4 MB, 在所有 Python 提交中击败了5.01%的用户        
"""

"""
#一遍字典模拟哈希
class Solution(object):
    def twoSum(self,number,target):
        new_number = dict()
        for id_A,item_A in enumerate(number):
            if new_number.get(target-item_A)!=None:
                return [id_A,new_number.get(target-item_A)]
            #new_number.update([(item_A,id_A)])
            new_number[item_A]=id_A
#执行结果：通过
#执行用时 :48 ms, 在所有 Python 提交中击败了87.85%的用户
#内存消耗 :13.2 MB, 在所有 Python 提交中击败了8.23%的用户
"""