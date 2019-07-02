from random import randint

def levelOne(maze, bot, size, gold, pit, beacon):

    iRotate = 0
    iMove = 0
    ifGoldWasFound = False
    scanned = ""
    move = ""
    # bot = scanAround(bot,size,maze, iMove, iRotate)
    # print(bot.memEast)
    # print("LOOKING EAST? " + str(bot.memEast))
    while True:
        print("\n/////////////////////// LOOOP  /////////////////////////////////// ")        
        # print(i)
        isGold = bot.isGold(gold)
        isPit = bot.isPit(pit)
        if(isPit == True):
            break
        if(isGold == True):
            break
        # scanned = bot.scan(maze,bot,size)

        bot = scanAround(bot,size,maze, iMove, iRotate)
        move = whereToMove(bot,maze)
        #THIS IS THE SCANNED AREA
        if(move == "B"):
            foundBeaconMoveForwardToBeacon(maze, bot, size, beacon, iMove, iRotate)
            bot = scanAround(bot,size,maze, iMove, iRotate)
            move = whereToMove(bot,maze)
            break
            print("BEACON")
        if(move == "G"):
            break
        
        
        print("LOOKING EAST? " + str(bot.memEast))


        # rotate_or_move = randint(0, 1)
        # if(rotate_or_move):
        #     iMove = iMove + 1
        #     bot.moveForward(size)

        # else:
        #     iRotate = iRotate + 1
        #     bot.rotate(maze)


        printMaze(maze)

        print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ")     
    if(move == "G"):
        foundGoldMoveForwardToGold(maze, bot, size, gold, iMove, iRotate)
    # print(scanned)
def scanAround(bot, size, maze, iMove, iRotate):

    # bot.moveForward(size)
    scanned = bot.scan(maze,bot,size)
    bot.memSouth = scanned
    bot.rotate(maze)
    print("\n/////////////////////// LOOOP  /////////////////////////////////// ")   
    printMaze(maze)
    print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ") 

    scanned = bot.scan(maze,bot,size)
    bot.memWest = scanned
    bot.rotate(maze)
    print("\n/////////////////////// LOOOP  /////////////////////////////////// ")   
    printMaze(maze)
    print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ") 

    scanned = bot.scan(maze,bot,size)
    bot.memNorth = scanned
    bot.rotate(maze)
    print("\n/////////////////////// LOOOP  /////////////////////////////////// ")   
    printMaze(maze)
    print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ") 

    scanned = bot.scan(maze,bot,size)
    bot.memEast = scanned
    bot.rotate(maze)
    print("\n/////////////////////// LOOOP  /////////////////////////////////// ")   
    printMaze(maze)
    print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ") 
    


    return bot


def whereToMove(bot, maze):
    move = ""

    #GOLD WAS FOUND
    if(bot.memSouth == "G"):
        move = "G"
       
    elif(bot.memWest == "G"):
        move = "G"
        bot.rotate(maze)
    elif(bot.memNorth == "G"):
        move = "G"
        bot.rotate(maze)
        bot.rotate(maze)
    elif(bot.memEast == "G"):
        move = "G"
        bot.rotate(maze)
        bot.rotate(maze)
        bot.rotate(maze)

    elif(bot.memSouth == "B"):
        move = "B"
       
    elif(bot.memWest == "B"):
        move = "B"
        bot.rotate(maze)
    elif(bot.memNorth == "B"):
        move = "B"
        bot.rotate(maze)
        bot.rotate(maze)
    elif(bot.memEast == "B"):
        move = "B"
        bot.rotate(maze)
        bot.rotate(maze)
        bot.rotate(maze)

    return move


def foundGoldMoveForwardToGold(maze, bot, size, gold, iMove, iRotate):
    while(True):
        print("\n/////////////////////// LOOOP  /////////////////////////////////// ")   
        bot.moveForward(size)
        isGold = bot.isGold(gold)

        printMaze(maze)
        print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ") 
        if(isGold == True):
            break
def foundBeaconMoveForwardToBeacon(maze, bot, size, beacon, iMove, iRotate):
    while(True):
        print("\n/////////////////////// LOOOP  /////////////////////////////////// ")   
        bot.moveForward(size)
        isBeacon = bot.isBeacon(beacon)

        printMaze(maze)
        print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ") 
        if(isBeacon == True):
            break
def printMaze(maze):
    for m in maze:
        print (*m, sep=" ")

