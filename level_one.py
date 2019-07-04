from random import randint

def levelOne(maze, bot, size, gold, pit, beacon):

    iRotate = 0
    iMove = 0
    ifGoldWasFound = False
    scanned = ""
    move = ""
    hitBottom = False
    # bot = scanAround(bot,size,maze, iMove, iRotate)
    # print(bot.memEast)
    # print("LOOKING EAST? " + str(bot.memEast))
    i = 0 
    while i != 38:
    # while True:
        print("\n/////////////////////// LOOOP  /////////////////////////////////// ")        
        # print(i)
        isGold = bot.isGold(gold)
        isPit = bot.isPit(pit)
        if(isPit == True):
            break
        if(isGold == True):
            break
        # scanned = bot.scan(maze,bot,size)
        if(i == 0):
            bot = scanAround(bot,size,maze, iMove, iRotate, "SOUTH")
            move = whereToMove(bot,maze)
        elif(hitBottom):
            bot = scanAround(bot,size,maze, iMove, iRotate, "EAST")
            move = whereToMove(bot,maze)
        else:
            bot = scanAround(bot,size,maze, iMove, iRotate, "SOUTH")
            move = whereToMove(bot,maze)  
        # print(bot.memNorth)
        # print(bot.memEast)
        # print(bot.memSouth)
        # print(bot.memWest)
        print(hitBottom)
        #THIS IS THE SCANNED AREA
        if(move == "G"):
            break
        elif(move == "B"):
            foundBeaconMoveForwardToBeacon(maze, bot, size, beacon, iMove, iRotate)
            bot = scanAround(bot,size,maze, iMove, iRotate, "SOUTH")
            move = whereToMove(bot,maze)
            break
        else:
            print("MOVE")
            if(bot.x == (size - 1)):
                print("i'm in the bottom")
                hitBottom = True
                # bot.rotate(maze)
                # bot.rotate(maze)
                # bot.rotate(maze)
            elif(bot.x == 0):
                hitBottom = False
                print("i'm in the top")

            bot.moveForward(size)
      
                


        printMaze(maze)
        i = i + 1
        print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ")     
    if(move == "G"):
        foundGoldMoveForwardToGold(maze, bot, size, gold, iMove, iRotate)
    # print(scanned)
def scanAround(bot, size, maze, iMove, iRotate, faceing):

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

        

    if(faceing == "WEST"):
        if(bot.looking_at == "NORTH"):
            bot.rotate(maze)
            bot.rotate(maze)
            bot.rotate(maze)
        elif(bot.looking_at == "EAST"):
            bot.rotate(maze)
            bot.rotate(maze)
        elif(bot.looking_at == "SOUTH"):
            bot.rotate(maze)

        print("\n/////////////////////// LOOOP  /////////////////////////////////// ")   
        printMaze(maze)
        print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ")
    elif(faceing == "NORTH"):
        if(bot.looking_at == "WEST"):
            bot.rotate(maze)
        elif(bot.looking_at == "EAST"):
            bot.rotate(maze)
            bot.rotate(maze)
            bot.rotate(maze)
        elif(bot.looking_at == "SOUTH"):
            bot.rotate(maze)
            bot.rotate(maze)

        print("\n/////////////////////// LOOOP  /////////////////////////////////// ")   
        printMaze(maze)
        print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ")  

    elif(faceing == "EAST"):
        if(bot.looking_at == "WEST"):
            bot.rotate(maze)
            bot.rotate(maze)
        elif(bot.looking_at == "NORTH"):
            bot.rotate(maze)
        elif(bot.looking_at == "SOUTH"):
            bot.rotate(maze)
            bot.rotate(maze)
            bot.rotate(maze)

        print("\n/////////////////////// LOOOP  /////////////////////////////////// ")   
        printMaze(maze)
        print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ")  
    elif(faceing == "SOUTH"):
        if(bot.looking_at == "WEST"):
            bot.rotate(maze)
            bot.rotate(maze)
            bot.rotate(maze)
        elif(bot.looking_at == "NORTH"):
            bot.rotate(maze)
            bot.rotate(maze)
        elif(bot.looking_at == "EAST"):
            bot.rotate(maze)


        print("\n/////////////////////// LOOOP  /////////////////////////////////// ")   
        printMaze(maze)
        print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ")  
    return bot


def whereToMove(bot, maze):
    move = ""

    #DO OTHER LOGIC BEFORE DOING G O B    
    #LOGIC BASE ON WHAT IT SAW 
    # if(bot.memEast == "N"):
    #     # bot.rotate(maze)
    #     # bot.rotate(maze)
    #     # bot.rotate(maze)
    #     move = "E"
    #SOUTH
    if(bot.memSouth == "G"):
        move = "G"
    elif(bot.memSouth == "B"):
        move = "B"



    #WEST
    if(bot.memWest == "G"):
        move = "G"
        bot.rotate(maze)
    elif(bot.memWest == "B"):
        move = "B"
        bot.rotate(maze)

    #NORTH
    if(bot.memNorth == "G"):
        move = "G"
        bot.rotate(maze)
        bot.rotate(maze)
    elif(bot.memNorth == "B"):
        move = "B"
        bot.rotate(maze)
        bot.rotate(maze)

    #EAST
    if(bot.memEast == "G"):
        move = "G"
        bot.rotate(maze)
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

