#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 19:00:27 2022

@author: momokosmac
"""
from Classes import Board   
from Classes import Player

#Part1_basic_version.py

#function define 

def accum(l,u):
    Z=[]
    for (x,y) in zip(l,u):
        z=x+y
        Z.append(z)
    return Z 

def gameover():
    print('--------------------')
    print('     Game Over ~  :)')
    print('--------------------') 
    
#初始化设置 

print('Game starts !  welcome !')
playerA_name = input('Enter the 1st username please:__ ')
playerB_name = input('Enter the other username please:__ ')

#创建boarder
size_of_board = int(input('Now we create the board , please enter a number of the size:'))
aa = Board(size_of_board)
a = aa.boarder(size_of_board)
# b = aa.graph(size_of_board)
playerA = Player(playerA_name,0,0)
playerB = Player(playerB_name,size_of_board-1,size_of_board-1)

#dict={'a':[0,-1],'d':[0,1],'w':[-1,0],'s':[1,0],'j':[0,-1],'l':[0,1],'i':[-1,0],'k':[1,0]}   
i=1 
n = size_of_board
#position_a=[0,0]
position_a = playerA.position
a[position_a[0]][position_a[1]]=1
#position_b=[n-1,n-1]   #到时候如果有函数定义可以更新这成[n,n]
position_b=playerB.position
#print(position_b)
a[position_b[0]][position_b[1]]=2
# 游戏开头语

print('Now the situation is  : ')
print('^^^^^^^^^^^^^^^^')
aa.graph(size_of_board)
#P(a)
print('^^^^^^^^^^^^^^^^')
while i <= 100 :
    # A take actions  when i is odd number
    if i %2 ==1:
        print('\033[5;30;36m It is '+playerA.name+ '\'s turn: '+ 'turn'+ str(i) )
        print('hint: you are allowed to take action from 4 directions keys :（awsd）')
        #playerA.move()
        #if di_a in('a','s','w','d'):
        step_a = playerA.move()  #输入移动方向
        position_a = accum(position_a,step_a)  # 矩阵的索引，代表玩家的绝对坐标=最新坐标
        # 1 check whether it crashed the wall ?
        # 2 check whether it collided with abother ? or went back ?(in my opinion , two illegal move can be checked 
        # together , for there common feature with position !=0(the priginial unit with position [0,0]). Moreover , 
        # when we find it illegal ,we shall clarify the specific illegal reason by the if...else statement
        if a[position_a[0]][position_a[1]]!=0:
            if a[position_a[0]][position_a[1]]== 1:
                print('Can not back!  U loss the game!')
                gameover()
                break

            elif a[position_a[0]][position_a[1]]== 2:
                print('Oh~ '+ playerB.name+ ' had occupied the cell~ U loss the game ！')
                gameover()
                break 
        else :           
            for j in position_a :  #非法操作的筛选 index＜0 或＞ n ， 则 loss
                if j < 0 or j > n-1  :  #if/else判断position_a的坐标是否在范围内，如果在 ，就继续游戏。
                    print('Oh~ Cause'+ playerA.name+ ' crashed into the wall, playerB is winner !!!')
                    gameover()
                    break
                else :
                    print('wait a minute...')
            print('Good ~ And now it becomes : ')
            print('^^^^^^^^^^^^^^^^')
            
            a[position_a[0]][position_a[1]]=1
            #P(a)
            aa.graph(size_of_board)
            
            print('^^^^^^^^^^^^^^^^')             
       
            
    # B take actions  when i is even number
    else :
        
        print('\033[7;18;32m It is playerB  turn: '+'turn'+ str(i))
        print('hint: you are allowed to take action from 4 directions keys :（jikl）')
        #di_b = input('take action from 4 directions:（jikl） ')
        step_b = playerB.move()  #输入移动方向
        position_b = accum(position_b,step_b )  # 矩阵的索引，代表玩家的绝对坐标=最新坐标
        #print(position_b)
        # 1 check whether it crashed the wall ?
        # 2 check whether it collided with abother ? or went back ?(in my opinion , two illegal move can be checked 
        # together , for there common feature with position !=0(the priginial unit with position [0,0]). Moreover , 
        # when we find it illegal ,we shall clarify the specific illegal reason by the if...else statement
        if  position_b[0] > n-1 or position_b[1] > n-1 :
            print('Oh~ Cause '+ playerB.name + ' crashed into the wall,'+ playerA.name+ ' is winner !!!') # 撞墙
            gameover()
            break 
        elif a[position_b[0]][position_b[1]]!=0: # 撞人/回退
            if a[position_b[0]][position_b[1]]== 2:
                print('Can not back!  U loss the game!')
                gameover()
                break

            elif a[position_b[0]][position_b[1]]== 1:
                print('Oh~'+ playerA.name+ ' had occupied the cell~ U loss the game')
                gameover()
                break 
        else :
            print('wait a minute...')
            print('Good ~ And now it becomes : ')
            print('^^^^^^^^^^^^^^^^')
            #print(position_b)
            a[position_b[0]][position_b[1]]=2
            #P(a)
            aa.graph(size_of_board)

            print('^^^^^^^^^^^^^^^^')        

        
    i+=1



