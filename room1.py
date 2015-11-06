import pygame
from pygame.locals import *
import os
from __main__ import screen


#displays the current room background 
def screen_stuff(screen):  
    current_room =  pygame.image.load(os.path.join("room_images","testroom.png")).convert()
    screen.blit(current_room,(0,0))
    pygame.draw.rect(screen,(0,0,0), (0,310,500,50))  # creates menu bar at bottom of Room 
    pygame.display.flip()

# When a identifyible item is clicked on, this function displays a discribtion in the menu bar 
def text_to_screen(item): 
    rect = pygame.draw.rect(screen,(0,0,0), (0,310,500,50))
    pygame.display.update(rect)
    font = pygame.font.SysFont("Arial", 30)
    label = font.render("Thats a " +str(item)+ "!", 1,(255,0,0))
    screen.blit(label, (23,320))
    pygame.display.update()
    
# This function checks if an identifyible item has been clicked on and then sends that infomation to text_to_screen

def check_event(pos): 
    item = "none" # ititiates item to none 
    if pos[0] in range(160,211) and pos[1] in range(240, 256):
        print "Sink"
        item = "sink"
    elif pos[0] in range(395,500) and pos[1] in range(170, 381):
        print "Fridge"
        item = "fridge"
    elif pos[0] in range(444,497) and pos[1] in range(100, 166):
        print "Room Change" 
        from __main__ import room_change
        new_room = 2 
        room_change(new_room)
        print "room changed"
    else: # if a non-identifyible object is clicked on this will erase the menu bar 
        item = "none"
        pygame.draw.rect(screen,(0,0,0), (20,323,200,32))
        pygame.display.update(20,323,200,32)
    if item != "none":
        text_to_screen(item)


def display_right_arrow(x,y,right_arrow,right_arrow_patch):
    if ((x in range(444,497)) and (y in range(100,166))):
        right_arrow.set_colorkey((255,0,255))
        screen.blit(right_arrow,(444,100))
        pygame.display.update(444,100,53,66)
    else:
        from room1 import remove_right_arrow
        remove_right_arrow(right_arrow_patch)


def remove_right_arrow(right_arrow_patch):
    screen.blit(right_arrow_patch,(444,100))
    pygame.display.update(444,100,53,66)
    