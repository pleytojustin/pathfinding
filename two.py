from random import randint
import heapq
def levelTwo(maze, bot, size, gold, pit, beacon):
    iMove = 0 
    iRotate = 0
    i = 0 
    moveVal = ""
    openList = []
    closeList = []

    # heapq.heapqpsuh(openList,(0,0))
    # heapq.heappsuh(closeList,(0,0))
    while True:
        isGold = bot.isGold(gold)

        if(isGold == True):
            break
        scanAll(bot,size, maze, iMove, iRotate)
        print(" +N++  "+bot.memNorth)
        print(" +S++  "+bot.memSouth)
        print(" +E++  "+bot.memEast)
        print(" +W++  "+bot.memWest)
        # heuristics(bot)
        minimumValue, goTo = computeF(bot,closeList,gold)
        print(minimumValue)
        print(goTo)
        if(goTo == "SOUTH"):
            bot.moveForward(size)
        if(goTo == "EAST"):
            bot.rotate(maze)
            bot.rotate(maze)
            bot.rotate(maze)         
            bot.moveForward(size)
        if(goTo == "WEST"):
            bot.rotate(maze)
            bot.moveForward(size)
        if(goTo == "NORTH"):
            bot.rotate(maze)
            bot.rotate(maze)
            bot.moveForward(size)

            


        print("\n/////////////////////// LOOOP  /////////////////////////////////// ")  
        printMaze(maze)
        print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ") 
        i = i + 1
        iMove = iMove + 1
        iRotate = iRotate + 1
    if(moveVal == "GOLD"):
        foundGoldMoveForwardToGold(maze,bot,size,gold,iMove,iRotate)
    if(moveVal == "BECON"):
        foundBeaconMoveForwardToBeacon(maze,bot,size,beacon,iMove,iRotate)
        foundGoldMoveForwardToGold(maze,bot,size,gold,iMove,iRotate)
        
def move(bot,size,maze,iMove,iRotate):
    move = ""

    return move


def manhattan(bot, gold):
    D = 1
    x = abs(bot.x - gold[0])
    y = abs(bot.y - gold[1])
    return D * (x + y)

def heuristics(bot):
    north = 0
    south = 0
    east = 0
    west = 0
    #SOUTH
    if(bot.memSouth == "P"):
        south = 100
    elif(bot.memSouth == "N"):
        south = 50    

    #WEST
    if(bot.memWest == "P"):
        west = 100
    elif(bot.memWest == "N"):
        west = 50

    #NORTH
    if(bot.memNorth == "P"):
        north = 100
    elif(bot.memNorth == "N"):
        north = 50
    
    #EAST
    if(bot.memEast == "P"): 
        east = 100
    elif(bot.memEast == "N"):
        east = 50
    
    return south,west,north,east


def computeF(bot,closeList,gold):
    
    fn = 0
    fnSouth = 0
    fnWest = 0
    fnNorth = 0
    fnEast = 0
    gn = manhattan(bot,gold)
    print("Man distance: " + str(gn) )
    south, west, north, east = heuristics(bot)

    #COMPUTED FN IS NOW HERE
    fnSouth = gn + south
    fnWest = gn + west
    fnNorth = gn + north
    fnEast = gn + east

    minimumValue = 100000000

    print(fnSouth)
    print(fnWest)
    print(fnNorth)
    print(fnEast)
    goTo = ""
    if(minimumValue >=  fnWest):
        minimumValue = fnWest
        goTo = "WEST"

    if(minimumValue >=  fnNorth):
        minimumValue = fnNorth
        goTo = "NORTH"

    if(minimumValue >=  fnEast):
        minimumValue = fnEast
        goTo = "EAST"

    if(minimumValue >=  fnSouth):
        minimumValue = fnSouth
        goTo = "SOUTH"
    

    print("minValue is: " + str(minimumValue) + " " + goTo)
    # for i in range(0,4):
    #     minimum = 0
    #     if(i == 0):
    #     elif()

  
        # heapq.heappush(openList,gold)
    
    return minimumValue, goTo


    
def scanAll(bot,size, maze, iMove, iRotate):
    print("Scanning all ...")
    #ALWAYS FACE SOUTH 
    while(bot.looking_at != "SOUTH"):
        pass
        bot.rotate(maze)
    else:
        pass
    scanned = bot.scan(maze,bot,size)
    bot.memSouth = scanned
    bot.rotate(maze)        
    

    scanned = bot.scan(maze,bot,size)
    bot.memWest = scanned
    bot.rotate(maze)


    scanned = bot.scan(maze,bot,size)
    bot.memNorth = scanned
    bot.rotate(maze)


    scanned = bot.scan(maze,bot,size)
    bot.memEast = scanned
    bot.rotate(maze)


    #ALWAYS FACE SOUTH 
    while(bot.looking_at != "SOUTH"):
        # print("set south")
        bot.rotate(maze)
    else:
        pass
        # print("no need to set south")

def foundGoldMoveForwardToGold(maze, bot, size, gold, iMove, iRotate):
    #LAST CHECK FOR GOLD
    while(bot.scan(maze, bot,size) != "G"):
        bot.rotate(maze)

    while(True):
        print("\n/////////////////////// LOOOP  /////////////////////////////////// ")   
        bot.moveForward(size)
        isGold = bot.isGold(gold)
        print("going to gold")
        print(" +N++  "+bot.memNorth)
        print(" +S++  "+bot.memSouth)
        print(" +E++  "+bot.memEast)
        print(" +W++  "+bot.memWest)
        printMaze(maze)
        
        print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ") 
        if(isGold == True):
            break
def foundBeaconMoveForwardToBeacon(maze, bot, size, beacon, iMove, iRotate):
    #LAST CHECK FOR GOLD
    while(bot.scan(maze, bot,size) != "B"):
        bot.rotate(maze)

    isThereAnotherBeacon = False
    while(True):
        print("\n/////////////////////// LOOOP  /////////////////////////////////// ")   
        bot.moveForward(size)
        isBeacon = bot.isBeacon(beacon)
        print("going to beacon")
        printMaze(maze)
        print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ") 
        if(isBeacon == True):
            # bot.botNewBeacon = (bot.x,bot.y)
            # while(bot.scan(maze, bot,size)):
            #     bot.rotate(maze)
            #     isThereGold = 

            # while(bot.scan(maze, bot,size) != "B"):
            #     bot.rotate(maze)
            #     isThereAnotherBeacon = True
            # if(isThereAnotherBeacon):

            #     foundBeaconMoveForwardToBeacon(maze, bot, size, beacon, iMove, iRotate)
            break
def printMaze(maze):
    for m in maze:
        print (*m, sep=" ")

