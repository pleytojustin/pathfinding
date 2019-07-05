from random import randint

def levelOne(maze, bot, size, gold, pit, beacon):

    iRotate = 0
    iMove = 0
    ifGoldWasFound = False
    scanned = ""
    move = ""
    hitBottom = False
    invalidatePos = True
    hitRight = False
    # bot = scanAround(bot,size,maze, iMove, iRotate)
    # print(bot.memEast)
    # print("LOOKING EAST? " + str(bot.memEast))
    i = 0 
    while i != 5:
    # while True:
        print("\n/////////////////////// LOOOP  /////////////////////////////////// ")        
        # print(i)
        isGold = bot.isGold(gold)
        isPit = bot.isPit(pit)
        if(isPit == True):
            print("I'm in the pit")
            break
        if(isGold == True):
            break
        # scanned = bot.scan(maze,bot,size)
        if(i == 0):
            bot = scanAround(bot,size,maze, iMove, iRotate, "SOUTH",invalidatePos)
            move = whereToMove(bot,maze,size)
        elif(hitBottom):
            bot = scanAround(bot,size,maze, iMove, iRotate, "EAST",invalidatePos)
            move = whereToMove(bot,maze,size)         
        else:
            bot = scanAround(bot,size,maze, iMove, iRotate, "SOUTH",invalidatePos)
            move = whereToMove(bot,maze,size)  
        if(hitRight):
            bot = scanAround(bot,size,maze, iMove, iRotate, "WEST",invalidatePos)
            move = whereToMove(bot,maze,size)   
        # else:
        #     bot = scanAround(bot,size,maze, iMove, iRotate, "NORTH",invalidatePos)
        #     move = whereToMove(bot,maze,size)  
        # print(bot.memNorth)
        # print(bot.memEast)
        # print(bot.memSouth)
        # print(bot.memWest)
        print(hitBottom)
        #THIS IS THE SCANNED AREA
        if(move == "G"):
            break
        elif(move == "B"):
            print("FOUND BEACON")
            invalidatePos = False
            foundBeaconMoveForwardToBeacon(maze, bot, size, beacon, iMove, iRotate)
            bot = scanAround(bot,size,maze, iMove, iRotate, "SOUTH",invalidatePos)
            move = whereToMove(bot,maze,size)
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
            
            if(bot.y == (size - 1)):
                hitRight = True
                print("i'm in the right most")

            elif(bot.y == 0):
                hitRight = False
                print("i'm in the left most")

            bot.moveForward(size)
      
                


        printMaze(maze)
        i = i + 1
        print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ")     
    if(move == "G"):
        foundGoldMoveForwardToGold(maze, bot, size, gold, iMove, iRotate)
    # print(scanned)
def scanAround(bot, size, maze, iMove, iRotate, faceing,invalidatePos):

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

        
    if(invalidatePos == True):
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


def whereToMove(bot, maze,size):
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
    elif(bot.memSouth == "P"):
        print("THERE IS PIT SOUTH")


    #WEST
    if(bot.memWest == "G"):
        move = "G"
        bot.rotate(maze)
    elif(bot.memWest == "B"):
        move = "B"
        bot.rotate(maze)
    elif(bot.memWest == "P"):
        print("THERE IS PIT WEST")
    #NORTH
    if(bot.memNorth == "G"):
        move = "G"
        bot.rotate(maze)
        bot.rotate(maze)
    elif(bot.memNorth == "B"):
        move = "B"
        bot.rotate(maze)
        bot.rotate(maze)
    elif(bot.memNorth == "P"):
        print("THERE IS PIT NORTH")
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
    elif(bot.memEast == "P"):
        print("THERE IS PIT EAST")


   

    if(bot.memSouth == "P" and bot.looking_at == "SOUTH"):
        print("let's avoid it?")
        # if(bot.memWest == "P"):
        #     print("OH NOH I'm STUCK MAYBE?")
        #     bot.rotate(maze)
        #     bot.rotate(maze)
        #     bot.rotate(maze)
        # else:

        bot.rotate(maze)
        bot.rotate(maze)
        bot.rotate(maze)
        bot.moveForward(size)
        bot.rotate(maze)
    # if(bot.memNorth == "P"):
    # if(bot.memWest == "P" and bot.looking_at == "WEST"):

    # return move


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
    while(True):
        print("\n/////////////////////// LOOOP  /////////////////////////////////// ")   
        bot.moveForward(size)
        isBeacon = bot.isBeacon(beacon)
        print("going to beacon")
        printMaze(maze)
        print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ") 
        if(isBeacon == True):
            break
def printMaze(maze):
    for m in maze:
        print (*m, sep=" ")

