import pygame as py
import os


class Multiplayer:

    def __init__(self):

        self.players = {}

        self.ship_imgs = self.load_ships_imgs()
        self.bullet_imgs = self.load_bullet_imgs()
        self.bullet_sound = self.load_bullet_sound()


    def update(self, messages, ship):
        
    
        for player, message in messages.items():

            if player not in self.players:
                self.players[player] = Enemy_Player(
                    player,
                    self.ship_imgs[message['img']],
                    self.bullet_imgs[message['bullet info']['img']],
                    message['bullet info']['damage'],
                    message['space coord']
                )

            self.update_player(self.players[player], message)

            if message['killed by'] == ship.comms.player:
                ship.kills += 1
                print(f"{ship.comms.player} Killed {player}")
                print(f"Total kills: {ship.kills}")

            collision_sprites = self.bullet_collision(ship, self.players[player].bullet_group)
            if collision_sprites:
                print(collision_sprites)
                ship.health -= self.players[player].dmg
                print(f"health: {ship.health}")

                if ship.health < 0:
                    ship.message['killed by'] = self.players[player].player
                    ship.dead = True
    #bullet collision and ship
    def bullet_collision(self, ship, bullet_group):
        hits = []
        for count, bullet in enumerate(bullet_group):

            #If there is a collision
            if ship.rect.scale_by(.8).colliderect(bullet):
                hits.append(count)
                print('hit')
        return hits
    
    def update_player(self, player, message):

        player.space_coord = message['space coord']
        player.health = message['health']
        player.angle = message['angle']
        player.rect[0], player.rect[1] = player.space_coord[0], player.space_coord[1]
        player.bullets.clear()
        player.bullet_group.empty()
        for bullet in message['bullet info']['bullets']:
            rectangle = py.transform.rotate(player.bullet_img, bullet['angle']).get_rect()
            rectangle[0], rectangle[1] = bullet['space coord'][0], bullet['space coord'][1]
            player.bullets.append(
                Enemy_Bullet(
                    rectangle,
                    bullet['space coord'],
                    bullet['angle']
                )
            )
            player.bullet_group.add(player.bullets[-1])
    def display_enemies(self, messages, ship):
        for sender in messages.values():
            ship_screen_coords = self.screen_location_update(sender['space coord'], ship)
            if (ship_screen_coords[0] > -40 and ship_screen_coords[0] < 1440 and 
                    ship_screen_coords[1] > -40 and ship_screen_coords[1] < 840):
                
                self.draw_ship(ship_screen_coords, sender['img'], sender['angle'], sender['health'], ship)
                if sender['bullet info']['shooting']:
                    py.mixer.Sound.play(self.bullet_sound)

            for bullet in sender['bullet info']['bullets']:
                bullet_screen_coords = self.screen_location_update(bullet['space coord'], ship)
                if (bullet_screen_coords[0] > -40 and bullet_screen_coords[0] < 1440 and 
                    bullet_screen_coords[1] > -40 and bullet_screen_coords[1] < 840):
                    self.draw_bullet(bullet_screen_coords, sender['bullet info']['img'], bullet['angle'], ship)

    def screen_location_update(self, space_coordinates, ship):
        x = space_coordinates[0] - ship.current_view[0]
        y = space_coordinates[1] - ship.current_view[1]
        return (x, y)
        

    #ship movement,rotation and health
    def draw_ship(self, screen_coordinates, img, angle, health, ship):

        rot_img = py.transform.rotate(self.ship_imgs[img], angle)
        x, y = screen_coordinates
        ship.screen.blit(rot_img, (x - rot_img.get_width()//2, y - rot_img.get_width()//2))
        #health bar is green when health is 60% or more
        bar_width = health/2
        if health > 60:          
            color = (0, 255, 0)
        #health bar is Yellow when health is 30% or more
        elif health > 30:               
            color = (255, 255, 0)
        else:   
            #health bar is red                 
            color = (255, 0, 0)

        py.draw.rect(ship.screen, color, py.Rect(x -(bar_width/2), y+32, bar_width, 10))


    def draw_bullet(self, screen_coordinates, img, angle, bullet):

        rot_img = py.transform.rotate(self.bullet_imgs[img], angle)
        x, y = screen_coordinates
        bullet.screen.blit(rot_img, (x - rot_img.get_width()//2, y - rot_img.get_width()//2))


    def add_ships(self, messages):

        for sender in messages:
            if sender not in self.players:
                pass

    # To load & blit ship images           
    def load_ships_imgs(self):
        ship_files = os.listdir("assets/ships")    
        ship_files.remove('.DS_Store')
        ship_files.sort()
        print(ship_files)
        ship_images = [] 
        for ship_file in ship_files:
            ship = py.image.load(f'assets/ships/{ship_file}')
            ship_images.append(py.transform.scale(ship, (60, 60)))
        return ship_images
    
    # Load & Blit Bullet images 
    def load_bullet_imgs(self):
        bullet_files = os.listdir("assets/bullets")   
        bullet_files.remove('.DS_Store')
        bullet_files.sort()
        bullet_imgs = []
        for bullet_file in bullet_files:
            img = py.image.load(f'assets/bullets/{bullet_file}')
            scaler = .2
            bullet_imgs.append(py.transform.scale_by(img, scaler))
        return bullet_imgs
    
    def load_bullet_sound(self):
        bullet_sound = py.mixer.Sound('sounds/bullet_sound1.wav')
        py.mixer.Sound.set_volume(bullet_sound, 0.2)

        return bullet_sound


class Enemy_Player(py.sprite.Sprite):

    def __init__(self, player, s_img, b_img, dmg, space_coordinates):
        py.sprite.Sprite.__init__(self)

        self.player = player
        self.ship_img = s_img
        self.rect = s_img.get_rect()
        self.bullet_img = b_img
        self.dmg = dmg
        self.kills = 0
        self.health = 100
        self.angle = 0
        self.space_coordinates = space_coordinates
        self.bullets = []
        self.bullet_group = py.sprite.Group()


class Enemy_Bullet(py.sprite.Sprite):

    def __init__(self, rect, space_coordinates, angle):

        py.sprite.Sprite.__init__(self)

        self.rect = rect
        self.angle = angle
        self.space_coordinates = space_coordinates

        
