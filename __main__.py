import pygame
from pygame.locals import *
import os


#identifyies what room the Player is in 
def first_room():
    room_doc = open("room_num.txt", "w")
    room_doc.write("1") 
    room_doc.close()
    room_doc = open("room_num.txt", "r")
    room = int(room_doc.readline(1))
    room_doc.close()
    return room 

def get_room():
    room_doc = open("room_num.txt", "r")
    room = int(room_doc.readline(1))
    room_doc.close() 
    return room 
room = get_room()

# Images Zoo 
screen = pygame.display.set_mode((500,400), pygame.HWSURFACE)
rect = pygame.draw.rect(screen,(0,0,0), (0,310,500,50))  # Menu rect
right_arrow = pygame.image.load(os.path.join("room_images","right_arrow.png")).convert()
left_arrow = pygame.image.load(os.path.join("room_images","left_arrow.png")).convert()
#room1 Images 
right_arrow_patch = pygame.image.load(os.path.join("room_images","right_arrow_patch.png")).convert()
#room2 Images 
left_arrow_room2_patch = pygame.image.load(os.path.join("room_images","left_arrow_room2_patch.png")).convert()
right_arrow_room2_patch = pygame.image.load(os.path.join("room_images","right_arrow_room2_patch.png")).convert()
#room3 images
left_arrow_room3_patch = pygame.image.load(os.path.join("room_images","left_arrow_room3_patch.png")).convert()
right_arrow_room3_patch = pygame.image.load(os.path.join("room_images","right_arrow_room3_patch.png")).convert()
# Bear
bear = pygame.image.load(os.path.join("room_images","teddy_bear.png")).convert()

# I think the room change function would be most efficent here in the the main function 
def room_change(new_room): 
    room_doc = open("room_num.txt", "w")
    room_doc.write(str(new_room)) 
    room_doc.close()
    room = get_room()
    if room == 1:
        from room1 import screen_stuff
        screen_stuff(screen)
    elif room == 2:
        from room2 import screen_stuff
        from room2 import bear_blit
        screen_stuff(screen)
        bear_blit(bear)
    elif room == 3:
        from room3 import screen_stuff
        screen_stuff(screen)
    return room 



#main game loop
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
 
    def on_init(self):
    	room = first_room()
        pygame.init()
        self._display_surf = screen
        self._running = True
        if room == 1: 
        	#import room
        	from room1 import screen_stuff
        	screen_stuff(screen)
        if room == 2:
            from room2 import screen_stuff
            screen_stuff(screen)
            bear_blit(bear)
        
        
    def on_event(self, event):
    	room = get_room() # IDK IF THIS WILL WORK 
        if event.type == QUIT:
            self._running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print pos
            if room == 1:
                from room1 import check_event
                check_event(pos)
            elif room == 2:
                from room2 import check_event
                check_event(pos) 
            elif room == 3:
                from room3 import check_event
                check_event(pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print pos 
            if room == 1:
                pass
            if room == 2: 
                from room2 import move_item
                move_item(pos, bear)
        if event.type == pygame.MOUSEMOTION:
            x,y = event.pos
            if room == 1: 
                from room1 import display_right_arrow
                display_right_arrow(x,y,right_arrow, right_arrow_patch)
            elif room == 2: 
                from room2 import display_left_arrow
                from room2 import display_right_arrow
                display_left_arrow(x,y,left_arrow, left_arrow_room2_patch)
                display_right_arrow(x,y, right_arrow, right_arrow_room2_patch)
            elif room ==3: 
                from room3 import display_left_arrow
                from room3 import display_right_arrow
                display_left_arrow(x,y,left_arrow, left_arrow_room3_patch)
                display_right_arrow(x,y, right_arrow, right_arrow_room3_patch)
          
    def on_loop(self):
        pass
    
    def on_render(self):
        pass
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()        
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()