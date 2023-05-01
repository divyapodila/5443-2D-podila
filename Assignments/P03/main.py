import pygame as py
import copy
import random
from background import set_scrollers, move_screen 
from ship import Ship, Bullet, GameObject, Ship_Type
from gameClass import GameClass
from astroids import Asteroid


py.init()

# game variables
tiles_x = 2
tiles_y = 3
WIDTH = 1400
HEIGHT = 800
asteroids = []
ship_group = py.sprite.Group()
screen = py.display.set_mode([WIDTH, HEIGHT])

#setting space theme music for the game 
py.mixer_music.load("sounds/music.mp3")
py.mixer_music.play(1)

#setting logo and button for start game
logo = py.image.load("assets/logo.png").convert_alpha()
button = py.image.load("assets/button.png").convert_alpha()
font=py.font.Font("assets/Font/Staatliches-Regular.ttf", 60)
font_big=py.font.Font("assets/Font/Staatliches-Regular.ttf", 30)

#background
background = py.image.load('assets/spaceBackground.png')
background = py.transform.smoothscale(background, (WIDTH, HEIGHT))
bg_width = background.get_width()        
bg_height = background.get_height()                             
start_rect=button.get_rect()
start_rect.topleft=(WIDTH/2-button.get_width()/2,400)

MENU=True
CLOSED=False
while MENU:
    for event in py.event.get():
        if event.type == py.QUIT:
            CLOSED=not CLOSED
            MENU = not MENU
            break
        if event.type == py.MOUSEBUTTONDOWN:
            if event.button==1 and start_rect.collidepoint(py.mouse.get_pos()):
                MENU = not MENU
                print("STARTED")
                break
    if CLOSED:
        break
    for x in range(tiles_x):
        for y in range(tiles_y):
            screen.blit(background, (x * bg_width + 0, y * bg_height + 0))

    screen.blit(logo,(WIDTH/2-logo.get_width()/2,180))
    screen.blit(button,(WIDTH/2-button.get_width()/2,400))
    
    py.display.update()

if not CLOSED:
    #new ship added
    ship = Ship()
    ship_group.add(ship)
    #player ships blit on screen at random
    print(ship_group.sprites())
    clock = py.time.Clock()
    fps = 50
    Ship_Type.clock = py.time
    py.display.set_caption("GALAXY WARS!!")
    GameObject.screen = screen

    # import pygame scrollers for screen movement based on co-ordinates
    scroll_x, scroll_y = set_scrollers(ship, [WIDTH, HEIGHT], [tiles_x, tiles_y])

    #asteroids
    for i in range(30):
        asteroids.append(Asteroid())
    winner=None
    running = True
    while running:  
        
        GameObject.current_view = (-scroll_x, -scroll_y, -scroll_x+bg_width, -scroll_y+bg_width)
        clock.tick(fps)
        # Blit Background screen image
        for x in range(tiles_x):
            for y in range(tiles_y):
                screen.blit(background, (x * bg_width + scroll_x, y * bg_height + scroll_y))

        for event in py.event.get():
            if event.type == py.QUIT:
                running = False

            #Hit space button to shoot when key pressed
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    ship.shoot()

        #asteroids on the screen
        asteroids = [asteroid for asteroid in asteroids if asteroid.space_location_update()]
        for asteroid in asteroids:
            asteroid.screen_location_update()
            asteroid.draw_entity()

        while(len(asteroids) < 30):
            asteroids.append(Asteroid())
        scroll_x, scroll_y = move_screen(scroll_x, scroll_y, ship, WIDTH, HEIGHT, tiles_x, tiles_y)
        w=ship.update_ship()
        if w!=None:
            running=False
            winner=w
        py.display.flip() 
        
    END_MENU=True
    try:
        while END_MENU and not CLOSED:
            for event in py.event.get():
                if event.type == py.QUIT:
                    CLOSED=not CLOSED
                    END_MENU = not END_MENU
                    break
                if event.type == py.MOUSEBUTTONDOWN:
                    if event.button==1 and start_rect.collidepoint(py.mouse.get_pos()):
                        MENU = not MENU
                        print("STARTED")
                        break
            if CLOSED:
                break
            for x in range(tiles_x):
                for y in range(tiles_y):
                    screen.blit(background, (x * bg_width + 0, y * bg_height + 0))
            #Game over text display
            text=font.render("Game Over",True,"#b714ba")
            screen.blit(text,(WIDTH/2-text.get_width()/2,200))
            
            #displaye which player wins
            text=font.render(w+" WINS",True,"#b714ba")
            screen.blit(text,(WIDTH/2-text.get_width()/2,300))
            
            py.display.flip() 
    except:
        pass
    
py.quit() 