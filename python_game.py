import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')
pygame.display.update()

clock = pygame.time.Clock()

block_size = 20
FPS = 10

smallfont = pygame.font.SysFont(None, 25)
medfont = pygame.font.SysFont(None, 50)
largefont = pygame.font.SysFont(None, 80)

def pause():
    paused = True

    while paused:
        gameDisplay.fill(white)
        message_to_screen("Paused", black, -100, size= "large")
        message_to_screen("Press c to play and q to quit",
                          black,
                          25)
        pygame.display.update()
        clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

                gameDisplay.fill(white)
                message_to_screen("Paused", black, -100, size= "large")
                message_to_screen("Press c to play and q to quit",
                                  black,
                                  25)
                pygame.display.update()
                clock.tick(5)

def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text,[0,0])
    

def snake(block_size, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    
    return textSurface, textSurface.get_rect()
    

def message_to_screen(msg,color,y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    #screen_text = font.render(msg, True, color)
    #gameDisplay.blit(screen_text, [display_width/2,display_height/2])
    textRect.center = (display_width/2), (display_height/2)+y_displace
    gameDisplay.blit(textSurf, textRect)


def game_intro():
    intro = True
    while intro == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                    gameloop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()


                
        gameDisplay.fill(white)
        message_to_screen("Welcome to slither", green , -100, size = "large")
        message_to_screen("The objective of the game is to eat red apples ", black, -30, "small")
        message_to_screen("The more apples you eat the longer you get", black, 10, "small")
        message_to_screen("If you run into yourself or the edges, you die", black, 50, "small")
        message_to_screen("Press c to play or q to quit", black, 80, "small")
        pygame.display.update()
        clock.tick(15)

def gameloop():
    gameExit = False
    gameOver = False
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0

    snakelist = []
    snakelength = 1

    randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
    
    while not gameExit:
        
        while gameOver == True :
            gameDisplay.fill(white)
            message_to_screen("Game over",red,-50, size="large")
            message_to_screen("Press c to play again or q to quit", black, 50)
            pygame.display.update()

            for event in pygame.event.get() :
                if event.type == pygame.QUIT:
                    gameover = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameExit = True

                    if event.key == pygame.K_c:
                        gameloop()

                    
                        

            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                        pause()
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
    

            if lead_x >= display_width or lead_x<0 or lead_y >= display_height or lead_y <0 :
                gameOver = True 
                    
        lead_x +=lead_x_change
        lead_y +=lead_y_change 
        gameDisplay.fill(white)
        applethickness= 30
        pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,applethickness, applethickness])

        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakelist.append(snakeHead)

        if len(snakelist) > snakelength:
            del snakelist[0]

        for eachSegment in snakelist[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
        
        snake(block_size, snakelist)
        score(snakelength-1)

        
        pygame.display.update()

        """if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
            randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
            snakelength +=1"""

        '''if lead_x >= randAppleX and lead_x<=randAppleX+applethickness:
            if lead_y >= randAppleY and lead_y<=randAppleY+applethickness:
                randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
                randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
                snakelength +=1'''

        if lead_x > randAppleX and lead_x < randAppleX + applethickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + applethickness:
            #print("x crossover")
            if lead_y > randAppleY and lead_y < randAppleY+ applethickness or lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + applethickness:
                    randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
                    randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
                    snakelength +=1


        clock.tick(FPS)
                

    pygame.quit()
    quit()

game_intro()
gameloop()
