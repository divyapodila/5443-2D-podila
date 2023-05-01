import copy
import pygame as py
import os, random
from pprint import pprint
from simple_comms import Simple_Comms
from multiplayer import Multiplayer

WIDTH = 1400
HEIGHT = 800
tiles_x = 2
tiles_y = 3

class GameObject(py.sprite.Sprite):
    screen = None
    current_view = None
    def __init__(self, space_coordinates, vector, img):
        # velocity and movement
        self.vector = vector            
        self.screen_coordinates = tuple(space_coordinates)
        self.space_coordinates = copy.deepcopy(space_coordinates)
        self.img = img                             
        self.rect = self.img.get_rect()
        #angle of ship
        self.angle = self.find_angle(vector)
        py.sprite.Sprite.__init__(self)

    def get_location_on_screen():
        pass


    #Updates the location of the GameObject based on the space_location
    def screen_location_update(self):
        x = self.space_coordinates[0] - self.current_view[0]
        y = self.space_coordinates[1] - self.current_view[1]
        self.screen_coordinates = (x, y)


    def find_angle(self, vector):
        return vector.angle_to(py.Vector2(1, 0))
    
    def draw_entity(self):
        rot_img = py.transform.rotate(self.img, self.angle)
        x, y = self.screen_coordinates
        self.screen.blit(rot_img, (x - rot_img.get_width()//2, y - rot_img.get_width()//2))
        #ship health bar
        if type(self) == Ship:
            bar_width = self.health/2

            bar_width = self.health/2
            #green color for health >60%
            if self.health > 60:                 
                color = (0, 255, 0)
            #Yellow color for health >30%
            elif self.health > 30:              
                color = (255, 255, 0)
            else:
            #Red color for health <30%                               
                color = (255, 0, 0)
            py.draw.rect(self.screen, color, py.Rect(x -(bar_width/2), y+32, bar_width, 10))


    #To update Location of an object on screen
    def space_location_update(self):

        #x-coordinates
        new_xpos = self.space_coordinates[0] + self.vector[0]
        new_ypos = self.space_coordinates[1] + self.vector[1]
        in_universe = True
        if new_xpos > 0 and new_xpos < WIDTH*tiles_x:
            self.space_coordinates[0] = new_xpos
        else:
            in_universe = False
        if new_ypos > 0 and new_ypos < HEIGHT*tiles_y:
            self.space_coordinates[1] = new_ypos
        else:
            in_universe = False
        self.rect[0] = self.space_coordinates[0]
        self.rect[1] = self.space_coordinates[1]
        return in_universe

class Ship(GameObject):
    ship_size = (60, 60)

    def __init__(self, space_coordinates=[], vector=py.math.Vector2(1, 0)):
        self.comms = Simple_Comms()
        self.multiplayer = Multiplayer()
        #ship's health
        self.health = 100  
        #initialize number of kills                     
        self.kills = 0  
        #scoreboard of player info and number of kills for each                        
        self.leaderboard = []                  
        self.dead = False                      
        self.respawn_timer = 0
        self.prev_vector=None
        self.font = py.font.Font("assets/Font/Staatliches-Regular.ttf", 30)
        self.small_font = py.font.Font("assets/Font/Staatliches-Regular.ttf", 25)
        # Add a random Ship
        ship_files = os.listdir("assets/ships")     
        ship_files.remove('.DS_Store')
        ship_files.sort()
        ship_choice = random.randint(0, len(ship_files)-1)
        ship_file = ship_files[ship_choice]
        ship = py.image.load(f'assets/ships/{ship_file}')
        ship = py.transform.scale(ship, Ship.ship_size)
        
        #Bullet lazer images randomly
        bullet_file = random.choice(os.listdir("assets/bullets"))      
        while bullet_file == '.DS_Store':
            bullet_file = random.choice(os.listdir("assets/bullets")) 
        self.bullet_color = bullet_file

        #Initial random coordinates
        if space_coordinates == []:
            space_coordinates.append(random.randint(100, tiles_x*WIDTH-100)) 
            space_coordinates.append(random.randint(100, tiles_y*HEIGHT-100))    
        GameObject.__init__(self, space_coordinates, vector, ship)

        self.gun = Ship_Type()


        # message passing to Local players added
        self.message = {
            'space coord': copy.deepcopy(self.space_coordinates),
            'img':          ship_choice,
            'killed by':    '',
            'kills':        self.kills,
            'angle':        self.angle,
            'health':       self.health,
            'bullet info':  self.gun.message   
        }

    def player_dead(self):
        self.health = 100
        self.dead=False
    #Update the messages of each player everytime 
    def update_message(self):
        self.message['space coord'] = copy.deepcopy(self.space_coordinates)
        self.message['angle'] = self.angle
        self.message['health'] = self.health
        self.message['kills'] = self.kills
        self.message['bullet info'] = self.gun.message

    def update_screen(self):
        white = (255,255,255)
        gray = (30,30,50)
        # displays the % Health left
        health_text = self.font.render(f"Health: {self.health}", False, "#b714ba")
        health_text_rect = health_text.get_rect()
        health_text_rect.midleft = (WIDTH-150, 20)
        self.screen.blit(health_text, health_text_rect)
        

        # displays the AMO of the gun. Amount of attack / damage it can cause
        amo_text = self.font.render(f"Attack: {self.gun.attributes['ammo']}", False,"#b714ba")
        amo_text_rect = amo_text.get_rect()
        amo_text_rect.midleft = (WIDTH-150, 60)
        self.screen.blit(amo_text, amo_text_rect)
        self.leaderboard.clear()
        self.leaderboard.append((self.kills, self.comms.player))

        for enemy, message in self.comms.message.items():
            self.leaderboard.append((message['kills'], enemy))
        self.leaderboard.sort(reverse=True)
        leaderboard_header_text = self.font.render(f"Player          Score", False,"#b714ba")
        leaderboard_header_rect = leaderboard_header_text.get_rect()
        leaderboard_header_rect.topleft = (50, 10)
        self.screen.blit(leaderboard_header_text, leaderboard_header_rect)

        for count, stat in enumerate(self.leaderboard):
            leaderboard_text = self.small_font.render(f"{stat[1]}          {stat[0]}", False, "#b714ba")
            leaderboard_rect = leaderboard_text.get_rect()
            leaderboard_rect.topleft = (50, 40+(count*20))
            self.screen.blit(leaderboard_text, leaderboard_rect)

        player_text = self.font.render(f"{self.comms.player}", False,"#b714ba")
        player_text_rect = player_text.get_rect()
        player_text_rect.center = (WIDTH/2, 20)
        self.screen.blit(player_text, player_text_rect)
        

    def update_ship(self):

        self.handle_keys()
        self.space_location_update()
        self.screen_location_update()
        self.draw_entity()
        self.update_screen()
        self.update_message()
        self.comms.send(self.message)
        self.message['killed by'] = ''
        self.multiplayer.display_enemies(self.comms.message, self)
        self.multiplayer.update(self.comms.message, self)

        if self.dead:
            self.player_dead()
        self.gun.update(self.comms.message)
        for kill,player in self.leaderboard:
            if kill>4:
                return player

    #Keyboard inputs
    def handle_keys(self):
        key = py.key.get_pressed()

        if key[py.K_RIGHT]: 
            self.angle -= 5
            self.vector = self.vector.rotate(5)
            if self.prev_vector!=None:
                self.prev_vector=self.prev_vector.rotate(5)
            if self.angle < -360:
                self.angle += 360
        elif key[py.K_LEFT]:
            self.angle += 5 
            self.vector = self.vector.rotate(-5)
            if self.prev_vector!=None:
                self.prev_vector=self.prev_vector.rotate(-5)
            if self.angle > 360:
                self.angle -= 360
        #setting velocity of ship
        max_speed = 10
        min_speed = 0
        if key[py.K_UP] and (self.vector.magnitude() <= max_speed):
            if self.vector.magnitude()==0:
                self.vector=self.prev_vector.copy()
            self.vector *= 1.1 
        #To stop the ship abruptly if down arrow key is pressed. vel=0    
        elif key[py.K_DOWN] and (self.vector.magnitude() >= min_speed):
            if self.vector.magnitude()<1 and self.vector.magnitude()!=0:
                self.prev_vector=self.vector.copy()
                self.vector *=0
            else:
                self.vector *= .95

    def shoot(self):
        v=self.vector
        if self.vector.magnitude()==0:
            v=self.prev_vector
        self.gun.shoot(v, self.space_coordinates)

class Ship_Type():
    clock = None
    def __init__(self):
        bullet_files = os.listdir("assets/bullets")
        bullet_files.remove('.DS_Store')     
        bullet_files.sort()
        bullet_choice = random.randint(0, len(bullet_files)-1)
        bullet_file = bullet_files[bullet_choice]
        img = py.image.load(f'assets/bullets/{bullet_file}')
        scaler = .2
        self.bullet_image = py.transform.scale_by(img, scaler)
        self.bullet_sound = py.mixer.Sound('sounds/bullet_sound1.wav')
        py.mixer.Sound.set_volume(self.bullet_sound, 0.2)
        gun_types = [
            {"ammo": 10, 'reload':1000, 'attack': 8, 'speed': 10},
            {"ammo": 20, 'reload':3000, 'attack': 5, 'speed': 12},
            {"ammo": 4, 'reload':2000, 'attack': 17, 'speed': 10},
            {"ammo": 2, 'reload':3000, 'attack': 40, 'speed': 9}
        ]
        # chooses a random gun type
        self.attributes = random.choice(gun_types)          
        self.bullets = []  
        #number of bullet's in magazine                                 
        self.bullets_in_mag = self.attributes['ammo'] 
        #reload of gun    
        self.reloading = False                              
        self.reload_start_t = 0                    
        self.reload_time_left = 0
        self.message = {
            'shooting': False,
            'attack':   self.attributes['attack'],
            'img':      bullet_choice,
            'bullets':  []
        }

    def check_collision(self, messages):
        hits = []
        #reads messages from local players
        for message in messages.values():
            enemy_rect = py.Rect((message['space coord'][0], message['space coord'][1]), (60, 60))
            enemy_rect = enemy_rect.scale_by(.8)

            for bullet in self.bullets:
                if enemy_rect.colliderect(bullet.rect):
                    hits.append(bullet)

        for hit in hits:
            self.bullets.remove(hit)


    def shoot(self, vector, space_coord):
        if self.bullets_in_mag > 0:
            self.bullets_in_mag -= 1                      
            vec = py.math.Vector2.normalize(vector)    
            speed = self.attributes['speed']
            self.bullets.append(Bullet(copy.deepcopy(space_coord), vec*speed, self.bullet_image))
            py.mixer.Sound.play(self.bullet_sound)
            self.message['shooting'] = True
            if (self.bullets_in_mag <= 0 and self.reloading == False):
                self.reloading = True
                self.reload_start_t = Ship_Type.clock.get_ticks()
            
    def update(self, messages):
        self.bullets = [bullet for bullet in self.bullets if bullet.space_location_update()]
        self.message['bullets'].clear()
        for bullet in self.bullets:
            bullet.space_location_update()
            bullet.screen_location_update()
            bullet.draw_entity()
            self.message['bullets'].append(
                {
                    'space coord':  copy.deepcopy(bullet.space_coordinates),
                    'angle':        bullet.angle
                }
            )

        #bullet to enemy ship collision detection
        self.check_collision(messages)
        self.message['shooting'] = False
        if self.reloading:
            # check how much reload time is left
            self.reload_time_left = self.reload_start_t + self.attributes['reload'] - Ship_Type.clock.get_ticks()
            # check if the reload is done
            if self.reload_start_t + self.attributes['reload'] <= Ship_Type.clock.get_ticks():
                self.reloading = False
                self.bullets_in_mag = self.attributes['ammo']

class Bullet(GameObject):
    id = 0
    def __init__(self, space_coordinates, vector, bullet_img):
        Bullet.id += 1
        self.id = Bullet.id
        GameObject.__init__(self, space_coordinates, vector, bullet_img)

