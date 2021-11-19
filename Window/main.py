import pygame as pg
import numpy as np 
from funcs import *
import tensorflow as tf


class App:
    
    def __init__(self):
        self.res = self.width, self.height = (800, 600)
        self.screen = pg.display.set_mode(self.res, pg.SCALED)
        self.clock = pg.time.Clock()
        
    def update(self):
        pass
    
    def draw(self):
        pg.display.flip()
    
    def run(self):
        while True:
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick(60)
            pg.display.set_caption(f'FPS: {self.clock.get_fps()}')
        
        
if __name__ == '__main__':
    app = App()
    app.run()