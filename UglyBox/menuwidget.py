import pygame 
import sys 


pygame.init() 

res = (800,80) 

screen = pygame.display.set_mode(res) 

color_black = (000,000,000)

color = (255,255,255) 

color_light = (170,170,170) 

color_dark = (100,100,100) 
color_orange = (241,73,4)
width = screen.get_width() 

height = screen.get_height() 

smallfont = pygame.font.SysFont('Raleway_Bold',26) 
rec_menu = smallfont.render('Record' , True, color)
vid_menu = smallfont.render('Video' , True, color)
audio_menu = smallfont.render('Audio' , True, color)
ev_menu = smallfont.render('E.V.' , True, color)
wb_menu = smallfont.render('W.B.' , True, color)
focus_menu = smallfont.render('Focus' , True, color)
img_menu = smallfont.render('Image' , True,color)
connect_menu = smallfont.render('Connect', True, color)
sys_menu = smallfont.render('Sys' , True, color)
help_menu = smallfont.render('Help' , True,color)


rec_icon = pygame.image.load('UglyBox/assets/video-camera.png')
vid_icon = pygame.image.load('UglyBox/assets/film.png')
audio_icon = pygame.image.load('UglyBox/assets/audio-speaker-on.png')
ev_icon = pygame.image.load('UglyBox/assets/exposure.png')
wb_icon = pygame.image.load('UglyBox/assets/sun.png')
focus_icon = pygame.image.load('UglyBox/assets/focus.png')
img_icon = pygame.image.load('UglyBox/assets/picture.png')
connect_icon = pygame.image.load('UglyBox/assets/link.png')
sys_icon = pygame.image.load('UglyBox/assets/settings.png')
help_icon = pygame.image.load('UglyBox/assets/information.png')
#testimage0.jpg is loaded into the variable image1





while True: 
	
	for ev in pygame.event.get(): 
		
		if ev.type == pygame.QUIT: 
			pygame.quit() 
			
		if ev.type == pygame.MOUSEBUTTONDOWN: 
			
			if width-800 <= mouse[0] <= width-720 and height-80 <= mouse[1] <= height-0: 
				pygame.quit() 
				
	screen.fill((100,100,100)) 
	
	mouse = pygame.mouse.get_pos() 

	if width-800 <= mouse[0] <= width-800+80 and height-80 <= mouse[1] <= height-0:		    pygame.draw.rect(screen,color_orange,[width-800,height-80,80,80]) 
		

	if width-720 <= mouse[0] <= width-720+80 and height-80 <= mouse[1] <= height-0:		    pygame.draw.rect(screen,color_orange,[width-720,height-80,80,80]) 
	if width-640 <= mouse[0] <= width-640+80 and height-80 <= mouse[1] <= height-0:		    pygame.draw.rect(screen,color_orange,[width-640,height-80,80,80]) 
	if width-560 <= mouse[0] <= width-560+80 and height-80 <= mouse[1] <= height-0:		    pygame.draw.rect(screen,color_orange,[width-560,height-80,80,80]) 
	if width-480 <= mouse[0] <= width-480+80 and height-80 <= mouse[1] <= height-0:		    pygame.draw.rect(screen,color_orange,[width-480,height-80,80,80]) 
	if width-400 <= mouse[0] <= width-400+80 and height-80 <= mouse[1] <= height-0:		    pygame.draw.rect(screen,color_orange,[width-400,height-80,80,80]) 
	if width-320 <= mouse[0] <= width-320+80 and height-80 <= mouse[1] <= height-0:		    pygame.draw.rect(screen,color_orange,[width-320,height-80,80,80]) 
	if width-240 <= mouse[0] <= width-240+80 and height-80 <= mouse[1] <= height-0:		    pygame.draw.rect(screen,color_orange,[width-240,height-80,80,80]) 
	if width-160 <= mouse[0] <= width-160+80 and height-80 <= mouse[1] <= height-0:		    pygame.draw.rect(screen,color_orange,[width-160,height-80,80,80]) 
	if width-80 <= mouse[0] <= width-80+80 and height-80 <= mouse[1] <= height-0:		    pygame.draw.rect(screen,color_orange,[width-80,height-80,80,80]) 
		

	screen.blit(rec_icon, [10, 2])
	screen.blit(vid_icon, [90, 2])
	screen.blit(audio_icon, [170, 2])
	screen.blit(ev_icon, [245, 2])
	screen.blit(wb_icon, [330, 2])
	screen.blit(focus_icon, [410, 2])
	screen.blit(img_icon, [490, 2])
	screen.blit(connect_icon, [570, 2])
	screen.blit(sys_icon, [650, 2])
	screen.blit(help_icon, [730, 2])
	screen.blit(rec_menu , (width-795,height-18))
	screen.blit(vid_menu , (width-710,height-18))
	screen.blit(audio_menu , (width-630,height-18))
	screen.blit(ev_menu , (width-535,height-18))
	screen.blit(wb_menu , (width-460,height-18))
	screen.blit(focus_menu , (width-390,height-18))
	screen.blit(img_menu , (width-310,height-18))
	screen.blit(connect_menu , (width-235,height-18))
	screen.blit(sys_menu , (width-140,height-18))
	screen.blit(help_menu , (width-60,height-18))

	



	
	pygame.display.update() 


#80 x 800 - 80 x 80 squares
#grey canvas 
#white icons 

#Record 
#Video
#audio
#ev 
#wb 
#focus
#image 
#connect 
#system 
#help 
