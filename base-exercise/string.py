# -*- coding: utf-8 -*
"""
    @Time:2019-12-27 10:31
    @Version:1.0.0
    @Author:Yincheats
    @Description:字符串&字符串格式化
"""

"""
    1. 单引号 '' 和 双引号 "" 对于一个字符串本身效果是一样的
    2. 单双引号可以区分不同的字符串 eg:"You are a 'BAD' man " 反之亦然
    3. 转义字符 
        \'表示单引号，\"表示双引号
        'I\'m a \"good\" teacher' = 'I'm a "good" teacher'
        '\' 被称作转译字符，除了用来表示引号，还有比如用
        \\表示字符串中的\
        \n表示字符串中的换行
"""

"""
    输出以下字符
    1.He said, "I'm yours!"
    2.\\_v_//
    3.Stay hungry,
      stay foolish.
             -- Steve Jobs
    4.  *
        ***
        *****
        ***
        *
"""

# 1.He said, "I'm yours!"
str1 = "He said \"I\'m yours\" "
print(str1)
# 2.\\_v_//
str2 = "\\\\_v_//"
print(str2)
"""
3.
    Stay hungry,
    stay foolish.
        -- Steve Jobs
"""
str3 = "Stay hungry,\nstay foolish.\n    -- SteveJobs"
print(str3)
"""
4.
    *
    ***
    *****
    ***
    *
"""
str4 = "*\n***\n*****\n***\n*"
print(str4)

"""
字符串格式化
    eg:str1="a" str2="b" int3=0 num4=1
    1. 连接输出
        print(str1+str2) = "ab"
    2. 转换链接输出
        print(str1+str(int3))="a0"
    3. %格式化
        num = 27 代替整数 %d
        print("My age is %d' % num)
        代替小数 %f
        print('Price is %f' % 4.99)
        保留两位小数 %.2f
        print('Price is %.2f' % 4.99)
        代替字符串输出 %s
        name = 'Crossin'
        print('%s is a good teacher.' % name)
        当字符串中的多个变量需要进行格式化
        print "%s's score is %d" % ('Mike', 87)
        
        
"""
num = 27
str5 = 'My age is %d' % num
str6 = 'Price is %f' % 4.99
print(str5)
print(str6)
print('Price is %.2f' % 4.99)
name = 'Crossin'
print('%s is a good teacher.' % name)
strtest = "%s's score is %d" % ('Mike', 87)
print(strtest)