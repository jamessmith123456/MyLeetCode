# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:41:43 2019

@author: ZhuangChi
"""


"""
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。


说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3:
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4:
输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5:
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
"""

"""
python正则表达式：
Python 的 re 模块（Regular Expression 正则表达式）提供各种正则表达式的匹配操作，和 Perl 脚本的正则表达式功能类似，
使用这一内嵌于 Python 的语言工具，尽管不能满足所有复杂的匹配情况，但足够在绝大多数情况下能够有效地实现对复杂字符串的
分析并提取出相关信息。Python 会将正则表达式转化为字节码，利用 C 语言的匹配引擎进行深度优先的匹配。

表 1. 正则表达式元字符和语法
符号	说明	实例
.	
表示任意字符，如果说指定了 DOTALL 的标识，就表示包括新行在内的所有字符。
'abc'  >>>'a.c'   >>>结果为:'abc' 

^
表示字符串开头。	
'abc'  >>>'^abc'  >>>结果为:'abc'

$
表示字符串结尾。
'abc'  >>>'abc$'  >>>结果为:'abc'

*, +, ?	
'*'表示匹配前一个字符重复 0 次到无限次，'+'表示匹配前一个字符重复 1次到无限次，'?'表示匹配前一个字符重复 0 次到1次	
'abcccd'  >>>'abc*' >>>结果为:'abccc'
'abcccd' >>>'abc+'  >>>结果为:'abccc'
'abcccd' >>>'abc?'  >>>结果为:'abc'

*?, +?, ??
前面的*,+,?等都是贪婪匹配，也就是尽可能多匹配，后面加?号使其变成惰性匹配即非贪婪匹配	
'abc'  >>>'abc*?' >>>结果为:'ab'
'abc'  >>>'abc??' >>>结果为:'ab'
'abc'  >>>'abc+?' >>>结果为:'abc'

{m}
匹配前一个字符 m 次
'abcccd' >>>'abc{3}d'  >>>结果为:'abcccd'

{m,n}
匹配前一个字符 m 到 n 次
'abcccd'  >>> 'abc{2,3}d' >>>结果为:'abcccd'

{m,n}?
匹配前一个字符 m 到 n 次，并且取尽可能少的情况
'abccc'  >>> 'abc{2,3}?' >>>结果为:'abcc'


\
对特殊字符进行转义，或者是指定特殊序列	
'a.c' >>>'a\.c' >>> 结果为: 'a.c'

[]
表示一个字符集,所有特殊字符在其都失去特殊意义,只有： ^  -  ]  \   含有特殊含义
'abcd' >>>'a[bc]' >>>结果为:'ab'

|
或者，只匹配其中一个表达式 ，如果|没有被包括在()中，则它的范围是整个正则表达式
'abcd' >>>'abc|acd' >>>结果为:'abc'

( … )	被括起来的表达式作为一个分组. findall 在有组的情况下只显示组的内容
'a123d' >>>'a(123)d' >>>结果为:'123'

(?#...)	注释，忽略括号内的内容  特殊构建不作为分组	 'abc123' >>>'abc(?#fasd)123' >>>结果为:'abc123'
 
(?= … )	表达式’…’之前的字符串，特殊构建不作为分组	在字符串’ pythonretest ’中 (?=test) 会匹配’ pythonre ’

(?!...)	后面不跟表达式’…’的字符串，特殊构建不作为分组	如果’ pythonre ’后面不是字符串’ test ’，那么 (?!test) 会匹配’ pythonre ’

(?<= … )	跟在表达式’…’后面的字符串符合括号之后的正则表达式，特殊构建不作为分组则表达式’ (?<=abc)def ’会在’ abcdef ’中匹配’ def ’

（?:）	取消优先打印分组的内容	'abc' >>>'(?:a)(b)' >>>结果为'[b]'

?P<>	指定Key	'abc' >>>'(?P<n1>a)>>>结果为:groupdict{n1:a}




正则表达式特殊序列
特殊表达式序列	说明
\A	只在字符串开头进行匹配。
\b	匹配位于开头或者结尾的空字符串
\B	匹配不位于开头或者结尾的空字符串
\d	匹配任意十进制数，相当于 [0-9]
\D	匹配任意非数字字符，相当于 [^0-9]
\s	匹配任意空白字符，相当于 [ \t\n\r\f\v]
\S	匹配任意非空白字符，相当于 [^ \t\n\r\f\v]
\w	匹配任意数字和字母，相当于 [a-zA-Z0-9_]
\W	匹配任意非数字和字母的字符，相当于 [^a-zA-Z0-9_]
\Z	只在字符串结尾进行匹配



上面提到贪婪匹配和非贪婪匹配请看例子：
import re
#贪婪
ret_greed= re.findall(r'a(\d+)','a23b')
print(ret_greed)
#非贪婪
ret_no_greed= re.findall(r'a(\d+?)','a23b')
print(ret_no_greed)
 
['23']
['2']
由于贪婪匹配为尽可能的多匹配所以结果为23 ，有人好奇了，findall是什么鬼 ，请耐心往下看：



re模块
正则表达式使用反斜杠” \ “来代表特殊形式或用作转义字符，这里跟Python的语法冲突，因此，Python用” \\ “表示正则表达
式中的” \ “，因为正则表达式中如果要匹配” \ “，需要用\来转义，变成” \ “，而Python语法中又需要对字符串中每一个\进行转义，
所以就变成了” \\ “。

上面的写法是不是觉得很麻烦，为了使正则表达式具有更好的可读性，Python特别设计了原始字符串(raw string)，需要提醒你的是，
在写文件路径的时候就不要使用raw string了，这里存在陷阱。raw string就是用’r’作为字符串的前缀，如 r”\n”：表示两个字
符”\”和”n”，而不是换行符了。Python中写正则表达式时推荐使用这种形式。

1、 re.findall(pattern, string[, flags]):
方法能够以列表的形式返回能匹配的子串。先看简单的例子：
import re
a = 'one1two2three3four4'
ret = re.findall(r'(\d+)',a)
print(ret)
['1', '2', '3', '4']
从上面的例子可以看出返回的值是个列表，并且返回字符串中所有匹配的字符串。

2、re.finditer(pattern, string[, flags])
搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。 请看例子：
import re
  
p = re.compile(r'\d+')
for m in p.finditer('one1two2three3four4'):
    print m.group(),
### output ###
# 1 2 3 4　



正则表达式re.findall()与re.finditer()的区别
re.findall()如果可以匹配返回的是一个列表，re.finditer()返回的是一个迭代器，需要对其进行遍历，才能获取数据。
import re
def main():
    content = '八神是我的好朋友，他的手机电话是18381665314， 他的QQ是1911966573， 他女朋友的电话是18381665315, QQ:1911966574 ！'
    regex = re.compile(r'\d{11}')
    tels = regex.findall(content)
    print(tels)

if __name__ == '__main__':
    main()
# ['18381665314', '18381665315']

以上的findall()代码，用以下的finditer()代码，输出的效果是等价的.
import re


def main():
    content = '八神是我的好朋友，他的手机电话是18381665314， 他的QQ是1911966573， 他女朋友的电话是18381665315, QQ:1911966574 ！'
    regex = re.compile(r'\d{11}')
    tels_obj = regex.finditer(content)
    tels_list = []
    for tel in tels_obj:
        tels_list.append(tel.group())
    print(tels_list)


if __name__ == '__main__':
    main()
# ['18381665314', '18381665315']






3、re.match和re.search
Python提供了两种不同的原始操作：match和search。match是从字符串的起点开始做匹配，而search（perl默认）是从字符串做任意
匹配。看个例子:
import re
 
ret_match= re.match("c","abcde");     #从字符串开头匹配，匹配到返回match的对象，匹配不到返回None
if(ret_match):
    print("ret_match:"+ret_match.group());
else:
    print("ret_match:None");
 
ret_search = re.search("c","abcde"); #扫描整个字符串返回第一个匹配到的元素并结束，匹配不到返回None
if(ret_search):
    print("ret_search:"+ret_search.group());
ret_match:None
ret_search:c

注意： for i in ret_match.match("abcde")  是不可以的 ，返回的不是迭代器！而是直接 (ret_match.match("abcde")).group()
同理，search方法也是的   (ret_match.search("abcde")).group()



re.match对象拥有以下方法：
import re
a = "123abc456"
ret_match= re.match("a","abcde");
print(ret_match.group())  #返回返回被 RE 匹配的字符串
print(ret_match.start())  #返回匹配开始的位置
print(ret_match.end())    #返回匹配结束的位置
print(ret_match.span())   #返回一个元组包含匹配 (开始,结束) 的位置
其中group()方法可以指定组号，如果组号不存在则返回indexError异常看如下例子：
import re
a = "123abc456"
re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0)   #123abc456,返回整体默认返回group(0) 返回所有group匹配到的字符串
re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1)   #123 只返回第一个group匹配到的字符串
re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2)   #abc 只返回第二个group匹配到的字符串
re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3)   #456 只返回第三个group匹配到的字符串





re.sub和re.subn
import  re
#sub
ret_sub = re.sub(r'(one|two|three)','ok','one word two words three words') 
#ok word ok words ok words

#subn
import  re
ret_subn = re.subn(r'(one|two|three)','ok','one word two words three words') 
#('ok word ok words ok words', 3) 3,表示替换的次数





re.split(pattern, string, maxsplit=0)
通过正则表达式将字符串分离。如果用括号将正则表达式括起来，那么匹配的字符串也会被列入到list中返回。
maxsplit是分离的次数，maxsplit=1分离一次，默认为0，不限制次数。看一下例子：
import re
ret = re.split('\d+','one1two2three3four4') 
#匹配到1的时候结果为'one'和'two2three3four4'，匹配到2的时候结果为'one', 'two'和'three3four4', 所以结果为：
####output####
['one', 'two', 'three', 'four', '']







re.compile(strPattern[, flag])
这个方法是Pattern类的工厂方法，用于将字符串形式的正则表达式编译为Pattern对象。
第二个参数flag是匹配模式，取值可以使用按位或运算符’|’表示同时生效，比如re.I | re.M。
另外，你也可以在regex字符串中指定模式，比如re.compile(‘pattern’, re.I | re.M)与re.compile(‘(?im)pattern’)是等价的。
可选值有：
re.I(IGNORECASE): 忽略大小写（括号内是完整写法，下同）
re.M(MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
re.S(DOTALL): 点任意匹配模式，改变'.'的行为
re.L(LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
re.U(UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
re.X(VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。

import re
text = "JGood is a handsome boy, he is cool, clever, and so on..."
regex = re.compile(r'\w*oo\w*')
print(regex.findall(text))
 
['JGood', 'cool']
"""













给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3:
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4:
输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5:
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false


字符串分割函数：str.split(s,num)[n]   
其中s表示指定的分隔符 不写的话默认是空格' '
num表示分割次数，会将字符串分割成num+1个子字符串 并且每一个子字符串可以赋值给新的变量
[n]表示选取第n个分片，n表示返回的list中元素下标 从0开始
temp = 'abcdefghijklmn'

temp.split('de',0)
['abcdefghijklmn']

temp.split('de',1)
['abc', 'fghijklmn']

temp.split('de',2)
['abc', 'fghijklmn']

temp.split('de',3)
['abc', 'fghijklmn']

temp.split('de',3)[0]
'abc'

temp.split('de',3)[1]
'fghijklmn'

temp = 'abcdebcadecbade'
temp.split('de')
['abc', 'bca', 'cba', '']  这里最后多个''是因为'de'在最后  如果不是在最后的话，应该就不会有个''
比如：
temp.split('d')
['abc', 'ebca', 'ecba', 'e']

temp.split('de',0)
['abcdebcadecbade']

temp.split('de',1)
['abc', 'bcadecbade']

temp.split('de',2)
['abc', 'bca', 'cbade']



拓展：
import os
os.path.split('PATH')


class Solution(object):
    def isMatch(self,s,p):  
        #s中凡是重复字符的部分 都可以缩写为'.*'  这是个很重要的思路！劳资牛逼!
        s_unique = []
        s_unique_count = []
        for i in range(len(s)):
            if i==0:
                s_unique.append(s[i])
                s_unique_count.append(0)
            else:
                if s[i] != s_unique[-1]:
                    s_unique.append(i)
                    s_unique_count.append(0)
                if s[i] == s_unique[-1]:
                    s_unique_count[-1] = 1
                
        
        #得到的p_list中所有的*都与前一个字符合并为list的一个元素了
        p_list = list(p)
        p_list_new = []
        for i in range(len(p_list)):
            if i==0:
                p_list_new.append(p_list[i])
            else:
                if p_list[i] == '*':
                   p_list_new[-1] = p_list_new[-1]+p_list[i]
                else:
                   p_list_new.append(p_list[i])
       
        logo = False
        for i in range(len(s_unique)):
            for j in p_list_new:
                if len(j)==1:
                    if j == s_unique[i] and s_unique_count[i] == 0:
                        logo = True
                    if j != s_unique[i]:
                        logo = False
                    if j == s_unique[i] and s_unique_count[i] == 1:
                        logo = False
                        
                    if j == '.' and s_unique_count[i] == 0:
                        logo = True
                    if j == '.' and s_unique_count[i] == 1:
                        logo = False
                
                if len(j)==2:
                    if j[0]==s_unique[i]:
                        logo = True
                    else:
                        logo = False
                
        return logo        



