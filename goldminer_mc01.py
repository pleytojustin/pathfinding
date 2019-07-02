from random import seed
from random import randint
from pandas import *
from level_zero import *
from level_one import *
class bot:
    x = 0
    y = 0
    isOnBeacon = False
    looking_at = "SOUTH"
    memNorth = ""
    memSouth = ""
    memEast = ""
    memWest = ""
    def isGold(self, gold):
        i = gold[0]
        j =  gold[1]

        if(self.x  == i and self.y == j):
            print("search successful")
            return True
        else:
            return False
    def isBeacon(self, beacon):
        isBeacon = False
        for b in beacon:
            i = b[0]
            j = b[1]
            if(self.x == i and self.y == j):
                print("At BEACON")
                isBeacon = True

        return isBeacon
    def isPit(self, pit):
        isPit = False
        for p in pit:
            i = p[0]
            j = p[1]
            if(self.x == i and self.y == j):
                print("FELL IN PIT")
                isPit = True

        return isPit

    def rotate(self, maze):
        try:
            if(self.looking_at == "SOUTH"):
                maze[self.x][self.y] = "←"
                self.looking_at = "WEST"
            elif(self.looking_at == "EAST"):
                maze[self.x][self.y] = "↓"
                self.looking_at = "SOUTH"
            elif(self.looking_at == "NORTH"):
                maze[self.x][self.y] = "→"
                self.looking_at = "EAST"
            elif(self.looking_at == "WEST"):
                maze[self.x][self.y] = "↑"
                self.looking_at = "NORTH"
        except IndexError:
            pass 
    def moveForward(self,size):
        try:
            #print(str(self.x) + " AND xxxx " + str(self.y) + " FORWARD")
            if(self.looking_at == "WEST"):
                # print("----:", self.checkInfront(size,"WEST"))
                # if(self.checkInfront_with_pit(size,"WEST")): #NO DEATH IN PIT
                if(self.isMoveValid(size,"WEST")): # DEATH IN PIT
                    if(self.isOnBeacon == False):
                        maze[self.x][self.y] = "_"        
                    else:
                        maze[self.x][self.y] = "B"
                    if(maze[self.x][self.y - 1] == "B"):
                        print("BEACON")
                        
                        self.isOnBeacon = True
                    else:
                   
                        self.isOnBeacon = False
                    
                    self.y = self.y - 1
                    maze[self.x][self.y] = "←"
                    self.looking_at = "WEST"
                
            elif(self.looking_at == "SOUTH"):
                #print("----:", self.checkInfront(size,"SOUTH"))
                # if(self.checkInfront_with_pit(size,"SOUTH")): #NO DEATH IN PIT
                if(self.isMoveValid(size,"SOUTH")): # DEATH IN PIT
                    if(self.isOnBeacon == False):
                        maze[self.x][self.y] = "_"      
                    else:
                        maze[self.x][self.y] = "B"
                    if(maze[self.x + 1][self.y] == "B"):
                        print("BEACON")
                        self.isOnBeacon = True
                    else:
                    
                        self.isOnBeacon = False
                     
                    self.x = self.x + 1
                    maze[self.x][self.y] = "↓"
                    self.looking_at = "SOUTH"
            elif(self.looking_at == "EAST"):
                #print("----:", self.checkInfront(size,"EAST"))
                # if(self.checkInfront_with_pit(size,"EAST")): #NO DEATH IN PIT
                if(self.isMoveValid(size,"EAST")): # DEATH IN PIT
                    if(self.isOnBeacon == False):
                        maze[self.x][self.y] = "_"    
                    else:
                        maze[self.x][self.y] = "B"  
                    if(maze[self.x][self.y + 1] == "B"):
                        print("BEACON")
                        self.isOnBeacon = True
                    else:
            
                        self.isOnBeacon = False
                                 
                    self.y = self.y + 1
                    maze[self.x][self.y] = "→"
                    self.looking_at = "EAST"
            elif(self.looking_at == "NORTH"):
                #print("----:", self.checkInfront(size,"NORTH"))
                # if(self.checkInfront_with_pit(size,"NORTH")): #NO DEATH IN PIT
                if(self.isMoveValid(size,"NORTH")): # DEATH IN PIT
                    if(self.isOnBeacon == False):
                        maze[self.x][self.y] = "_"
                    else:
                        maze[self.x][self.y] = "B"
                    if(maze[self.x - 1][self.y] == "B"):
                        print("BEACON")
                        self.isOnBeacon = True
                    else:
                    
                        self.isOnBeacon = False
                             
                    self.x = self.x - 1
                    maze[self.x][self.y] = "↑"
                    self.looking_at = "NORTH"
        except IndexError:
            pass
        # return None

    def isMoveValid(self, size, position):
        isInfrontValid = True
        if(position == "WEST"):
            #print(str(self.x) + " AND " + str(self.y - 1) + " LOOKING WEST")
            if((0 <= (self.y - 1))):
                isInfrontValid = True
            else:
                print("CAN'T MOVE FORWARD WEST")
                isInfrontValid = False
        elif(position == "SOUTH"):
            #print(str(self.x  + 1) + " AND " + str(self.y) + " LOOKING SOUTH")

            if((size > ( self.x + 1))):
                isInfrontValid = True
            else:
                print("CAN'T MOVE FORWARD SOUTH")
                isInfrontValid = False
        elif(position == "EAST"):
            #print(str(self.x) + " AND " + str(self.y + 1) + " LOOKING EAST")
            if((size > (self.y + 1))):
        
                isInfrontValid = True
            else:
                print("CAN'T MOVE FORWARD EAST")
                isInfrontValid = False
        elif(position == "NORTH"):
            #print(str(self.x - 1) + " AND " + str(self.y) + " LOOKING NORTH")
            if((0 <= (self.x - 1))):     
                
                isInfrontValid = True
            else:
                print("CAN'T MOVE FORWARD NORTH")
                isInfrontValid = False
  
        return isInfrontValid

    def checkInfront_with_pit(self, size, position):
        isInfrontValid = True
        if(position == "WEST"):
            #print(str(self.x) + " AND " + str(self.y - 1) + " LOOKING WEST")
            if((0 <= (self.y - 1)) and (maze[self.x][self.y - 1] != "P")):
                isInfrontValid = True
            else:
                print("CAN'T MOVE FORWARD WEST")
                isInfrontValid = False
        elif(position == "SOUTH"):
            #print(str(self.x  + 1) + " AND " + str(self.y) + " LOOKING SOUTH")

            if((size > ( self.x + 1)) and (maze[self.x + 1][self.y] != "P")):
                isInfrontValid = True
            else:
                print("CAN'T MOVE FORWARD SOUTH")
                isInfrontValid = False
        elif(position == "EAST"):
            #print(str(self.x) + " AND " + str(self.y + 1) + " LOOKING EAST")
            if((size > (self.y + 1)) and (maze[self.x][self.y + 1] != "P")):
        
                isInfrontValid = True
            else:
                print("CAN'T MOVE FORWARD EAST")
                isInfrontValid = False
        elif(position == "NORTH"):
            #print(str(self.x - 1) + " AND " + str(self.y) + " LOOKING NORTH")
            if((0 <= (self.x - 1)) and (maze[self.x - 1][self.y] != "P")):     
                
                isInfrontValid = True
            else:
                print("CAN'T MOVE FORWARD NORTH")
                isInfrontValid = False
  
        return isInfrontValid

    def scan(self,maze, bot,size):
        scanned = "N"
    
        x = self.x
        y = self.y
        if(self.looking_at == "SOUTH"):
    
            for i in range(size - x):
                if maze[x + i][y] == "G":
                    scanned = "G"
                    break
                if maze[x + i][y] == "B":
                    scanned = "B"
                    break
                if maze[x + i][y] == "P":
                    scanned = "P"  
                    break                  
                    
                
        elif(self.looking_at == "NORTH"):
         
            for i in range(x):
            
                if maze[i ][y] == "G":
                    scanned = "G"
                    break
                if maze[i ][y] == "B":
                    scanned = "B"
                    break
                if maze[i ][y] == "P":
                    scanned = "P"    
                    break            
                            
     
        elif(self.looking_at == "EAST"):
          
            for i in range(size - y):
                if maze[x][y + i] == "G":
                    scanned = "G"
                    break
                if maze[x][y + i] == "B":
                    scanned = "B"
                    break
                if maze[x][y + i] == "P":
                    scanned = "P"      
                    break 
        elif(self.looking_at == "WEST"):
            
            for i in range(y):
                if maze[x][i] == "G":
                    scanned = "G"
                    break
                if maze[x][i] == "B":
                    scanned = "B"
                    break
                if maze[x][i] == "P":
                    scanned = "P"    
                    break       

        # print(isGold)
        return scanned

def initializeMaze(startingPoint, gold, beacon, pitArray,size):

    initalMaze = [['_' for x in range(size)] for y in range(size)] 
    #initalize Start 
    # ← → ↑ ↓ ↖ ↗ ↘ ↙
    initalMaze[startingPoint[0]][startingPoint[1]] = "↓"

    #initalize Gold
    initalMaze[gold[0]][gold[1]] = "G"

    #initalize Beacon
    for b in beacon:

        initalMaze[b[0]][b[1]] = "B"
    # initalMaze[beacon[0]][beacon[1]] = "B"

    #initalize Pit Array
    for pit in pitArray:

        initalMaze[pit[0]][pit[1]] = "P"
    return initalMaze

if __name__ == "__main__":
    size = 30
    
    #INITALIZE BOT
    bot = bot()

    startingPoint = (0,0)
    bot.x = startingPoint[0]
    bot.y = startingPoint[1]
    gold = (9,2)
    #beacon = [(2,5),(3,5),(4,5),(5,5),(0,1),(0,2)]
    beacon = [(5,2), (9,0)]

    pitArray = [(2,5),(3,5),(4,5),(5,5),]
    # pitArray = []
    maze = initializeMaze(startingPoint, gold, beacon, pitArray, size)

    print("Maze Initalized")
    printMaze(maze)

       
    #levelZero(maze, bot, size, gold, pitArray)
    levelOne(maze, bot, size, gold, pitArray, beacon)