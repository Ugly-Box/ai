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

# stores the width of the screen into a variable 
width = screen.get_width() 

# stores the height of the screen into a variable 
height = screen.get_height() 

# defining a font, y = pygame.font.SysFont('FontName',FontSize)
smallfont = pygame.font.SysFont('Raleway_Bold',38) 

# rendering a text written in this font y = smallfont.render('x (font you want)' , True , color_variable) 
audio_gain = smallfont.render('Input Gain' , True , color) 
assist_tools = smallfont.render('Assist Tools' , True , color) 
false_color = smallfont.render('False Color' , True , color) 
shutter = smallfont.render('SH' , True , color)
iso = smallfont.render('ISO' , True , color) 
iris = smallfont.render('F/' , True , color) 
nd = smallfont.render('eND' , True , color) 
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
	# if mouse is hovered on a button it changes to lighter shade 
	if width-800 <= mouse[0] <= width-600 and height-370 <= mouse[1] <= height-220: 
		pygame.draw.rect(screen,color_dark,[width-800,height-370,200,150]) 
		
	else: 
		pygame.draw.rect(screen,color_black,[width-800,height-370,200,150]) 
	# if mouse is hovered on a button it changes to lighter shade 
	if width-600 <= mouse[0] <= width-400 and height-370 <= mouse[1] <= height-220: 
		pygame.draw.rect(screen,color_dark,[width-600,height-370,200,150]) 
		
	else: 
		pygame.draw.rect(screen,color_black,[width-600,height-370,200,150]) 
# if mouse is hovered on a button it changes to lighter shade 
	if width-400 <= mouse[0] <= width-200 and height-370 <= mouse[1] <= height-220: 
		pygame.draw.rect(screen,color_dark,[width-400,height-370,200,150]) 
		
	else: 
		pygame.draw.rect(screen,color_black,[width-400,height-370,200,150]) 
# if mouse is hovered on a button it changes to lighter shade 
	if width-200 <= mouse[0] <= width and height-370 <= mouse[1] <= height-220: 
		pygame.draw.rect(screen,color_dark,[width-200,height-370,200,150]) 
		
	else: 
		pygame.draw.rect(screen,color_black,[width-200,height-370,200,150]) 

		
	# superimposing the text onto our button 
	screen.blit(audio_gain , (width-735,height-470))
	screen.blit(assist_tools , (width-520,height-470))
	screen.blit(false_color , (width-520,height-420)) 
	screen.blit(shutter , (width-720,height-350)) 
	screen.blit(iso , (width-520,height-350)) 
	screen.blit(iris , (width-320,height-350)) 
	screen.blit(nd , (width-120,height-350)) 
	
	# updates the frames of the game 
	pygame.display.update() 
