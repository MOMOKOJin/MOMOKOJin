 # Tron Game . read me：
 

before design the Tron game , classify the object fisrtly :

# Basic Version

## 1 boarder :

1.1 it made of a matrix of square ，the size of boarder is custimized , by input number from player .
The default value of unit in matrix is 0, when the position occuppied by player , it will turn into other value .


1.2 Class boarder : 

create a class, named boarder with initial character of size .
and create a method ,when input a number(n), returns a matrix with size of n*n .

## 2 player:

2.1 player :

it is a double-player game , so two players should have different value after taking actions ;
The initial position of two player: A & B are [0][0],and [n-1][n-1] of the boarder ;
for player A , I use 'awsd' ,reprents 4 directions , when one unit occupied by A ，the value of unit turns to 1 ；
for player B , I use 'jikl' ,reprents 4 directions , when one unit occupied by B ，the value of unit turns to 2 ；
ps : define 'awsd'/'jikl' as functional word 

2.2 Class player :
initial character with : name(ID), position ,color , action direction 


To have a better effect ,I set different color font to record two player's action ;

## 3 method-making , I created 2 methods :

the first one :accum() is to tranfer a move_position(from 4 directions) ,to the accumulated positon on the board , which to gaive value , to calculate all the units player have occupied.
the second : game over() used when game is over , with some print sentences .

## 4 the rule making --the most crucial part 

4.1 summary of rule：
two players take actions in turns , both of them can move 1 unit per turn , both of player are limited to go new unit which is not occupied , and go out of the boarder is not permitted.

4.2 about action turns ：
through while circulation + if else ,for player A take actions every odd turns ,and  B take actions every odd turns;

4.3 two symbols for game over :

    1. go to the unit value != 0;
    2. the 2 positions of unit is not in [0,n-1],which means player go out of the range .

4.4 frequency & implement of judgement :

system judge the action after every action ;

there are 3 conditions whether the action is illegal(error) from steps below :

a : whether player input a functional word ? (write it in the class method)
    -- if false , player will get a second chance(one more chance) 
    b : whether the move is go-back or go-after-another player ?
        -- if true , game over , and define current play lose the game ,game over 
        c : whether player go out of the boarder ?
            -- if yes , lose the game ,game over 
when illegal action with a ,seen as error action , trigger a next chance 
when illegal action with b,c, it triggers the game over , and we judge the player in current turn lose the game .
            
--if the move action is legal ,turns to the next player 


### The advantages of my code-design :
1 customization : to increase the involvement of players , set some customized part,like setting a personal username , the size of the board , which means users can adjust the difficulty according to personal conditions ;
2 error-tolerance , set if...else conditional statement for the errors below   :
• Move that is not listed as one of the 4 directions. 
• Repeated player ID/colour. 
• A negative value of the initial location of a player

-- open with Part1_basic_version.py


# Advance Version

1 : move simultaneously
based on the original code, we can remove the Outermost condition judgment , and after that,two players will finish one-step-action in one game turn , to allow players to move simultaneously.
ps: the computer player's action is based on player B ,with 4 direction by 'jikl' ,and I set one dictionary connect 4 words with 1,2,3,4 ,then I create one lambda with a randint(1,4), every turn it will create one random number form 1 to 4 , and with each number with one corresponding direction , which is the move_position of computer player but because of the random of the number ,at beginning step there are 50% possibility to trigger the game over condition ,so it is a little  stupid . There are much room for improvement. \ 

--open with Part1_advaced_v1.py file 

2 :play with computer player 
we are supposed to play with robot player ,which becomes a single game . it is a child class based
on Class Player, robot inherit initial method from the player,and it own a random action method , i use the
lambda function to realise the fucntion .
 
--open with Part1_adanced_v2.py file 


