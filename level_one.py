from random import randint

def levelOne(maze, bot, size, gold, pit):

    iRotate = 0
    iMove = 0
    ifGoldWasFound = False
    scanned = ""
    while True:
        print("\n/////////////////////// LOOOP  /////////////////////////////////// ")        
        # print(i)
        isGold = bot.isGold(gold)
        isPit = bot.isPit(pit)
        if(isPit == True):
            break
        if(isGold == True):
            break
        scanned = bot.scan(maze,bot,size)



        #THIS IS THE SCANNED AREA
        if(scanned == "G"):
            break
   



        # rotate_or_move = randint(0, 1)
        # if(rotate_or_move):
        #     iMove = iMove + 1
        #     bot.moveForward(size)

        # else:
        #     iRotate = iRotate + 1
        #     bot.rotate(maze)


        printMaze(maze)

        print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ")     
    if(scanned == "G"):
        foundGoldMoveForwardToGold(maze, bot, size, gold, iMove, iRotate)
    # print(scanned)
    def scannedOption():
        pass




def foundGoldMoveForwardToGold(maze, bot, size, gold, iMove, iRotate):
    while(True):
        print("\n/////////////////////// LOOOP  /////////////////////////////////// ")   
        bot.moveForward(size)
        isGold = bot.isGold(gold)

        printMaze(maze)
        print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ") 
        if(isGold == True):
            break
def printMaze(maze):
    for m in maze:
        print (*m, sep=" ")

