import pygame 
import sys 


# initializing the constructor 
pygame.init() 

# screen resolution 
res = (800,480) 

# opens up a window y = pygame.display.set_mode(x)
screen = pygame.display.set_mode(res) 

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
smallfont = pygame.font.SysFont('Raleway',25) 

# rendering a text written in this font y = smallfont.render('x (font you want)' , True , color_variable) 
text = smallfont.render('exit' , True , color) 

while True: 
	
	for ev in pygame.event.get(): 
		
		if ev.type == pygame.QUIT: 
			pygame.quit() 
			
		#checks if a mouse is clicked 
		if ev.type == pygame.MOUSEBUTTONDOWN: 
			
			#if the mouse is clicked on the 
			# button the game is terminated 
			if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
				pygame.quit() 
				
	# background screen fill color, screen.fill((r,g,b))
	screen.fill((0,0,0)) 
	
	# stores the (x,y) coordinates into the variable as a tuple 
	mouse = pygame.mouse.get_pos() 
	
	# if mouse is hovered on a button it changes to lighter shade 
	if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
		pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
		
	else: 
		pygame.draw.rect(screen,color_dark,[width/5,height/4,140,50]) 
	
	# superimposing the text onto our button 
	screen.blit(text , (width/2+50,height/2)) 
	
	# updates the frames of the game 
	pygame.display.update() 
