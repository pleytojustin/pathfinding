from random import randint

def levelOne(maze, bot, size, gold, pit):

    iRotate = 0
    iMove = 0
    while True:
        print("\n/////////////////////// LOOOP  /////////////////////////////////// ")        
        # print(i)
        
        scanned = bot.scan(maze,bot,size)
        
        # rotate_or_move = randint(0, 1)
        # if(rotate_or_move):
        #     iMove = iMove + 1
        #     bot.moveForward(size)

        # else:
        #     iRotate = iRotate + 1
        #     bot.rotate(maze)

        isGold = bot.isGold(gold)
        isPit = bot.isPit(pit)
        printMaze(maze)

        print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ")     
        if(isPit == True):
            break
        if(isGold == True):
            break
    
    def scannedOption():
        pass

def printMaze(maze):
    for m in maze:
        print (*m, sep=" ")

