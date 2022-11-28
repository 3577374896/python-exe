#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-11-24 16:14:43
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


from turtle import *
from random import *
from math import *
import turtle as t
import random as r
def tree(n,l):
    pd()#下笔
    #阴影效果
    t = cos(radians(heading()+45))/8+0.25
    pencolor(t,t,t)
    pensize(n/3)
    forward(l)#画树枝
 
    if n>0:
        b = random()*15+10 #右分支偏转角度
        c = random()*15+10 #左分支偏转角度
        d = l*(random()*0.25+0.7) #下一个分支的长度
        #右转一定角度,画右分支
        right(b)
        tree(n-1,d)
        #左转一定角度，画左分支
        left(b+c)
        tree(n-1,d)
        #转回来
        right(c)
    else:
        #画叶子
        right(90)
        n=cos(radians(heading()-45))/4+0.5
        pencolor(n,n*0.8,n*0.8)
        #circle(3)
        drawsnow2()
        left(90)
        #添加0.3倍的飘落叶子
        if(random()>0.7):
            pu()
            #飘落
            t = heading()
            an = -40 +random()*40
            setheading(an)
            dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
            forward(dis)
            setheading(t)
            #画叶子
            pd()
            right(90)
            n = cos(radians(heading()-45))/4+0.5
            pencolor(n*0.5+0.5,0.4+n*0.4,0.4+n*0.4)
            #circle(2)
            drawsnow2()
 
            left(90)
            pu()
            #返回
            t=heading()
            setheading(an)
            backward(dis)
            setheading(t)
    pu()
    backward(l)#退回
 
def drawsnow2():  # 定义花的方法
    t.ht()  # 隐藏笔头，ht=hideturtle
    t.pensize(2)  # 定义笔头大小
    #t.pencolor("white")  # 定义画笔颜色为白色，其实就是花为白色
    t.pu()  # 提笔，pu=penup
    t.pd()  # 落笔，pd=pendown
    dens = 6  # 花瓣数设为6
    snowsize = r.randint(1, 5)  # 定义花大小
    for j in range(dens):  # 就是6，那就是画5次，也就是一个花五角星
        # t.forward(int(snowsize))  #int（）取整数
        t.fd(int(snowsize))
        t.backward(int(snowsize))
            # t.bd(int(snowsize))  #注意没有bd=backward，但有fd=forward，小bug
        t.right(int(360 / dens))  # 转动角度
 
 
 
bgcolor(0.5,0.5,0.5)#背景色#隐藏turtle
speed(0)#速度 1-10渐进，0 最快
ht()
tracer(0,0)
pu()#抬笔
backward(100)
left(90)#左转90度
pu()#抬笔
backward(300)#后退300
tree(12,100)#递归7层
done()