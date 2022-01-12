# define the class player
#define the class board 
#define the class board 
class Board():
    
    def __init__(self,n):
        self.n = n
        self.a = []
        
    def boarder(self,n):
        self.a=[[0 for i in range(n)] for j in range(n)]
        return self.a 

    
    def graph(self,n):
        for i in self.a:
            print(i)
# define the class player
class Player():
    
    def __init__(self,name,x,y):
        self.x = x
        self.y = y
        self.name = name
        self.position=[x,y]
    
        
    def move(self):
        for i in range(2):
            dict={'a':[0,-1],'d':[0,1],'w':[-1,0],'s':[1,0],'j':[0,-1],'l':[0,1],'i':[-1,0],'k':[1,0]}
            cc = input('take action from 4 directions keys mentioned ')
            if cc not in dict:
                print('illegal input , one more chance !') 
                             
            else :
                return dict[(cc)]
                break
                
#机器人类： 从 jikl中输出
class Robot_player(Player):
    
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.position=[x,y]
        
    def random_action(self):
        
        dict1={1:'j',2:'i',3:'k',4:'l'}
        dict={'j':[0,-1],'l':[0,1],'i':[-1,0],'k':[1,0]}
        randint = lambda a,b:round(a+(b-a)*int.from_bytes(__import__('os').urandom(7), 'big')/2**56)
        rd=randint(1,4)

        return dict[dict1[rd]]      