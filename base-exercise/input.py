# -*- coding: utf-8 -*
"""
    @Time:2019-12-26 14:32
    @Version:1.0.0
    @Author:Yincheats
    @Description:input输入
"""
from pip._vendor.distlib.compat import raw_input

print("who do you think I am?")
answer = input()
print("your answer :"+answer)
print("bye bye")

# raw_input()
print("this is raw_input()")
raw_input()
print("what`s difference between input() and raw_input() ?")
"""
    raw_input() 和 input()的区别
    在python2中 raw_input是接收字符串的 input()是接收数字的，input返回的数字类型为（float,int）
    在python3.x中raw_input( )和input( )进行了整合，
    去除了raw_input( )，仅保留了input( )函数，其接收任意任性输入
    将所有输入默认为字符串处理，并返回字符串类型。
"""