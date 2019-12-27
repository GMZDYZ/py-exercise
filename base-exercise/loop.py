# -*- coding: utf-8 -*
"""
    @Time:2019-12-26 17:07
    @Version:1.0.0
    @Author:Yincheats
    @Description:循环
"""

"""
    打印圣诞树
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * *     
      ***** 
      ***** 
      ***** 
"""

for i in range(0, 5):
    for a in range(i + 1, 5):
        print(" ", end=" ")
    for b in range(0, (i + 1)):
        print("*", end=" ")
    for c in range(0, i + 1):
        if c != 0:
            print("*", end=" ")
    if i >= 4:
        for d in range(0, 3):
            print()
            for e in range(0, 3):
                print(" ", end=" ")
            print("*****", end=" ")
    print()
