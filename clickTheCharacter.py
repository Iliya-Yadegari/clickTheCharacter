HEIGHT = 600
WIDTH = 600

robot_obj = Actor('robot_win',(234,545))
cat1_obj = Actor('cat1',(245,345))
cat2_obj = Actor('cat2',(234,195))

def draw():
    screen.fill((0,7,186))
    robot_obj.draw()
    cat1_obj.draw()
    cat2_obj.draw()

def update():
    robot_obj.left += 2
    cat1_obj.left += 2
    cat2_obj.left += 2
    if robot_obj.left > WIDTH:
       robot_obj.right = 0
    if cat1_obj.left > WIDTH:
       cat1_obj.right = 0
    if cat2_obj.left > WIDTH:
       cat2_obj.right = 0

def on_mouse_down(pos,button):
    if robot_obj.collidepoint(pos) and button == mouse.LEFT:
        print('WIN')
        robot_obj.image = 'alien_hurt'
        sounds.eep.play()

    elif cat1_obj.collidepoint(pos) and button == mouse.LEFT:
        print('WIN')
        cat1_obj.image = 'cat3'
        sounds.meow3.play()

    elif cat2_obj.collidepoint(pos) and button == mouse.LEFT:
        print('WIN')
        cat2_obj.image = 'cat4'
        sounds.meow4.play()

    else:
        print('GAME OVER')
