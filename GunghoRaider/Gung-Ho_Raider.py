#-------------------------------------------------------------------------------
# Name:        Gung-Ho Raider
# Objective:   Collect as many rubies as you can
# Purpose:     School Project
#
# Author:      Karan Gupta
#
# Created:     14/10/2017
# Last Edited: 10/05/2019
# Features:
#              1) Choose difficulty level (Higher level = more speed but more score
#                 as well)
#              2) Choose Level Type (Different Types of Maps)
#              3) Store scores in a file and show high score on screen
#              4) Maneuver through Obstacles
#              5) Save character from patrolling police
#              6) Pause the game at any time
#              7) Home Screen
#              8) Restart the game after dying
#
#
# Work Log:
# 14/10/2017 => Project initiated
# 25/10/2017 => Basic framework and logic created
# 18/11/2017 => Added file handling with high score and name saving
# 19/11/2017 => Added difficulty level
# 20/11/2017 => Added obstacles
# 22/11/2017 => Added more obstacles with level type + Pause option
# 02/12/2017 => Added patroling enemies
# 10/12/2017 => Added Home Screen artwork and finishing
# 23/03/2019 => Converted from Python 2 to Python 3 file, Thought of further
#               development initiated
# 10/05/2019 => Fixed minor bugs (empty file)
# 11/05/2019 => Convert into a level based game
#
#
#-------------------------------------------------------------------------------

import pygame
import time
import random

Name = input("Enter your nickname here")
FPS = int(input("Enter difficulty level 1 to 5"))
Level_Type = int(input('''Enter level type:
1. Bars
2. Plus
3. Maze
4. Arena'''))

pygame.init()

red = (255,0,0)                                                                    #RGB codes for the required colours
blue = (0,0,255)
black = (0,0,0)
green = (0,255,0)
white = (255,255,255)
yellow = (255,255,0)
cyan = (0,255,255)
orange = (255,128,0)
maroon = (102,0,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("GUNG-HO RAIDER brought to you by KARAN GUPTA")
pygame.display.update()


clock = pygame.time.Clock()

block_size = 10                                                                     #Specifying the pixel size of the game
FPS = 10+5*FPS                                                                      #Frames per second of the game

font = pygame.font.SysFont('calibri', 25)

def enemy(block_size, EnemyList):
    image_to_screen('PrisonGuard.bmp',EnemyList[0])
    image_to_screen('PrisonGuard.bmp',EnemyList[2])

def image_to_screen(image, coordinates):
    Img = pygame.image.load(image)
    gameDisplay.blit(Img, coordinates)

def message_to_screen(msg, color, width, height):                                  #For printing text on screen
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/width, display_height/height])

obstacleList = []
if Level_Type == 1:                                                                #Obstacle list created based on choice
    #Small Bars
    for ObsX in [250.0,550.0]:
        for ObsY in range(200,400,10):
            obstacleList.append([ObsX,float(ObsY)])
    #Big Bars
    for ObsX in [100.0,700.0]:
        for ObsY in range(100,500,10):
            obstacleList.append([ObsX,float(ObsY)])

if Level_Type == 2:
    #PLUS 1
    for ObsX in range(50,350,10):
        obstacleList.append([float(ObsX),300.0])
    for ObsY in range(100,500,10):
        obstacleList.append([200.0,float(ObsY)])
    #PLUS 2
    for ObsX in range(450,750,10):
        obstacleList.append([float(ObsX),300.0])
    for ObsY in range(100,500,10):
        obstacleList.append([600.0,float(ObsY)])

if Level_Type == 3:
    #Rectangle 1
    for ObsX in range(100,710,10):
        if ObsX in range(350,450):
            obstacleList.append([float(ObsX),500.0])
        else:
            obstacleList.append([float(ObsX),500.0])
            obstacleList.append([float(ObsX),100.0])
    for ObsY in range(100,500,10):
        obstacleList.append([100.0,float(ObsY)])
        obstacleList.append([700.0,float(ObsY)])
    #Rectangle 2
    for ObsX in range(200,610,10):
        if ObsX in range(350,450):
            obstacleList.append([float(ObsX),200.0])
        else:
            obstacleList.append([float(ObsX),200.0])
            obstacleList.append([float(ObsX),400.0])
    for ObsY in range(200,400,10):
        obstacleList.append([200.0,float(ObsY)])
        obstacleList.append([600.0,float(ObsY)])

if Level_Type == 4:
    pass

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

def gameLoop():                                                                    #Reinitializing the game for restarting.
    gameExit = False
    gameOver = False
    gameStart = False
    gamePause = False

    display_width = 800
    display_height = 600
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.update()

    while not gameStart:                                                           #Home Screen Artwork
        gameDisplay.fill(maroon)
        image_to_screen("Robber.bmp", [-100,20])
        image_to_screen("PoliceAnimated.gif", [550,175])
        message_to_screen("GUNGO-HO RAIDER", white, 2.5, 2.75)
        message_to_screen("-Created by KarGo Productions", white, 3.05, 2.5)
        message_to_screen("Press ENTER to Begin", cyan, 2.75, 2)
        message_to_screen("* Collect as many rubies as you can!", white, 3.3, 1.7)
        message_to_screen("* Don't get caught by the patrolling Police!", white, 3.3, 1.6)
        message_to_screen("* P to pause the game", white, 3.3, 1.506)
        message_to_screen("ESC to quit", cyan, 1.17, 1.05)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameStart = True
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
                    gameStart = True
        pygame.display.update()


    if Level_Type == 4:
        display_width = 1200
        display_height = 700
        gameDisplay = pygame.display.set_mode((display_width,display_height))
        pygame.display.set_caption("GUNG-HO RAIDER brought to you by KARAN GUPTA")
        pygame.display.update()


    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0
    score = 0
    RaiderList = []
    if Level_Type != 4:
        EnemyList = [[50,i] for i in [50,60,550,560]]+[[60,j] for j in [50,60,550,560]]
    else:
        EnemyList = [[80,i] for i in [80,90,620,630]]+[[90,j] for j in [80,90,620,630]]




    while True:                                                                    #Generate initial Ruby
        randRubyX = round(random.randrange(0, display_width - block_size)/10.0)*10.0
        randRubyY = round(random.randrange(0, display_height - block_size)/10.0)*10.0
        if [randRubyX,randRubyY] not in obstacleList:
            break

    while not gameExit:
                                                                                   #Scoreboard using file handling
        if gameOver == True:
            score_file = open("Score.txt","r+")
            eachLine = score_file.readline()
            eachScore = 0
            eachName = ""
            if eachLine:
                eachScore = eachLine.split()[-1]
                eachName = eachLine.split()[0]
            max = 0
            maxName = ""
            if eachScore:
                max = int(eachScore)
                maxName = eachName
            try:
                while eachLine:
                    if eachLine != "\n":
                        eachScore = eachLine.split()[-1]
                        eachName = eachLine.split()[0]
                        if int(eachScore) > max:
                            max = int(eachScore)
                            maxName = eachName
                    eachLine = score_file.readline()
            except EOFError:
                pass
            score_file.close()

            score_file = open("Score.txt","a+")                                    #Write the scores onto the file
            score_file.write("%s "%Name)
            score_file.write("%d"%score)
            score_file.write("\n")
            score_file.close()

        while gameOver == True:
            gameDisplay.fill(black)
            message_to_screen("Game over, press c to play again or q to exit", red,4,2)

            if score > max:
                message_to_screen("New High Score!",blue,2.5,2.2)
                message_to_screen("High Score: %d - %s"%(score,Name),blue,2.5,1.8)
                message_to_screen("Your score: %d"%score,cyan,2.5,1.65)
            else:
                message_to_screen("Not a new High Score! Better luck next time.",blue,3.9,2.2)
                message_to_screen("HighScore: %d - %s"%(max,maxName),blue,2.5,1.8)
                message_to_screen("Your score: %d"%score,cyan,2.5,1.65)

            pygame.display.update()

            for event in pygame.event.get():                                       #Take input for restart or quit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_c:
                        gameLoop()
#-------------------------------------------------------------------------------

        for event in pygame.event.get():                                           #Key mapping for game
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                    gamePause = False
                if event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                    gamePause = False
                if event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    gamePause = False
                if event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    gamePause = False
                if event.key == pygame.K_p:
                    if gamePause == True:
                        gamePause = False
                    else:
                        gamePause = True
#-------------------------------------------------------------------------------

        if not gamePause:

            lead_x += lead_x_change
            lead_y += lead_y_change

            if lead_x < 0 or lead_x >= display_width or lead_y < 0 or lead_y >= display_height:
                gameOver = True

            gameDisplay.fill(black)
            pygame.draw.rect(gameDisplay, red, [randRubyX, randRubyY, block_size, block_size])  #Ruby
            image_to_screen('RubyNew1.bmp',[randRubyX,randRubyY])


        #OBSTACLES DRAWING IN GAME
            if Level_Type == 1:
                pygame.draw.rect(gameDisplay,green,[5*display_width/16, display_height/3, block_size, 20*block_size])
                pygame.draw.rect(gameDisplay,green,[11*display_width/16, display_height/3, block_size, 20*block_size])
                pygame.draw.rect(gameDisplay,green,[display_width/8, display_height/6, block_size, 40*block_size])
                pygame.draw.rect(gameDisplay,green,[7*display_width/8, display_height/6, block_size, 40*block_size])

            if Level_Type == 2:
                #PLUS 1
                pygame.draw.rect(gameDisplay,green,[display_width/4, display_height/6, block_size, 40*block_size])
                pygame.draw.rect(gameDisplay,green,[display_width/16, display_height/2, 30*block_size, block_size])
                #PLUS 2
                pygame.draw.rect(gameDisplay,green,[3*display_width/4, display_height/6, block_size, 40*block_size])
                pygame.draw.rect(gameDisplay,green,[9*display_width/16, display_height/2, 30*block_size, block_size])

            if Level_Type == 3:
                #Outer Rectangle
                pygame.draw.rect(gameDisplay,green,[display_width/8, display_height/6, block_size, 40*block_size])
                pygame.draw.rect(gameDisplay,green,[7*display_width/8, display_height/6, block_size, 40*block_size])
                pygame.draw.rect(gameDisplay,green,[display_width/8, 5*display_height/6, 61*block_size, block_size])
                pygame.draw.rect(gameDisplay,green,[display_width/8, display_height/6, 25*block_size, block_size])
                pygame.draw.rect(gameDisplay,green,[9*display_width/16, display_height/6, 25*block_size, block_size])
                #Inner Rectangle
                pygame.draw.rect(gameDisplay,green,[display_width/4, display_height/3, block_size, 20*block_size])
                pygame.draw.rect(gameDisplay,green,[3*display_width/4, display_height/3, block_size, 20*block_size])
                pygame.draw.rect(gameDisplay,green,[display_width/4, display_height/3, 41*block_size, block_size])
                pygame.draw.rect(gameDisplay,green,[display_width/4, 2*display_height/3, 15*block_size, block_size])
                pygame.draw.rect(gameDisplay,green,[9*display_width/16, 2*display_height/3, 16*block_size, block_size])

            if EnemyList[0][0] == 15*display_width/16 or EnemyList[0][0] == 14*display_width/15:                             #Enemy direction change and movement
                E_lead_x = -block_size
            elif EnemyList[0][0] == display_width/16 or EnemyList[0][0] == display_width/15:
                E_lead_x = block_size
            for EnemyIter in range(8):
                EnemyList[EnemyIter][0] += E_lead_x
            enemy(block_size,EnemyList)

            Raider = []
            Raider.append(lead_x)
            Raider.append(lead_y)

            if Raider in EnemyList:
                gameOver = True

            if Raider in obstacleList:
                gameOver = True

            image_to_screen('csprite.bmp', Raider)

            pygame.display.update()

            if lead_x==randRubyX and lead_y == randRubyY:                        #Generate random ruby on screen
                while True:
                   randRubyX = round(random.randrange(0, display_width - block_size)/10.0)*10.0
                   randRubyY = round(random.randrange(0, display_height - block_size)/10.0)*10.0
                   if [randRubyX,randRubyY] not in obstacleList: break

                score += FPS-5
            screen_text = font.render("SCORE: %d"%score, True, white)
            gameDisplay.blit(screen_text, [4*display_width/5,0])
            pygame.display.update()

            clock.tick(FPS)

        elif gamePause:
            message_to_screen("Game Paused Press P or Arrow Keys to continue",white,5.0,40.0)
            pygame.display.update()


    pygame.quit()
    quit()

#-------------------------------------------------------------------------------
if __name__ == '__main__': gameLoop()

