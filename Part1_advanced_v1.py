#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 19:35:10 2022

@author: momokosmac
"""

#Part1_advanced_v1.py
#初始化设置 initial settings
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
    
    
print('Game starts !  welcome !')
playerA_name = input('Enter the 1st username please:__ ')
playerB_name = input('Enter the other username please:__ ')

#to create a board
size_of_board = int(input('Now we create the board , please enter a number of the size:'))
aa = Board(size_of_board)
a = aa.boarder(size_of_board)
playerA = Player(playerA_name,0,0)
playerB = Player(playerB_name,size_of_board-1,size_of_board-1)


i=1 
n = size_of_board
#position_a=[0,0]
position_a = playerA.position
a[position_a[0]][position_a[1]]=1
#position_b=[n-1,n-1]   
position_b=playerB.position
#print(position_b)
a[position_b[0]][position_b[1]]=2

# beginning instruction with customization

print('Now the situation is  : ')
print('^^^^^^^^^^^^^^^^')
#P(a)
aa.graph(size_of_board)
print('^^^^^^^^^^^^^^^^')
while i <= 100 :
    # cancell the if...else conditional statement, two players will play together in one turn :
    # A take first
 
    print('\033[5;30;36m It is '+ playerA.name + ' turn: '+ 'turn'+ str(i) )
    print('hint: you are allowed to take action from 4 directions keys :（awsd）')
    #playerA.move()
    #if di_a in('a','s','w','d'):
    step_a = playerA.move()  #输入移动方向
    position_a = accum(position_a,step_a)  # 矩阵的索引，代表玩家的绝对坐标=最新坐标
    # 1 check whether it crashed the wall ?
    # 2 check whether it collided with abother ? or went back ?(in my opinion , two illegal move can be checked 
    # together , for there common feature with position !=0(the priginial unit with position [0,0]). Moreover , 
    # when we find it illegal ,we shall clarify the specific illegal reason by the if...else statement)
    if a[position_a[0]][position_a[1]]!=0:
        if a[position_a[0]][position_a[1]]== 1:
            print('Can not back!  U loss the game!')
            gameover()
            break

        elif a[position_a[0]][position_a[1]]== 2:
            print('Oh~ '+ playerB.name + ' had occupied the cell~ U loss the game ！')
            gameover()
            break 
    else :           
        for j in position_a :  #非法操作的筛选 index＜0 或＞ n ， 则 loss
            if j < 0 or j > n-1  :  #if/else判断position_a的坐标是否在范围内，如果在 ，就继续游戏。
                print('Oh~ Cause '+ playerA.name + 'crashed into the wall, '+ playerB.name + ' is winner !!!')
                gameover()
                break
            else :
                print('wait a minute...')
        print('Good ~ And now it becomes : ')
        print('^^^^^^^^^^^^^^^^')
        #print(position_a)
        a[position_a[0]][position_a[1]]=1
        #P(a)
        aa.graph(size_of_board)
        print('^^^^^^^^^^^^^^^^')             
        
    # then B :
    print('\033[7;18;32m It is playerB  turn: '+'turn'+ str(i))
    print('hint: you are allowed to take action from 4 directions keys :（jikl）')
    
    step_b = playerB.move()  
    # after moving ,refresh position of B 
    position_b = accum(position_b,step_b )  
    #print(position_b)
    # 1 check whether it crashed the wall ?
    # 2 check whether it collided with abother ? or went back ?(in my opinion , two illegal move can be checked 
    # together , for there common feature with position !=0(the priginial unit with position [0,0]). Moreover , 
    # when we find it illegal ,we shall clarify the specific illegal reason by the if...else statement)
    if  position_b[0] > n-1 or position_b[1] > n-1 :
        print('Oh~ Cause '+ playerB.name + ' crashed into the wall, '+ playerA.name + 'is winner !!!') # 撞墙
        gameover()
        break 
    elif a[position_b[0]][position_b[1]]!=0: # 撞人/回退
        if a[position_b[0]][position_b[1]]== 2:
            print('Can not back!  U loss the game!')
            gameover()
            break

        elif a[position_b[0]][position_b[1]]== 1:
            print('Oh~ '+ playerA.name + ' had occupied the cell~ U loss the game')
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




