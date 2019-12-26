# -*- coding: utf-8 -*
"""
    @Time:2019-12-26 15:02
    @Version:1.0.0
    @Author:Yincheats
    @Description:猜数字
"""
from random import randint

targetNum = randint(1, 10)
print("guess a num for your glory 😡")
int_yourNum = int(input())
while int_yourNum != targetNum:
    if int_yourNum < targetNum:
        print("less;num:", int_yourNum, "😂")
    if int_yourNum > targetNum:
        print("bigger;num:", int_yourNum)
    print("let`s try again,input a num", "😂")
    int_yourNum = int(input())
    continue
print("good job! you guessed", "👍👍👍")
