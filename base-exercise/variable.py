# -*- coding: utf-8 -*
"""
    @Time:2019-12-26 14:41
    @Version:1.0.0
    @Author:Yincheats
    @Description:变量
"""

"""
    python变量的基本类型
    字符串 ： 单引号或双引号
    整数 
    浮点数：小数
    bool(布尔)：逻辑运算符 True 和 False
"""
# 输出字符串variable
_name = "Crossin"
_type = 'Room'
print(_name, _type)
# 输出整数
int_a = 3
int_b = 5
print(int_a, int_b, int_a * int_b)
# 输出float
float_a = 0.9
float_b = 0.22
print(float_a, float_b, float_a * float_b)
# bool布尔
"""
    python中的逻辑关系运算符：
    大于，小于 >,< 
    大于等于，小于等于 >=,<=
    不等于，等于 !=,==
    
    “与” :  and
    “或” :  or
    “非” :  not
    
"""
int_a1 = 1
int_a2 = 2
print(int_a1 and int_a2)

"""
    python变量命名规则
    1 第一个字符必须是字母或者下划线“_”
    2 剩下的部分可以是字母，数字，下划线
    3 python变量命名对大小写敏感，即 value和Value为两个不同的变量
    
    举几个例子：
    i = 1
    __my_name = 2
    name_23 = 3
    a1b2_c3 = 4
    
    几个不正确的例子：
    2things=1
    this is spaced out=2
    my-name=3
"""
a = 1
a += 3
# 注意这里的a+=3不能成为一个变量
print(a)
# 关于bool
bool_a = True
bool_b = not a

print(1<2 and bool_b==True) # False