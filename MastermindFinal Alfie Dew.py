#Asks the user for the username input
currentplayer = [0]
playername = input("What is your player name? ")
currentplayer[0] = playername

#Imports the necessary modules for the pygame code
import pygame
import random
import time
import glob
import os

#Initialises the pygame module
pygame.init()

#intialsing variables
display_width = 800
display_height = 900

#intialising lists
currentrectxl = [50]
currentrectyl = [(display_height) - 260]
currentcolour = [0]
runtimes = [0]
countstate = [0]

storedrectcoord = []
storedcolour = []

codecolours = []
run = [0]

#colours
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
grey = (120,120,119)
dark_grey = (94, 94, 92)
brown = (135, 77, 43)
red = (255,0,0)
blue = (0,0,255)
yellow = (245, 212, 66)
dark_red = (200,0,0)
dark_blue = (0,0,200)
dark_green = (0,200,0)
dark_yellow = (199, 172, 54)
magenta = (245, 66, 230)
dark_magenta = (191, 59, 180)

#sets the list for the amount of white and red pins
whitepins =[0]
redpins = [0]
storeredpin = []
storedwhitepin = []

#sets the lists for the current location of the pins
pinyr = [(display_height) - 160]
pinyw = [(display_height) - 160]

#sets variables for the storing of pin values
pinystoredw = []
pinxstoredw = []
pinvaluestoredw = []
pinystoredr = []
pinxstoredr = []
pinvaluestoredr = []

filenames = []
listy = []
finishedloading = [False]
ran = [False]

leaderboard_player = []
leaderboard_score = []
winning = [False]
losingstatus = [0]

#defines the leaderboard function to create a text file with player results
def leaderboard():

    if winning[0] == True:
        leaderboard_player.append(currentplayer[0])
        leaderboard_score.append(int(len(storedrectcoord)/4))
        file = open("Leaderboard.txt", "a+")
        file.writelines("\n")
        file.writelines(leaderboard_player[0])
        file.writelines("        ")
        file.writelines(str(leaderboard_score))


        file.close()
        arrangedleaderboard()

#formats the leaderboard to put in order of points
def arrangedleaderboard():

    file = open("Leaderboard.txt")

    scores = {}
    linenum = []
    scorenum = []
    username = []

    lines = file.readlines()



    for i in range(4,len(lines)):
        value = lines[i]
        value = value.strip("\n")
        score = (value[-2:-1])
        line = i - 3
        scores[line] = score

    sortedscores = sorted(scores.items(), key = lambda t:t[1])

    for item in sortedscores:
        item = str(item)
        tupitem = (eval(item))
        x,y = tupitem
        linenum.append(x)
        scorenum.append(y)

    for i in range(3, len(lines)):
        userline = lines[i]
        
        user = userline[0:10]
        

    for item in linenum:
        user = lines[int(item + 3)]
        user = user[0:10]
        username.append(user)

    file.close()

    file = open("ArrangedLeaderboard.txt", "a")
    file.writelines("\n")

    for i in range(0, len(linenum)):
        position = i + 1
        file.writelines(str(position))
        file.writelines("        ")
        file.writelines(username[i])
        file.writelines("        ")
        file.writelines(scorenum[i])

    file.close()



#loads the file in order to continue a saved game
def loadfile(filename):

    file = open(filename, "r")

    lines = file.readlines()
    currentrectxl[0] = int(lines[0])
    currentrectyl[0] = int(lines[1])
    currentcolour[0] = (eval(lines[2]))
    runtimes[0] = int(lines[3])
    countstate[0] = int(lines[4])

    storedrectcoord.clear()
    lines[5] = lines[5].split(";")
    values5 = lines[5]
    del values5[-1]
    for item in values5:
        storedrectcoord.append(eval(item))

    storedcolour.clear()
    lines[6] = lines[6].split(";")
    values6 = lines[6]
    del values6[-1]
    for item in lines[6]:
        storedcolour.append(eval(item))

    codecolours.clear()
    lines[7] = lines[7].split(";")
    values7 = lines[7]
    del values7[-1]
    for item in values7:
        codecolours.append(eval(item))

    run[0] = int(lines[8])
    whitepins[0] = int(lines[9])
    redpins[0] = int(lines[10])

    storeredpin.clear()
    values11 = lines[11]
    values11 = values11[:-2]
    values11 = values11.split(",")
    for item in values11:
        print(item)
        storeredpin.append(int(item))

    storedwhitepin.clear()
    values12 = lines[12]
    values12 = values12[:-2]
    values12 = values12.split(",")
    for item in values12:
        storedwhitepin.append(int(item))

    pinyr[0] = int(lines[13])
    pinyw[0] = int(lines[14])

    pinystoredw.clear()
    values15 = lines[15]
    values15 = values15[:-2]
    values15 = values15.split(",")
    for item in values15:
        pinystoredw.append(item)

    pinxstoredw.clear()
    values16 = lines[16]
    values16 = values16[:-2]
    values16 = values16.split(",")
    for item in values16:
        pinxstoredw.append(item)

    pinvaluestoredw.clear()
    values17 = lines[17]
    values17 = values17[:-2]
    values17 = values17.split(",")
    for item in values17:
        if item != (""):
            pinvaluestoredw.append(int(item))

    pinystoredr.clear()
    values18 = lines[18]
    values18 = values18[:-2]
    values18 = values18.split(",")
    for item in values18:
        pinystoredr.append(int(item))
    
    pinxstoredr.clear()
    values19 = lines[19]
    values19 = values19[:-2]
    values19 = values19.split(",")
    for item in values19:
        pinxstoredr.append(int(item))

    pinvaluestoredr.clear()
    values20 = lines[20]
    values20 = values20[:-2]
    values20 = values20.split(",")
    for item in values20:
        if item != (""):
            pinvaluestoredr.append(int(item))

    finishedloading[0] = True
    ran[0] = True

    time.sleep(0.1)

#function in order to show the user the available text files
def loadbox():

    add = True
    filename = os.listdir("/Users/alfiedew/")

    for item in filename:
        if (item[-3:]) == "txt":
            for element in filenames:
                if item == element:
                    add == False

            if add != False:
                filenames.append(item)

#Lets the user pick a text file by printing the filenames in the game
def printfilenames():

    font = pygame.font.SysFont("Arial", 15)
    ycoordinate = 40

    for i in range(0, len(filenames)):

        add = True

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for item in listy:
            y = ycoordinate-10
            if y == item:
                add = False

        if add == True:
            listy.append(ycoordinate-10)

        if 20+300 > mouse[0] > 20 and ycoordinate-10+20 > mouse[1] > ycoordinate-10:
            pygame.draw.rect(gameDisplay,grey,[20,ycoordinate-10,300,20])
        else:
            pygame.draw.rect(gameDisplay,black,[20,ycoordinate-10,300,20])

        text = font.render(filenames[i],True,white)
        textRect = text.get_rect()
        textRect.center = (80,ycoordinate)
        gameDisplay.blit(text, textRect)

        ycoordinate += 40


    for i in range(0, len(filenames)):

        if click[0] == 1 and (20+300 > mouse[0] > 20 and (listy[i])+20 > mouse[1] > (listy[i])):
            loadfile(filenames[i])
            time.sleep(0.1)

#Creates the button for the user to load the necessary game file
def loadbutton():

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    font = pygame.font.SysFont("Arial", 30)
    text = font.render("Load", True, black)
    textRect = text.get_rect()
    textRect.center = (545,635)

    if 500+90 > mouse[0] > 500 and 610+50 > mouse[1] > 610:
        pygame.draw.rect(gameDisplay,dark_grey,[500,610,90,50])
    else:
        pygame.draw.rect(gameDisplay,grey,[500,610,90,50])

    gameDisplay.blit(text, textRect)

    if click[0] == 1 and (500+90 > mouse[0] > 500 and 610+50 > mouse[1] > 610):
        print("loaded")
        return "blackbox"
        time.sleep(0.1)

#Creates the button in order for the user to save the current progress in the game
def savebutton():

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    font = pygame.font.SysFont("Arial", 30)
    text = font.render("Save",True,black)
    textRect = text.get_rect()
    textRect.center = (545,725)
    

    if 500+90 > mouse[0] > 500 and 700+50 > mouse[1] > 700:
        pygame.draw.rect(gameDisplay,dark_grey,[500,700,90,50])
    else:
        pygame.draw.rect(gameDisplay,grey,[500,700,90,50])

    gameDisplay.blit(text, textRect)

    if click[0] == 1 and (500+90 > mouse[0] > 500 and 700+50 > mouse[1] > 700):
        time.sleep(0.1)
        saveprogress()

#Function to add each element of each list to a text file so that their progress is saved
def saveprogress():
    file = open("Saveprogress.txt", "w+")

    file.writelines(str(currentrectxl[0]))
    file.writelines("\n")
    file.writelines(str(currentrectyl[0]))
    file.writelines("\n")
    file.writelines(str(currentcolour[0]))
    file.writelines("\n")
    file.writelines(str(runtimes[0]))
    file.writelines("\n")
    file.writelines(str(countstate[0]))
    file.writelines("\n")
    for i in range(0,len(storedrectcoord)):
        file.writelines(str(storedrectcoord[i]))
        file.writelines(";")
    file.writelines("\n")
    for k in range(0,len(storedcolour)):
        file.writelines(str(storedcolour[k]))
        file.writelines(";")
    file.writelines("\n")
    for l in range(0, len(codecolours)):
        file.writelines(str(codecolours[l]))
        file.writelines(";")
    file.writelines("\n")
    file.writelines(str(run[0]))
    file.writelines("\n")
    file.writelines(str(whitepins[0]))
    file.writelines("\n")
    file.writelines(str(redpins[0]))
    file.writelines("\n")
    for m in range(0, len(storeredpin)):
        file.writelines(str(storeredpin[m]))
        file.writelines(",")
    file.writelines("\n")
    for n in range(0, len(storedwhitepin)):
        file.writelines(str(storedwhitepin[n]))
        file.writelines(",")
    file.writelines("\n")
    file.writelines(str(pinyr[0]))
    file.writelines("\n")
    file.writelines(str(pinyw[0]))
    file.writelines("\n")
    for o in range(0, len(pinystoredw)):
        file.writelines(str(pinystoredw[o]))
        file.writelines(",")
    file.writelines("\n")
    for p in range(0, len(pinxstoredw)):
        file.writelines(str(pinxstoredw[p]))
        file.writelines(",")
    file.writelines("\n")
    for q in range(0, len(pinvaluestoredw)):
        file.writelines(str(pinvaluestoredw[q]))
        file.writelines(",")
    file.writelines("\n")
    for r in range(0, len(pinystoredr)):
        file.writelines(str(pinystoredr[r]))
        file.writelines(",")
    file.writelines("\n")
    for s in range(0, len(pinxstoredr)):
        file.writelines(str(pinxstoredr[s]))
        file.writelines(",")
    file.writelines("\n")
    for t in range(0, len(pinvaluestoredr)):
        file.writelines(str(pinvaluestoredr[t]))
        file.writelines(",")
    file.writelines("\n")


    file.close()

#Checks for eligibility for a white pin
def checkingwhite():
    tempcolours = []
    tempcolours.append(storedcolour[-4])
    tempcolours.append(storedcolour[-3])
    tempcolours.append(storedcolour[-2])
    tempcolours.append(storedcolour[-1])

    for i in range(0, len(codecolours)):
        for k in range(0, len(tempcolours)):

            if codecolours[i] == tempcolours[k] and codecolours[i] != tempcolours[i]:
                whitepins[0] += 1


#function to check whether a red pin can be given
def checkingred():

    tempcolours = []
    tempcolours.append(storedcolour[-4])
    tempcolours.append(storedcolour[-3])
    tempcolours.append(storedcolour[-2])
    tempcolours.append(storedcolour[-1])

    for i in range(0, len(codecolours)):

        if codecolours[i] == tempcolours[i]:
            redpins[0] += 1
        
            
#Function to print necessary text when they win the game
def finished():
    font = pygame.font.SysFont("Arial", 60)
    text = font.render("You Win",True,black)
    textRect = text.get_rect()
    textRect.center = ((display_width)/2,(display_height)/2)
            
#function to check whether the enter button has been pressed            
def enter():
    font = pygame.font.SysFont("Arial", 30)
    text = font.render("Enter", True, black)
    textRect = text.get_rect()
    textRect.center = (545,815)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 500+90 > mouse[0] > 500 and 790+50 > mouse[1] > 790:
        pygame.draw.rect(gameDisplay,dark_grey,[500,790,90,50])
    else:
        pygame.draw.rect(gameDisplay,grey,[500,790,90,50])

    gameDisplay.blit(text, textRect)

    if click[0] == 1 and (500+90 > mouse[0] > 500 and 790+50 > mouse[1] > 790):
        time.sleep(0.1)
        checkingred()
        checkingwhite()
        pinyr[0] -= 70
        pinyw[0] -= 70

#function to set whether a pin can be given, the value of that pin then changes
def pintext():

    ycoordinate = (display_height) - 160
    xcoordinate = 415
    redno = redpins[0]
    whiteno = whitepins[0]

    font = pygame.font.SysFont("Arial", 30)
    
    for i in range(0,10):

        if ycoordinate == pinyr[0]:
            text = font.render(str(redno),True,white)
            textRect = text.get_rect()
            addarraypinsr(ycoordinate,xcoordinate,redno)
            textRect.center = (xcoordinate,ycoordinate)
        else:
            text = font.render("0",True,white)
            textRect = text.get_rect()
            textRect.center = (xcoordinate,ycoordinate)

        for k in range(0,len(pinystoredr)):
            if pinystoredr[k] == ycoordinate - 70:
                value = storeredpin[k]
                text = font.render(str(value),True,white)
                textRect = text.get_rect()
                textRect.center = (xcoordinate,ycoordinate)

        
        gameDisplay.blit(text,textRect)
        ycoordinate -= 70


    ycoordinate = (display_height) - 160
    xcoordinate += 40
    for i in range(0,10):

        if ycoordinate == pinyw[0]:
            text = font.render(str(whiteno),True,red)
            textRect = text.get_rect()
            addarraypinsw(ycoordinate,xcoordinate,whiteno)
            textRect.center = (xcoordinate,ycoordinate)
        else:
            text = font.render("0",True,red)
            textRect = text.get_rect()
            textRect.center = (xcoordinate,ycoordinate)

        for k in range(0,len(pinystoredw)):
            if pinystoredw[k] == ycoordinate - 70:
                value = storedwhitepin[k]
                text = font.render(str(value),True,red)
                textRect = text.get_rect()
                textRect.center = (xcoordinate,ycoordinate)

        gameDisplay.blit(text,textRect)
        ycoordinate -= 70

#Adds the pins to the array so they can be saved when the display refreshes
def addarraypinsw(ycoord,xcoord,whitepin):

    settingy = True

    for item in pinystoredw:
        if ycoord == item:
            settingy = False

    if settingy != False:
        pinystoredw.append(ycoord)
        pinxstoredw.append(xcoord)
        storedwhitepin.append(whitepins[0])
        whitepins[0] = 0

#function to add to the arrays, pinystoredr,pinxstoredr and pinvaluestoredr the pin values for previous rows
def addarraypinsr(ycoord,xcoord,redpin):

    settingy = True

    for item in pinystoredr:
        if ycoord == item:
            settingy = False

    if settingy != False:
        pinystoredr.append(ycoord)
        pinxstoredr.append(xcoord)
        storeredpin.append(redpins[0])
        redpins[0] = 0

#function to add to the array the colours of the entered blocks
def addarray(x,y,colour):

    coordstate = True

    coords = (x,y)
    for i in range(0,len(storedrectcoord)):
        if coords == storedrectcoord[i]:
            coordstate = False
            
    if coordstate != False:
        storedrectcoord.append(coords)
        storedcolour.append(colour)
    
#function to set up the random colours that the user has to guess
def randomcode():
    colour_options = [red,blue,green,yellow,magenta]
    digit = random.randint(0,4)
    firstcolour = colour_options[digit]
    codecolours.append(firstcolour)
    print(firstcolour)

    digit = random.randint(0,4)
    secondcolour = colour_options[digit]
    codecolours.append(secondcolour)
    print(secondcolour)

    digit = random.randint(0,4)
    thirdcolour = colour_options[digit]
    codecolours.append(thirdcolour)
    print(thirdcolour)

    digit = random.randint(0,4)
    fourthcolour = colour_options[digit]
    codecolours.append(fourthcolour)
    print(fourthcolour)

#draws the main rectangles of the window    
def drawrectangle(color,xcoord, ycoord, width, height):

    pygame.draw.rect(gameDisplay, color, [xcoord, ycoord, width, height])

#function to set up the placeholder squares
def placeholders():

    
    xcoordinate = (120)
    ycoordinate = (display_height) - 890

    for i in range(0,11):
        for j in range(0,4):
            if currentrectxl[0] == xcoordinate and currentrectyl[0] == ycoordinate:
                rectangle = pygame.draw.rect(gameDisplay, currentcolour[0], [xcoordinate,ycoordinate,60,60])
                addarray(xcoordinate,ycoordinate,currentcolour[0])
            if losingstatus[0] == 1:
                if xcoordinate == 120 and ycoordinate == (display_height)-890:
                    pygame.draw.rect(gameDisplay, codecolours[0], [120,(display_height)-890,60,60])
                    pygame.draw.rect(gameDisplay, black, [120,(display_height)-890,60,60],2)
                if xcoordinate == 190 and ycoordinate == (display_height)-890:
                    pygame.draw.rect(gameDisplay, codecolours[1], [190,(display_height)-890,60,60])
                    pygame.draw.rect(gameDisplay, black, [190,(display_height)-890,60,60],2)
                if xcoordinate == 260 and ycoordinate == (display_height)-890:
                    pygame.draw.rect(gameDisplay, codecolours[2], [260,(display_height)-890,60,60])
                    pygame.draw.rect(gameDisplay, black, [260,(display_height)-890,60,60],2)
                if xcoordinate == 330 and ycoordinate == (display_height)-890:
                    pygame.draw.rect(gameDisplay, codecolours[3], [330,(display_height)-890,60,60])
                    pygame.draw.rect(gameDisplay, black, [330,(display_height)-890,60,60],2)
            else:
                pygame.draw.rect(gameDisplay, grey, [xcoordinate,ycoordinate,60,60])
                pygame.draw.rect(gameDisplay, black, [xcoordinate,ycoordinate,60,60],2)
            xcoordinate += 70
        xcoordinate = 120
        ycoordinate += 70

    if losingstatus[0] == 1:
                
        pygame.draw.rect(gameDisplay, codecolours[0], [120,710,60,60])
        pygame.draw.rect(gameDisplay, codecolours[1], [190,710,60,60])       
        pygame.draw.rect(gameDisplay, codecolours[2], [260,710,60,60])           
        pygame.draw.rect(gameDisplay, codecolours[3], [330,710,60,60])

    for k in range(0,len(storedrectcoord)):
        x,y = storedrectcoord[k]
        pygame.draw.rect(gameDisplay, storedcolour[k], [x,y,60,60])
    
#function to draw the pins    
def pins():

    xcoordinate = (400)
    ycoordinate = (display_height) - 820

    for i in range(0,10):
        xcoordinate = 400
        pygame.draw.rect(gameDisplay, red,[xcoordinate,ycoordinate,30,60])
        xcoordinate += 40
        pygame.draw.rect(gameDisplay, white,[xcoordinate,ycoordinate,30,60])
        ycoordinate += 70

    
#sets of functions in order to create the rectangle and colour of the rectangles of the blocks
def redbutton(colour):
    pygame.draw.rect(gameDisplay, colour, [120,(display_height) - 120,60,60])
    pygame.draw.rect(gameDisplay, black, [120,(display_height) - 120,60,60], 2)

def greenbutton(colour):
    pygame.draw.rect(gameDisplay, colour, [190,(display_height) - 120,60,60])
    pygame.draw.rect(gameDisplay, black, [190,(display_height) - 120,60,60], 2)

def bluebutton(colour):
    pygame.draw.rect(gameDisplay, colour, [260,(display_height) - 120,60,60])
    pygame.draw.rect(gameDisplay, black, [260,(display_height) - 120,60,60], 2)

def yellowbutton(colour):
    pygame.draw.rect(gameDisplay, colour, [330,(display_height) - 120,60,60])
    pygame.draw.rect(gameDisplay, black, [330,(display_height) - 120,60,60], 2)

def magentabutton(colour):
    pygame.draw.rect(gameDisplay, colour, [400,(display_height) - 120,60,60])
    pygame.draw.rect(gameDisplay, black, [400,(display_height) - 120,60,60], 2)

#function to change the colour of the blocks if the mouse is hovering over it
def buttonhover():
    mouse = pygame.mouse.get_pos()

    if 120+60 > mouse[0] > 120 and ((display_height-120)+60 > mouse[1] > (display_height-120)):
        redbutton(dark_red)
    if 190+60 > mouse[0] > 190 and ((display_height-120)+60 > mouse[1] > (display_height-120)):
        greenbutton(dark_green)
    if 260+60 > mouse[0] > 260 and ((display_height-120)+60 > mouse[1] > (display_height-120)):
        bluebutton(dark_blue)
    if 330+60 > mouse[0] > 330 and ((display_height-120)+60 > mouse[1] > (display_height-120)):
        yellowbutton(dark_yellow)
    if 400+60 > mouse[0] > 400 and ((display_height-120)+60 > mouse[1] > (display_height-120)):
        magentabutton(dark_magenta)

#function to register a click of the mouse and then change the colour of the placeholders
def buttonclick():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0] == 1 and (120+60 > mouse[0] > 120 and ((display_height-120)+60 > mouse[1] > (display_height-120))):
        currentrect(red)
        runtimes[0] += 1
        time.sleep(0.15)
    if click[0] == 1 and (190+60 > mouse[0] > 190 and ((display_height-120)+60 > mouse[1] > (display_height-120))):
        currentrect(green)
        runtimes[0] += 1
        time.sleep(0.15)
    if click[0] == 1 and (260+60 > mouse[0] > 260 and ((display_height-120)+60 > mouse[1] > (display_height-120))):
        currentrect(blue)
        runtimes[0] += 1
        time.sleep(0.15)
    if click[0] == 1 and (330+60 > mouse[0] > 330 and ((display_height-120)+60 > mouse[1] > (display_height-120))):
        currentrect(yellow)
        runtimes[0] += 1
        time.sleep(0.15)
    if click[0] == 1 and (400+60 > mouse[0] > 400 and ((display_height-120)+60 > mouse[1] > (display_height-120))):
        currentrect(magenta)
        runtimes[0] += 1
        time.sleep(0.15)

#function which stores the current state of the coordinates and changes the coords once the colour has been picked
def currentrect(clickedcolour):
    if runtimes[0] == 0:
        currentrectxl[0] = 120
        currentrectyl[0] = (display_height) - 190
    else:
        currentrectxl[0] = currentrectxl[0] + 70

    currentcolour[0] = clickedcolour
    if countstate[0] % 4 == 0 and countstate[0] != 0:
        currentrectxl[0] = 120
        currentrectyl[0] = currentrectyl[0] - 70
    countstate[0] += 1

#function to create the title of the game
def title():
    font = pygame.font.SysFont("Freesans", 70)
    text = font.render("Mastermind", True, red)
    textRect = text.get_rect()
    textRect.center = (550,40)    
    gameDisplay.blit(text,textRect)


gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Mastermind")

clock = pygame.time.Clock()

randomcode()

#Sets the variables for the game to begin
quitting = False
paused = False

running = 0
won = False
lose = False

while not quitting:

    #Lets the pygame module take the event data
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitting = True

    #fills the display white
    gameDisplay.fill(white)
            
    #Runs the main necessary functions for the game to play
    drawrectangle(brown,(display_width)/2 - 300,0,400,display_height)
    drawrectangle(brown,500,0,200,display_height )
    title()
    placeholders()
    redbutton(red)
    greenbutton(green)
    bluebutton(blue)
    yellowbutton(yellow)
    magentabutton(magenta)
    pins()
    pintext()

    #Allows for the game to be stopped if the user loads a new file
    loadingfile = loadbutton()
    if loadingfile == "blackbox":
        running = 1
        loadbox()
        time.sleep(0.1)

    if running == 1:
        drawrectangle(black,10,10,400,400)
        printfilenames()
        
    if finishedloading[0] == True:
        running = 0

    if running == 0:
        buttonhover()
        buttonclick()
        enter()

        if redpins[0] == 4:
            won = True
            winning[0] = True

        if len(storedrectcoord) == 40:
            lose = True

    #Condition to decide whether the user has won or lost
    if lose == True and won != True:
        drawrectangle(white,200,370,(display_width)/2,50)
        font = pygame.font.SysFont("Arial", 80)
        text = font.render("You have lost", True, black)
        textRect = text.get_rect()
        textRect.center = (400,400)
        gameDisplay.blit(text, textRect)
        losingstatus[0] = 1

    if won == True:
        drawrectangle(white,200,370,(display_width)/2,50)
        font = pygame.font.SysFont("Arial", 80)
        text = font.render("You have won",True,black)
        textRect = text.get_rect()
        textRect.center = (400,400)
        gameDisplay.blit(text, textRect)

    savebutton()
    loadbutton()

    #updates the display
    pygame.display.update()

    clock.tick(60)


#updates the leaderboard if the user has won
leaderboard()
pygame.display.quit()
quit()
