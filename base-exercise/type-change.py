# -*- coding: utf-8 -*
"""
    @Time:2019-12-27 15:42
    @Version:1.0.0
    @Author:Yincheats
    @Description:类型转换
"""

"""
    python是一门动态语言，声明变量的时候不需要声明变量类型
    python中的四种基本类型 str,int,bool,float都可进行类型转换
    int(x)   把x转换成整数
    float(x) 把x转换成浮点数
    str(x)   把x转换成字符串
    bool(x)  把x转换成bool值 
    注意：对特定变量类型进行操作时，如果这个操作的类型与之不匹配的，会产生错误
    例如 ： print("my num is %d " % '123') 这里的123因改为int
           print(""+bool(0))
    
    以下等式的bool结果均为true：
    int('123') == 123
    float('3.3') == 3.3
    str(111) == '111'
    bool(0) == False
    
    对于以下情况 bool()结果均为false 
    为0的数字，包括0，0.0
    空字符串，包括''，""
    表示空值的None
    空集合，包括()，[]，{}
    bool()
    
    python 中的None 相当于java中的null
    
    
"""
print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool(""))
print(bool(None))
noneArr = []
print(bool(noneArr))
noneArr = ()
print(bool(noneArr))
noneArr = {}
print(bool(noneArr))
