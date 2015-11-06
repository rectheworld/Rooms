import pygame
from pygame.locals import *
import os
from __main__ import screen
from __main__ import room


def screen_stuff(screen):
    current_room =  pygame.image.load(os.path.join("room_images","room2.png")).convert()
    screen.blit(current_room,(0,0))
    pygame.draw.rect(screen,(0,0,0), (0,310,500,50))
    pygame.display.flip()

#bear position

def bear_blit(bear):
    bear.set_colorkey((255,0,255))
    screen.blit(bear,(300,190))
    pygame.display.update(300,190,55,50)

def moving_bear(bear, bx, by):
    bear.set_colorkey((255,0,255))
    screen.blit(bear,(bx,by))
    pygame.display.flip()


def text_to_screen(item):
    rect = pygame.draw.rect(screen,(0,0,0), (0,310,500,50))
    pygame.display.update(rect)
    font = pygame.font.SysFont("Arial", 30)
    label = font.render("Thats a " +str(item)+ "!", 1,(255,0,0))
    screen.blit(label, (23,320))
    pygame.display.update()
    

def check_event(pos):
    item = "none"
    if pos[0] in range(349,391) and pos[1] in range(161, 205):
        print "Gatar"
        item = "gatar"
    elif pos[0] in range(0,56) and pos[1] in range(100, 166): # Move to LEft
        print "Room Change" 
        new_room = 1 
        from __main__ import room_change
        room_change(1)
    elif pos[0] in range(444,497) and pos[1] in range(100, 166): # Room change to right 
        print "Room Change" 
        new_room = 3 
        from __main__ import room_change
        room_change(3)      
    else:
        item = "none"
        pygame.draw.rect(screen,(0,0,0), (20,323,200,32))
        pygame.display.update(20,323,200,32)
    if item != "none":
        text_to_screen(item)

def move_item(pos,bear):
    bx = pos[0] # bear's x position 
    by = pos[1] # bear's y position 
    (button1, button2, button3,) = pygame.mouse.get_pressed()#get button pressed
    if button1 and (pos[0] in range(305,338) and pos[1] in range(194,235)):#check for collision between object and mouse
        (bx, by) = pygame.mouse.get_pos()#set object POS to mouse POS
        moving_bear(bear,bx,by)
    else:
        bear_blit(bear)

def display_right_arrow(x,y,right_arrow, right_arrow_room2_patch):
    if ((x in range(444,497)) and (y in range(100,166))):
        right_arrow.set_colorkey((255,0,255))
        screen.blit(right_arrow,(444,100))
        pygame.display.update(444,100,53,66)
    else:
        from room3 import remove_right_arrow
        remove_right_arrow(right_arrow_room2_patch)


def remove_right_arrow(right_arrow_room2_patch):
    screen.blit(right_arrow_patch,(444,100))
    pygame.display.update(444,100,53,66)

def display_left_arrow(x,y,left_arrow,left_arrow_room2_patch):
    if ((x in range(0,56)) and (y in range(100,166))):
        left_arrow.set_colorkey((255,0,255))
        screen.blit(left_arrow,(0,100))
        pygame.display.update(0,100,56,66)
    else:
        from room2 import remove_left_arrow
        remove_left_arrow(left_arrow_room2_patch)

def remove_left_arrow(left_arrow_room2_patch):
    screen.blit(left_arrow_room2_patch,(0,100))
    pygame.display.update(0,100,56,66)
