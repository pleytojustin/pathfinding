# generate random integer values
from random import seed
from random import randint
from pandas import *


def initializeMaze(startingPoint, gold, beacon, pitArray,size):

    initalMaze = [['_' for x in range(size)] for y in range(size)] 
    #initalize Start 
    # ← → ↑ ↓ ↖ ↗ ↘ ↙
    initalMaze[startingPoint[0]][startingPoint[1]] = "↓"

    #initalize Gold
    initalMaze[gold[0]][gold[1]] = "G"

    #initalize Beacon
    # initalMaze[beacon[0]][beacon[1]] = "B"

    #initalize Pit Array
    for pit in pitArray:

        initalMaze[pit[0]][pit[1]] = "P"
    return initalMaze

def levelOne(maze, bot, size):
    scan(maze,bot, size)
    


def levelZero(maze, bot, size, gold):
    print(bot.looking_at)
    print(bot.pos)
    it = 0
    # print(bot.isGold(gold))
    while(bot.isGold(gold) ):
    # while(it != 10):
        print(it)
        rotate_or_move = randint(0, 1)
        # IF 0 ROTATE if 1 MOVE forward
        #print(bot.restrict_pit_edges(maze,size))
        # if(bot.restrict_pit_edges(maze,size)):
        if(rotate_or_move):
            it = it + 1

            bot.moveForward(size)
            print("FORWARD")
        else:
            bot.rotate(maze)
            print("ROTATE")
        # else:
        #     print("PIT WAS INFRONT")
            # bot.rotate(maze)
        printMaze(maze)
    
def levelZeroNew():
    it = 0 
    while(bot.isGold(gold)):
        rotate_or_move = randint(0, 1)
        if(rotate_or_move):
            it = it + 1

            bot.moveForwardNew(size)
            print("FORWARD")
        else:
            bot.rotate(maze)
            print("ROTATE")          




        
def scan(maze, bot,size):
    isGold = False
  
    x = bot.x
    y = bot.y
    
    if(bot.looking_at == "SOUTH"):
        print("SOUTH")
        for i in range(size - x):
            if maze[x + i][y] == "G":
                isGold = True
                print("FOUND GOLD")
                
            
    elif(bot.looking_at == "NORTH"):
        print("FACING NORTH")
        for i in range(x):
           
            if maze[i ][y] == "G":
                isGold = True
                print("FOUND GOLD")
                        
        print("NORTH")
    elif(bot.looking_at == "EAST"):
        print("FACING EAST")
        for i in range(size - y):
            if maze[x][y + i] == "G":
                isGold = True
                print("FOUND GOLD")
    elif(bot.looking_at == "WEST"):
        print("FACING WEST")
        for i in range(y):
            if maze[x][i] == "G":
                isGold = True
                print("FOUND GOLD")

    print(isGold)
    return isGold

    #This just traverses the whole maze randomly





# def getInfornt(maze, bot):
#     x, y = bot.pos
#     if bot.looking_at == 'NORTH':
#         y = y + 1
#     elif bot.looking_at == 'SOUTH':
#         y = y - 1
#     elif bot.looking_at == 'EAST':
#         x = x + 1
#     elif bot.looking_at == 'WEST':
#         x = x - 1
#     elif bot.looking_at == 'NORT_EAST':
#         x = x - 1
#     return (x,y)

# def checkInfornt(infront, maze, bot):
    
#     print(infront)


class bot:
    pos = (0,0)
    x = 0
    y = 0
    #['NORTH', 'SOUTH', 'EAST', 'WEST','NORT_EAST', 'NORTH_WEST','SOUTH_EAST','SOUTH_WEST']
    looking_at = "SOUTH"
    # ← → ↑ ↓ ↖ ↗ ↘ ↙
    def rotate(self, maze):
        
        try:
            # print(str(self.x) + " AND xxxx  " + str(self.y) + " ROTATE")
            # maze[3][3] = "x"
            # printMaze(maze)
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
            print(str(self.x) + " AND xxxx " + str(self.y) + " FORWARD")
            if(self.looking_at == "WEST"):
                # print("----:", self.checkInfront(size,"WEST"))
                if(self.checkInfront(size,"WEST")):
                    maze[self.x][self.y] = "_"
                    self.y = self.y - 1
                    maze[self.x][self.y] = "←"
                    self.looking_at = "WEST"
                
            elif(self.looking_at == "SOUTH"):
                #print("----:", self.checkInfront(size,"SOUTH"))
                if(self.checkInfront(size,"SOUTH")):
                    maze[self.x][self.y] = "_"
                    self.x = self.x + 1
                    maze[self.x][self.y] = "↓"
                    self.looking_at = "SOUTH"
            elif(self.looking_at == "EAST"):
                #print("----:", self.checkInfront(size,"EAST"))
                if(self.checkInfront(size,"EAST")):
                    maze[self.x][self.y] = "_"
                    self.y = self.y + 1
                    maze[self.x][self.y] = "→"
                    self.looking_at = "EAST"
            elif(self.looking_at == "NORTH"):
                #print("----:", self.checkInfront(size,"NORTH"))
                if(self.checkInfront(size,"NORTH")):
                    maze[self.x][self.y] = "_"
                    self.x = self.x - 1
                    maze[self.x][self.y] = "↑"
                    self.looking_at = "NORTH"
        except IndexError:
            pass
        # return None
    def moveForwardNew(self,size):
        try:
            print(str(self.x) + " AND xxxx " + str(self.y) + " FORWARD")
            if(self.looking_at == "WEST"):
                # print("----:", self.checkInfront(size,"WEST"))
                if(self.checkInfront(size,"WEST")):
                    maze[self.x][self.y] = "_"
                    self.y = self.y - 1
                    maze[self.x][self.y] = "←"
                    self.looking_at = "WEST"
                
            elif(self.looking_at == "SOUTH"):
                #print("----:", self.checkInfront(size,"SOUTH"))
                if(self.checkInfront(size,"SOUTH")):
                    maze[self.x][self.y] = "_"
                    self.x = self.x + 1
                    maze[self.x][self.y] = "↓"
                    self.looking_at = "SOUTH"
            elif(self.looking_at == "EAST"):
                #print("----:", self.checkInfront(size,"EAST"))
                if(self.checkInfront(size,"EAST")):
                    maze[self.x][self.y] = "_"
                    self.y = self.y + 1
                    maze[self.x][self.y] = "→"
                    self.looking_at = "EAST"
            elif(self.looking_at == "NORTH"):
                #print("----:", self.checkInfront(size,"NORTH"))
                if(self.checkInfront(size,"NORTH")):
                    maze[self.x][self.y] = "_"
                    self.x = self.x - 1
                    maze[self.x][self.y] = "↑"
                    self.looking_at = "NORTH"
        except IndexError:
            pass
        # return None
    def restrict_pit_edges(self,maze,size):
        # print(size - 1)
        # print("x: " + str(self.x + 1))
        # print("y: " + str(self.y + 1))
        # print(size - 1)
        if(int(self.x + 1) > int(size - 1) or (int(self.y) + 1) > size - 1):
            print("out of bounds INFRONT")
            return False
        elif(self.looking_at == "WEST"):
            if maze[self.x][self.y - 1] == "P":
                print("PIT INFRONT")
                return False

        elif(self.looking_at == "SOUTH"):
            if maze[self.x + 1][self.y] == "P":
                print("PIT INFRONT")
                return False

        elif(self.looking_at == "EAST"):
            if maze[self.x][self.y + 1] == "P":
                print("PIT INFRONT")
                return False

        elif(self.looking_at == "NORTH"):
            if maze[self.x - 1][self.y] == "P":
                print("PIT INFRONT")
                return False

        else:
            return True
        return True
    def restrict_pit_edges_can_fall_pit(self,maze,size):
        # print(size - 1)
        # print("x: " + str(self.x + 1))
        # print("y: " + str(self.y + 1))
        # print(size - 1)
        if(int(self.x + 1) > int(size - 1) or (int(self.y) + 1) > size - 1):
            print("out of bounds INFRONT")
            return False
        elif(self.looking_at == "WEST"):

            print("PIT INFRONT")
            return False

        elif(self.looking_at == "SOUTH"):
        
            print("PIT INFRONT")
            return False

        elif(self.looking_at == "EAST"):
            print("PIT INFRONT")
            return False

        elif(self.looking_at == "NORTH"):
            print("PIT INFRONT")
            return False

        else:
            return True
        return True
    def isGold(self, gold):
        i = gold[0]
        j =  gold[1]
        # print(i)
        # print(j)
        # print("------ GOLD -----")
        # print(self.x)
        # print(self.y)
        if(self.x  == i and self.y == j):
            print("FOUND GOLD!")
            return False
        else:
            return True

    def isPit(self, pit):
        i = pit[0]
        j =  pit[1]
        # print(i)
        # print(j)
        # print("------ GOLD -----")
        # print(self.x)
        # print(self.y)
        if(self.x  == i and self.y == j):
            print("FOUND GOLD!")
            return False
        else:
            return True

    def checkInfront(self, size, position):
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
        
def printMaze(maze):
    for m in maze:
        print (*m, sep=" ")
if __name__ == "__main__":
    size = 30
    
    #INITALIZE BOT
    bot = bot()

    # print(bot.rotate())
    # print(bot.rotate())

    startingPoint = (0,0)
    bot.x = startingPoint[0]
    bot.y = startingPoint[1]
    gold = (5,1)
    beacon = (5,8)
    pitArray = [(2,5),(3,5),(4,5),(5,5),(0,1)]
    maze = initializeMaze(startingPoint, gold, beacon, pitArray, size)
 
    # printMaze(maze)
    # bot.rotate(maze)
    # print("000000")
    # printMaze(maze)
    # bot.rotate(maze)
    # # print(str(bot.x) )
    # # print(str(bot.y) )

  
    # # bot.rotate(maze)
    # # printMaze(maze)
    # print("000000")
    # bot.moveForward(size)
    # printMaze(maze)
    # print("000000")
    # bot.rotate(maze)
    # printMaze(maze)
    # print("000000")
    # bot.rotate(maze)
    # printMaze(maze)
    # print("000000")
    # bot.moveForward(size)
    # printMaze(maze)

    # bot.moveForward(size)
    # printMaze(maze)

    # bot.moveForward(size)
    # printMaze(maze)

    # bot.moveForward(size)
    # printMaze(maze)

    # bot.moveForward(size)
    # printMaze(maze)

    # bot.moveForward(size)
    # printMaze(maze)


    # bot.moveForward(size)
    # printMaze(maze)

    # bot.rotate(maze)
    # printMaze(maze)

    # bot.rotate(maze)
    # printMaze(maze)

    # bot.rotate(maze)
    # printMaze(maze)

    # bot.moveForward(size)
    # printMaze(maze)  

    # bot.moveForward(size)
    # printMaze(maze)

    # bot.moveForward(size)
    # printMaze(maze)

    # bot.moveForward(size)
    # printMaze(maze)

    # bot.moveForward(size)
    # printMaze(maze)

    # bot.moveForward(size)
    # printMaze(maze)

    # bot.moveForward(size)
    # printMaze(maze)

    # bot.moveForward(size)
    # printMaze(maze)

    # bot.moveForward(size)
    # printMaze(maze)

    # bot.moveForward(size)
    # printMaze(maze)

    # bot.moveForward(size)
    # printMaze(maze)

    # bot.rotate(size)
    # printMaze(maze)

    # if(bot.checkInfront(size,"WEST")):
    #     bot.moveForward(size)
    # bot.rotate(maze)
    # bot.rotate(maze)
    # bot.rotate(maze)
    # bot.rotate(maze)
    # bot.moveForward()
    # bot.restrict_pit_edges(maze, size)
    # bot.moveForward()
    # bot.restrict_pit_edges(maze, size)
    # bot.moveForward()
    # bot.restrict_pit_edges(maze, size)
    # bot.moveForward()
    # bot.restrict_pit_edges(maze, size)
    # bot.moveForward()
    # bot.restrict_pit_edges(maze, size)
    # bot.moveForward()
    # bot.restrict_pit_edges(maze, size)
    # bot.moveForward()
    # bot.restrict_pit_edges(maze, size)
    # bot.moveForward()
    # bot.restrict_pit_edges(maze, size)
    # bot.moveForward()
    # bot.restrict_pit_edges(maze, size)
    # bot.moveForward()
    # bot.restrict_pit_edges(maze, size)
    # bot.moveForward()
    # bot.restrict_pit_edges(maze, size)
    # bot.moveForward()
    # bot.restrict_pit_edges(maze, size)
    
    print("Maze Initalized")
    # print (maze)
    printMaze(maze)
    # for m in maze:
    #     print (*m, sep=" ")
       
    levelZero(maze, bot, size, gold)
    #levelOne(maze,bot,size)
# """
#  Example program to show using an array to back a grid on-screen.
 
#  Sample Python/Pygame Programs
#  Simpson College Computer Science
#  http://programarcadegames.com/
#  http://simpson.edu/computer-science/
 
#  Explanation video: http://youtu.be/mdTeqiWyFnc
# """
# import pygame
# import time

# # Define some colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)

# SIZE = 63

# # This sets the WIDTH and HEIGHT of each grid location
# WIDTH = 10
# HEIGHT = 10


 
# # This sets the margin between each cell
# MARGIN = 1
 
# # Create a 2 dimensional array. A two dimensional
# # array is simply a list of lists.
# grid = []
# for row in range(SIZE):
#     # Add an empty array that will hold each cell
#     # in this row
#     grid.append([])
#     for column in range(SIZE):
#         grid[row].append("")  # Append a cell
 
# # Set row 1, cell 5 to one. (Remember rows and
# # column numbers start at zero.)
# grid[1][5] = 1
 
# # Initialize pygame
# pygame.init()

# window=pygame.display.set_mode((10, 10))
# font=pygame.font.SysFont('arial', 10)
# text=font.render(' V ', True, (0, 0, 0))
# rect=text.get_rect()


# # Set the HEIGHT and WIDTH of the screen
# WINDOW_SIZE = [850, 850]
# screen = pygame.display.set_mode(WINDOW_SIZE)

# # Set title of screen
# pygame.display.set_caption("Array Backed Grid")
 
# # Loop until the user clicks the close button.
# done = False
 
# # Used to manage how fast the screen updates
# clock = pygame.time.Clock()
# i = 0
# # -------- Main Program Loop -----------
# while not done:
#     for event in pygame.event.get():  # User did something
#         if event.type == pygame.QUIT:  # If user clicked close
#             done = True  # Flag that we are done so we exit this loop
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             # User clicks the mouse. Get the position
#             pos = pygame.mouse.get_pos()
#             # Change the x/y screen coordinates to grid coordinates
#             column = pos[0] // (WIDTH + MARGIN)
#             row = pos[1] // (HEIGHT + MARGIN)
#             # Set that location to one
#             grid[row][column] = 1

#             print("Click ", pos, "Grid coordinates: ", row, column)
        

#     # Set the screen background
#     screen.fill(BLACK)
    
#     # Draw the grid
#     for row in range(SIZE):
#         for column in range(SIZE):
#             color = WHITE
#             if grid[row][column] == 1:
#                 color = GREEN

#             pygame.draw.rect(screen,
#                              color,
#                              [(MARGIN + WIDTH) * column + MARGIN,
#                               (MARGIN + HEIGHT) * row + MARGIN,
#                               WIDTH,
#                               HEIGHT])
            
#     # if(i < 50):
#     #     color = WHITE
#     #     grid[i][1] = 1
#     #     pygame.draw.rect(screen,
#     #                         color,
#     #                         [(MARGIN + WIDTH) * 0 + MARGIN,
#     #                         (MARGIN + HEIGHT) * i + MARGIN,
#     #                         WIDTH,
#     #                         HEIGHT])
#     #     window.blit(text, rect)
#     # i = i + 1
    
#     # Limit to 60 frames per second
#     clock.tick(40)

 
#     # Go ahead and update the screen with what we've drawn.
#     pygame.display.flip()
 
# # Be IDLE friendly. If you forget this line, the program will 'hang'
# # on exit.
# pygame.quit()