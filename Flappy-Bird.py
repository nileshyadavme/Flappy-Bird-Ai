import pygame
import neat
import time 
import os
import random


# WINDOW SIZE
WIN_WIDTH = 600
WIN_HEIGHT = 700

# LOAD BIRD IMAGE
BIRD_IMGS = [pygame.transform.scale2x( pygame.image.load(os.path.join("imgs", "bird1.png"))),
             pygame.transform.scale2x( pygame.image.load(os.path.join("imgs", "bird2.png"))),
             pygame.transform.scale2x( pygame.image.load(os.path.join("imgs", "bird3.png")))]

# LOAD PIPE,BASE,BG IMGS
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

# create the display surface object
# of specific dimension..e(X, Y).
class Bird:
    IMGS = BIRD_IMGS
    TILT_ANGLE = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]
    
    def jump(self):
        self.vel = -10
        self.tick_count = 0
        self.height = self.y
    def move(self):
        d = self.vel*self.tick_count + 1.5*self.tick_count**2
        if d>=16:
            d = 16
        if d < 0:
            d -=2
