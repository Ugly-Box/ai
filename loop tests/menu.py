import pygame, sys

res = (800,480) 
screen = pygame.display.set_mode(res) 
color_black = (000,000,000)
color = (255,255,255) 
color_light = (170,170,170) 
color_dark = (100,100,100) 
color_red = (255,0,0)
width = screen.get_width() 
height = screen.get_height() 
smallfont = pygame.font.get_default_font(text, True, color) 
middlefont = pygame.font.get_default_font(text, True, self.WHITE)
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

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('here', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while True: 
            for ev in pygame.event.get(): 
                if ev.type == pygame.QUIT: 
                    pygame.quit() 
                if ev.type == pygame.MOUSEBUTTONDOWN: 
                    if width-800 <= mouse[0] <= width-550 and height-480 <= mouse[1] <= height-370: 
                        pygame.quit() 
            screen.fill((0,0,0)) 
            mouse = pygame.mouse.get_pos() 
            if width-800 <= mouse[0] <= width-800+250 and height-480 <= mouse[1] <= height-370: 
                pygame.draw.rect(screen,color_dark,[width-800,height-480,250,110]) 
        
            else: 
                pygame.draw.rect(screen,color_black,[width-800,height-480,250,110])
            if width-550 <= mouse[0] <= width-250 and height-480 <= mouse[1] <= height-370: 
                pygame.draw.rect(screen,color_dark,[width-550,height-480,300,110]) 
        
        else: 
            pygame.draw.rect(screen,color_black,[width-550,height-480,300,110]) 
        if width-800 <= mouse[0] <= width-600 and height-370 <= mouse[1] <= height-220: 
            pygame.draw.rect(screen,color_dark,[width-800,height-370,200,150]) 
        
        else: 
            pygame.draw.rect(screen,color_black,[width-800,height-370,200,150]) 
        if width-600 <= mouse[0] <= width-400 and height-370 <= mouse[1] <= height-220: 
            pygame.draw.rect(screen,color_dark,[width-600,height-370,200,150]) 
        
        else: 
            pygame.draw.rect(screen,color_black,[width-600,height-370,200,150]) 
        if width-400 <= mouse[0] <= width-200 and height-370 <= mouse[1] <= height-220: 
            pygame.draw.rect(screen,color_dark,[width-400,height-370,200,150]) 
        
        else: 
            pygame.draw.rect(screen,color_black,[width-400,height-370,200,150]) 
        if width-200 <= mouse[0] <= width and height-370 <= mouse[1] <= height-220: 
            pygame.draw.rect(screen,color_dark,[width-200,height-370,200,150]) 
        
        else: 
            pygame.draw.rect(screen,color_black,[width-200,height-370,200,150]) 
        if width-800 <= mouse[0] <= width-668 and height-220 <= mouse[1] <= height-110: 
            pygame.draw.rect(screen,color_dark,[width-800,height-220,132,110]) 
        
        else: 
            pygame.draw.rect(screen,color_black,[width-800,height-220,132,110]) 
        if width-668 <= mouse[0] <= width-536 and height-220 <= mouse[1] <= height-110: 
            pygame.draw.rect(screen,color_dark,[width-668,height-220,132,110]) 
        
        else: 
            pygame.draw.rect(screen,color_black,[width-668,height-220,132,110]) 
        if width-536 <= mouse[0] <= width-406 and height-220 <= mouse[1] <= height-110: 
            pygame.draw.rect(screen,color_dark,[width-536,height-220,132,110]) 
        
        else: 
            pygame.draw.rect(screen,color_black,[width-536,height-220,132,110]) 
        if width-406 <= mouse[0] <= width-274 and height-220 <= mouse[1] <= height-110: 
            pygame.draw.rect(screen,color_dark,[width-406,height-220,132,110]) 
        
        else: 
            pygame.draw.rect(screen,color_black,[width-406,height-220,132,110]) 
        if width-274 <= mouse[0] <= width and height-220 <= mouse[1] <= height-110: 
            pygame.draw.rect(screen,color_dark,[width-274,height-220,274,110]) 
        
        else: 
            pygame.draw.rect(screen,color_black,[width-274,height-220,274,110])
        if width-800 <= mouse[0] <= width-536 and height-110 <= mouse[1] <= height: 
            pygame.draw.rect(screen,color_dark,[width-800,height-110,264,110]) 
        
        else: 
            pygame.draw.rect(screen,color_black,[width-800,height-110,264,110])    
        if width-536 <= mouse[0] <= width-274 and height-110 <= mouse[1] <= height: 
            pygame.draw.rect(screen,color_dark,[width-536,height-110,262,110]) 
        
        else: 
            pygame.draw.rect(screen,color_black,[width-536,height-110,262,110])
        if width-274 <= mouse[0] <= width and height-110 <= mouse[1] <= height: 
            pygame.draw.rect(screen,color_dark,[width-274,height-110,274,110]) 
        
        else: 
            pygame.draw.rect(screen,color_red,[width-274,height-110,274,110])            
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
    
        pygame.display.update()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Volume", 15, self.volx, self.voly)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made by me', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()
