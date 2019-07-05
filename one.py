from random import randint

def levelOne(maze, bot, size, gold, pit, beacon):
    iMove = 0 
    iRotate = 0
    i = 0 
    moveVal = ""
    # while i != 60:
    while(True):
        scanAll(bot,size, maze,iMove,iRotate)
        if(i == 0):
            print(" +N++  "+bot.memNorth)
            print(" +S++  "+bot.memSouth)
            print(" +E++  "+bot.memEast)
            print(" +W++  "+bot.memWest)
            if(bot.memEast == "P" and bot.memSouth == "N"):
                #GOING THE SOUTH
                bot.moveForward(size) 
                print("\n/////////////////////// LOOOP  /////////////////////////////////// ")  
                printMaze(maze)
                print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ") 
            elif(bot.memSouth == "P" and bot.memEast == "N"):
                #GOING TO THE SOUTH
                bot.rotate(maze)
                bot.rotate(maze)
                bot.rotate(maze)
                bot.moveForward(size)    
                print("\n/////////////////////// LOOOP  /////////////////////////////////// ")  
                printMaze(maze)
                print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ") 
            elif(bot.memSouth == "N" and bot.memEast == "N"):
                bot.rotate(maze)
                bot.rotate(maze)
                bot.rotate(maze)
                bot.moveForward(size)    
                print("\n/////////////////////// LOOOP  /////////////////////////////////// ")  
                printMaze(maze)
                print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ") 
            else:
                pass
                # if(bot.memEast == "N" and bot.memSouth == "P"):
                #     pass

                
        else:
            print(" +N++  "+bot.memNorth)
            print(" +S++  "+bot.memSouth)
            print(" +E++  "+bot.memEast)
            print(" +W++  "+bot.memWest)
            moveVal = move(bot,size,maze,iMove,iRotate)
            print(moveVal)
            if(moveVal == "GOLD"):
                break
            if(moveVal == "BECON"):
                break
            # scanAll(bot, size, maze, iMove, iRotate)

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
        # moveVal = move(bot,size,maze,iMove,iRotate)

        # while(moveVal == "BEACON"):
        #     moveVal = move(bot,size,maze,iMove,iRotate)

        foundGoldMoveForwardToGold(maze,bot,size,gold,iMove,iRotate)
        
    # print("HELLO")    
    # print("\n/////////////////////// LOOOP  /////////////////////////////////// ")   
    # printMaze(maze)
    # print("///////////////////// FORWARD: " + str(iMove) + " ROTATE: " + str(iRotate) + " ////////////////////// ") 
# def move(bot,size, maze, iMove, iRotate):
def move(bot,size,maze,iMove,iRotate):
    move = ""
    
    #GOLD GOLD GOLD
    if(bot.memEast == "G" or bot.memNorth == "G" or bot.memSouth == "G" or bot.memWest == "G"):
        move = "GOLD"
        return move
    if(bot.memEast == "B" or bot.memNorth == "B" or bot.memSouth == "B" or bot.memWest == "B"):
        move = "BECON"
        return move

    #TO GO DOWN HIT EAST
    if(bot.y == (size - 1)):
        bot.hitEast = True
    if(bot.hitEast):
        move = "E"

    #TO GO LEFT HIT SOUTH
    if(bot.x == (size - 1)):
        bot.hitEast = False
        bot.hitSouth = True
    if(bot.hitSouth):
        move = "S"

    print( "south: " +str(bot.hitSouth))
    print( "east: " +str(bot.hitEast))
    print(str(bot.hitSouth))
    if(bot.memEast == "N" and bot.hitEast == False and bot.hitSouth == False):
        bot.rotate(maze)
        bot.rotate(maze)
        bot.rotate(maze)
        bot.moveForward(size)
    elif(bot.memSouth == "N" and bot.hitSouth == False):
        print('1')
        bot.moveForward(size)
    elif(bot.memWest == "N" and bot.hitSouth == False):
        print('2')

        bot.rotate(maze)
        bot.moveForward(size)
    elif(bot.memSouth == "N" and bot.hitEast == True and bot.hitSouth == False):
        bot.moveForward(size)
    elif(bot.memWest == "N" and bot.hitSouth == True):
        print('4')

        print("trying to go west")
        bot.rotate(maze)
        bot.moveForward(size)
    elif(bot.memWest == "P" and bot.hitSouth == True):
        print('5')

        bot.rotate(maze)
        bot.rotate(maze)
        bot.moveForward(size)        
        
    return move




    
def scanAll(bot,size, maze, iMove, iRotate):
    print("Scanning all ...")
    #ALWAYS FACE SOUTH 
    while(bot.looking_at != "SOUTH"):
        print("set south")
        bot.rotate(maze)
    else:
        print("no need to set south")

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
        print("set south")
        bot.rotate(maze)
    else:
        print("no need to set south")

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

