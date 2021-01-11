#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((800, 480))

smallfont = pygame.font.SysFont('Raleway_Bold',38) 
middlefont = pygame.font.SysFont('Raleway_Medium',50)
color_black = (000,000,000)
color = (255,255,255) 
color_light = (170,170,170) 
color_dark = (100,100,100) 
color_red = (255,0,0)
width = screen.get_width() 
height = screen.get_height() 
audio_gain = middlefont.render('Input Gain' , True , color) 
assist_tools = smallfont.render('Assist Tools' , True , color) 
false_color = smallfont.render('False Color' , True , color) 
shutter = middlefont.render('SH' , True , color)
iso = middlefont.render('ISO' , True , color) 
iris = middlefont.render('F/' , True , color) 
nd = middlefont.render('eND' , True , color) 
fps = smallfont.render('FPS' , True , color) 
vfr = smallfont.render('VFR' , True , color) 
codec = smallfont.render('Codec' , True , color) 
lut = smallfont.render('Image' , True , color) 
res = smallfont.render('Resolution' , True , color) 
remaining = smallfont.render('Card Space' , True , color) 
wb = smallfont.render('White Balance' , True , color) 
battery = smallfont.render('Bat' , True , color) 

def draw_text(text, smallfont, color, surface, x, y):
    textobj = smallfont.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def main_menu():
    while True:

        screen.fill((0,0,0))
        screen.blit(audio_gain , (width-795,height-475))
        screen.blit(assist_tools , (width-520,height-470))
        screen.blit(false_color , (width-520,height-420)) 
        screen.blit(shutter , (width-740,height-350)) 
        screen.blit(iso , (width-550,height-350)) 
        screen.blit(iris , (width-320,height-350)) 
        screen.blit(nd , (width-160,height-350)) 
        screen.blit(fps , (width-760,height-200)) 
        screen.blit(vfr , (width-630,height-200)) 
        screen.blit(codec , (width-510,height-200)) 
        screen.blit(lut , (width-375,height-200)) 
        screen.blit(res , (width-200,height-200)) 
        screen.blit(remaining , (width-735,height-100)) 
        screen.blit(wb , (width-500,height-100)) 
        screen.blit(battery , (width-230,height-100)) 


        mx, my = pygame.mouse.get_pos()
# pygame.Rect(topleft, bottomleft, topright, bottomright)
        button_1 = pygame.Rect(0, 110, 250, 110)
        if button_1.collidepoint((mx, my+110)):
            if click:
                quick_audio()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def quick_audio():
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('Audio Settings', smallfont, (255, 255, 255), screen, width-500, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def options():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('options', smallfont, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

main_menu()