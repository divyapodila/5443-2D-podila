import copy

def move_screen(scroll_x, scroll_y, ship, WIDTH, HEIGHT, tiles_x, tiles_y):

    new_scrollx = scroll_x-ship.vector[0]
    new_scrolly = scroll_y-ship.vector[1]

    # X-coordinates of screen set scrollers
    if -new_scrollx >= 0 and -new_scrollx <= WIDTH*(tiles_x-1):
       
        if ship.space_coordinates[0] >= WIDTH/2 and ship.space_coordinates[0] <= WIDTH*tiles_x - (WIDTH/2):
            scroll_x -= ship.vector[0]
    
    # Y-coordinates of screen set scrollers
    if -new_scrolly >= 0 and -new_scrolly <= HEIGHT*(tiles_y-1):
        if ship.space_coordinates[1] >= HEIGHT/2 and ship.space_coordinates[1] <= HEIGHT*tiles_y - (HEIGHT/2):
            scroll_y -= ship.vector[1]
    return scroll_x, scroll_y

#set scrollers function for screen movement
def set_scrollers(ship, screen_dim, tiles):
    coords = copy.deepcopy(ship.space_coordinates)

    for i in range(2):
        if coords[i]+screen_dim[i]/2 <= screen_dim[i] * tiles[i] and coords[i]-screen_dim[i]/2 >= 0:
            coords[i] -= screen_dim[i]/2
        else:
            # ship is on the left end of the screen
            if coords[i] < (screen_dim[i]*tiles[i])/2:
                coords[i] = 0
            # Ship is on the right end of the screen
            else:
                coords[i] = (screen_dim[i] * (tiles[i]-1))
    return -coords[0], -coords[1]
        