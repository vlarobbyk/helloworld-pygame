# -*- coding: utf-8 -*-
# Grupo de Investigación en Inteligencia Artificial y Tecnologías de Asistencia (GI-IATa)
# Cátedra UNESCO Tecnologías de apoyo para la Inclusión Educativa
# author: vlarobbyk

import pygame
import sys
import os
import numpy as np

from Utilities import Utilities

class SplashScreen:
    
    def __init__(self):
        self.intro = True
        self.ut = Utilities()

    def start(self):
        width = 800
        height = 600
        infoObject = pygame.display.Info()
        swidth, sheight = infoObject.current_w,infoObject.current_h
        
        posx = (swidth/2)-(width/2)
        posy = (sheight/2)-(height/2)
        
        os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (posx,posy)
        
        _font = pygame.font.SysFont('Times New Roman',27)
        #_font = pygame.freetype.SysFont('Arial', 20)
        
        giiata_logo = pygame.image.load('./images/Logo-GIIATa.png')
        giiata_logo = pygame.transform.scale(giiata_logo, (180,160))

        ups_logo = pygame.image.load('./images/logo-ups.jpg')
        ups_logo = pygame.transform.scale(ups_logo, (180,160))
        
        robot = pygame.image.load('./images/Blue-Robot.png')
        robot = pygame.transform.scale(robot, (128, 128))
        
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Algoritmos de búsqueda - IA1')
        
        x = 0
        y = int((height/2)+(height/4))
        points = np.arange(3,70,0.97)
        fx_points = np.sqrt(points)
        clock = pygame.time.Clock()
        rectc = pygame.Rect(0,height/2,width,height)
        logic_function = lambda a: 1 if a else -1
        flag = True
        i = 0
        
        while self.intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.intro = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        self.intro = False
                    if event.key == pygame.K_q:
                        self.intro = False
                        pygame.quit()
                        sys.exit()

            
            screen.fill((255,255,255))
            self.ut.drawText(screen, 'Grupo de Investigación en Inteligencia Artificial y Tecnologías de Asistencia', (10,10,200), ((width/2)-100, 10, 500, 50), _font)

            self.ut.drawText(screen, 'Inteligencia Artificial 1 - Algoritmos de búsqueda', (100,10,200), ((width/2)-100, 73, 500, 100), _font)
            
            screen.blit(giiata_logo,(10,10))
            screen.blit(ups_logo, (10,170))
            
            #for i in range(len(points)):
                #screen.fill((255,255,255))
            screen.fill(((243, 111, 107)),rectc)
            x = int(points[i])*10
            fxt = int(fx_points[i]*20.0)
            #screen.set_at((x, int(y - int(fx_points[i]))), (203,0,0))
            pygame.draw.circle(screen, (10,10,223),  (x, y - fxt), 3)
            #print((x, y - fxt))
            screen.blit(robot, (x,y - fxt))
            
            i+=logic_function(flag)
            #print('i: %d len(points): %d' % (i,len(points)))
            
            if i>=len(points):
                flag = False
                i-=1
            elif i<=0:
                flag = True
                
            #print('Flag: ',flag)
                
            pygame.display.update()
            clock.tick(20)
            #screen.blit(robot, (x,y))
            #pygame.display.flip()
            #x+=1
            #y+=1
        
        print('Entra al juego')
    
if __name__=="__main__":
    pygame.init()
    pygame.font.init()
    sscren = SplashScreen()
    sscren.start()
