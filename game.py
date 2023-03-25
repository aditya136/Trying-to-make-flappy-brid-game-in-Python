from ursina import *
import random as r

app = Ursina()
Sky()

bird = Animation('assets\img',
                 collider='box',
                 scale=(2, 2, 2),
                 y=10)


camera.orthographic = True
camera.fov = 20

#def update():
    #bird.y = bird.y -4*time.dt 
    #for p in pipes:
        #p.x =p.x - 2*time.dt 
    #touch = bird.intersects()
    #if touch.hit or bird.y < -10:
        #quit()