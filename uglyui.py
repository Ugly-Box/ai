import pygame 
import sys 


# initializing the constructor 
pygame.init() 

# screen resolution 
res = (800,480) 

# opens up a window y = pygame.display.set_mode(x)
screen = pygame.display.set_mode(res) 

# Colors
color_black = (000,000,000)

# white color 
color = (255,255,255) 

# color of the button when clicked
color_light = (170,170,170) 

# color of the button when not clicked
color_dark = (100,100,100) 
color_red = (255,0,0)
# stores the width of the screen into a variable 
width = screen.get_width() 

# stores the height of the screen into a variable 
height = screen.get_height() 

# defining a font, y = pygame.font.SysFont('FontName',FontSize)
smallfont = pygame.font.SysFont('Raleway_Bold',38) 
middlefont = pygame.font.SysFont('Raleway_Medium',50)
# rendering a text written in this font y = smallfont.render('x (font you want)' , True , color_variable) 
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

while True: 
	
	for ev in pygame.event.get(): 
		
		if ev.type == pygame.QUIT: 
			pygame.quit() 
			
		#checks if a mouse is clicked 
		if ev.type == pygame.MOUSEBUTTONDOWN: 
			
			#if the mouse is clicked on the button the game is terminated 
			if width-800 <= mouse[0] <= width-550 and height-480 <= mouse[1] <= height-370: 
				pygame.quit() 
				
	# background screen fill color, screen.fill((r,g,b))
	screen.fill((0,0,0)) 
	
	# stores the (x,y) coordinates into the variable as a tuple 
	mouse = pygame.mouse.get_pos() 
	
	# if mouse is hovered on a button it changes to lighter shade 
	if width-800 <= mouse[0] <= width-800+250 and height-480 <= mouse[1] <= height-370: 
		pygame.draw.rect(screen,color_dark,[width-800,height-480,250,110]) 
		
	else: 
		pygame.draw.rect(screen,color_black,[width-800,height-480,250,110])
	# if mouse is hovered on a button it changes to lighter shade 
	if width-550 <= mouse[0] <= width-250 and height-480 <= mouse[1] <= height-370: 
		pygame.draw.rect(screen,color_dark,[width-550,height-480,300,110]) 
		
	else: 
		pygame.draw.rect(screen,color_black,[width-550,height-480,300,110]) 
	# 2nd row - Shutter
	if width-800 <= mouse[0] <= width-600 and height-370 <= mouse[1] <= height-220: 
		pygame.draw.rect(screen,color_dark,[width-800,height-370,200,150]) 
		
	else: 
		pygame.draw.rect(screen,color_black,[width-800,height-370,200,150]) 
# 2nd row - ISO 
	if width-600 <= mouse[0] <= width-400 and height-370 <= mouse[1] <= height-220: 
		pygame.draw.rect(screen,color_dark,[width-600,height-370,200,150]) 
		
	else: 
		pygame.draw.rect(screen,color_black,[width-600,height-370,200,150]) 
# 2nd row - f/ 
	if width-400 <= mouse[0] <= width-200 and height-370 <= mouse[1] <= height-220: 
		pygame.draw.rect(screen,color_dark,[width-400,height-370,200,150]) 
		
	else: 
		pygame.draw.rect(screen,color_black,[width-400,height-370,200,150]) 
# 2nd row - eND
	if width-200 <= mouse[0] <= width and height-370 <= mouse[1] <= height-220: 
		pygame.draw.rect(screen,color_dark,[width-200,height-370,200,150]) 
		
	else: 
		pygame.draw.rect(screen,color_black,[width-200,height-370,200,150]) 
# 3rd row - FPR
	if width-800 <= mouse[0] <= width-668 and height-220 <= mouse[1] <= height-110: 
		pygame.draw.rect(screen,color_dark,[width-800,height-220,132,110]) 
		
	else: 
		pygame.draw.rect(screen,color_black,[width-800,height-220,132,110]) 
# 3rd row - VFR
	if width-668 <= mouse[0] <= width-536 and height-220 <= mouse[1] <= height-110: 
		pygame.draw.rect(screen,color_dark,[width-668,height-220,132,110]) 
		
	else: 
		pygame.draw.rect(screen,color_black,[width-668,height-220,132,110]) 
# 3rd row - Codec
	if width-536 <= mouse[0] <= width-406 and height-220 <= mouse[1] <= height-110: 
		pygame.draw.rect(screen,color_dark,[width-536,height-220,132,110]) 
		
	else: 
		pygame.draw.rect(screen,color_black,[width-536,height-220,132,110]) 
# 3rd row - Image
	if width-406 <= mouse[0] <= width-274 and height-220 <= mouse[1] <= height-110: 
		pygame.draw.rect(screen,color_dark,[width-406,height-220,132,110]) 
		
	else: 
		pygame.draw.rect(screen,color_black,[width-406,height-220,132,110]) 
# 3rd row - Resolution
	if width-274 <= mouse[0] <= width and height-220 <= mouse[1] <= height-110: 
		pygame.draw.rect(screen,color_dark,[width-274,height-220,274,110]) 
		
	else: 
		pygame.draw.rect(screen,color_black,[width-274,height-220,274,110])
# 4th row - Card Space
	if width-800 <= mouse[0] <= width-536 and height-110 <= mouse[1] <= height: 
		pygame.draw.rect(screen,color_dark,[width-800,height-110,264,110]) 
		
	else: 
		pygame.draw.rect(screen,color_black,[width-800,height-110,264,110])	
# 4th row - white Balance
	if width-536 <= mouse[0] <= width-274 and height-110 <= mouse[1] <= height: 
		pygame.draw.rect(screen,color_dark,[width-536,height-110,262,110]) 
		
	else: 
		pygame.draw.rect(screen,color_black,[width-536,height-110,262,110])
# 4th row - white Balance
	if width-274 <= mouse[0] <= width and height-110 <= mouse[1] <= height: 
		pygame.draw.rect(screen,color_dark,[width-274,height-110,274,110]) 
		
	else: 
		pygame.draw.rect(screen,color_red,[width-274,height-110,274,110])			
	# superimposing the text onto our button 
	screen.blit(audio_gain , (width-795,height-475))
	screen.blit(assist_tools , (width-520,height-470))
	screen.blit(false_color , (width-520,height-420)) 
	screen.blit(shutter , (width-720,height-350)) 
	screen.blit(iso , (width-520,height-350)) 
	screen.blit(iris , (width-320,height-350)) 
	screen.blit(nd , (width-120,height-350)) 
	screen.blit(fps , (width-760,height-200)) 
	screen.blit(vfr , (width-630,height-200)) 
	screen.blit(codec , (width-510,height-200)) 
	screen.blit(lut , (width-375,height-200)) 
	screen.blit(res , (width-200,height-200)) 
	screen.blit(remaining , (width-735,height-100)) 
	screen.blit(wb , (width-500,height-100)) 
	screen.blit(battery , (width-230,height-100)) 
	
	# updates the frames of the game 
	pygame.display.update() 
