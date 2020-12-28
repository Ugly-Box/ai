#!/usr/bin/env python

import sys, os, time, subprocess, commands, pygame
from pygame.locals import *
from subprocess import *
from zui import zUI

os.environ["SDL_FBDEV"] = "/dev/fb0"
os.environ["SDL_MOUSEDEV"] = "/dev/input/mouse0"
os.environ["SDL_MOUSEDRV"] = "TSLIB"

# Initialize pygame modules individually
pygame.font.init()
pygame.display.init()
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

#set size of the screen
cmd = ''
size = width, height = 720, 720
screen = pygame.display.set_mode(size, FULLSCREEN)
zui = zUI(pygame, screen, size);

# define function that checks for touch location
def on_touch():
	cmd = ''
	
	# get the position that was touched
	touchpos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
	print (touchpos)
	return zui.GetCommandFromClick(touchpos)	

def ShowScreen(cmd):

	print (cmd)
	if cmd == 'close':
		cmd = ''
		zui.KeyBufferClear()
		zui.SavedCmdClear()
		
	parts = cmd.split('.')
	if parts[0] == 'key':
		if parts[1] == 'del':
			zui.KeyBufferDel()
		else:
			if len(zui.KeyBuffer()) < int(parts[2]):
				zui.KeyBufferAdd(parts[1])
		cmd = zui.SavedCmd()
			

		
	if cmd == '':	
		target = ''
		zui.LoadCameraState()
		zui.ClearScreen()
		zui.DrawGrid(4, 4)
		zui.GraphicButton(1, 0, 'camera.small', 2, 3, 'go.video')
		zui.TextButton(1.5, 0.7, zui.Resolution(), 0, 0, '', 80)
		zui.TextButton(1.8, 0.7, zui.FPS(), 0, 0, '', 80)
		zui.TextButton(2.72, 0, zui.Codec(), 0, 0, '', 60)
		zui.TextButton(1, 0, zui.LUT(), 0, 0, '', 60)
		zui.DoubleTextButton(0, 1, zui.ISO(), 'ISO', 1, 1, ('go.iso2' if (zui.IntIso() > 8000) else 'go.iso1'))
		
		if zui.WB() == 'D10000':
			zui.DoubleTextButton(0, 0, 'D10000', 'WB', 1, 1, 'go.wb', 70)
		elif zui.WB() == 'Manual':
			zui.DoubleTextButton(0, 0, zui.mWB(), 'WB', 1, 1, 'go.wb')
		elif zui.WB() == 'Auto':
			zui.DoubleTextButton(0, 0, 'Auto', 'WB', 1, 1, 'go.wb')
		else:
			zui.HybridButton(0, 0, 'wb.small.' + zui.WB(), 'WB', 1, 1, 'go.wb')
		
		zui.DoubleTextButton(0, 2, zui.Angle(), 'Angle',1, 1, 'go.angle')
		zui.GraphicButton(0, 3, 'record', 1, 1, 'rec')
		
		zui.HybridButton(1, 3, 'scene.small', 'Quick', 1, 1, 'go.scene')
		zui.HybridButton(2, 3, 'audio.small', 'Audio', 1, 1, 'go.audio')
		zui.HybridButton(3, 3, 'system.small', 'More', 1, 1, 'go.more')

		zui.CenteredTextButton(3, 0, "00:00:00", 1, 3, '', 150)

	elif cmd == 'rec':
		if zui.Recording() == False:
			zui.RecordingOn(0, 3, 'stop')
			print ('On')
		else:
			zui.RecordingOff(0, 3, 'record')
		
	elif cmd == 'go.wb':	
		zui.ClearScreen()
		zui.DrawGrid(3, 3)
		zui.GraphicButton(0, 2, 'close', 1, 1, 'close')
		zui.CenteredTextButton(0, 0, 'AUTO', 1, 1, 'set.wb.Auto', 90)
		zui.CenteredTextButton(0, 1, 'MANUAL', 1, 1, 'go.wbmanual', 70)
		zui.GraphicButton(1, 0, 'wb.Daylight', 1, 1, 'set.wb.Daylight')
		zui.GraphicButton(1, 1, 'wb.Cloudy', 1, 1, 'set.wb.Cloudy')
		zui.GraphicButton(1, 2, 'wb.Shade', 1, 1, 'set.wb.Shade')
		zui.GraphicButton(2, 0, 'wb.Incandescent', 1, 1, 'set.wb.')
		zui.GraphicButton(2, 1, 'wb.Fluorescent', 1, 1, 'set.wb.Fluorescent')
		zui.CenteredTextButton(2, 2, 'D10000', 1, 1, 'set.wb.D10000', 70)

	elif cmd == 'go.wbmanual':	
		zui.SavedCmdSet(cmd)
		zui.ClearScreen()
		zui.DrawGrid(4, 4)
		zui.GraphicButton(0, 3, 'close', 1, 1, 'close')
		zui.CenteredTextButton(0, 0, zui.KeyBuffer() + '00', 1, 3, '', 90)
		zui.CenteredTextButton(1, 0, '1', 1, 1, 'key.1.3', 90)
		zui.CenteredTextButton(1, 1, '2', 1, 1, 'key.2.3', 90)
		zui.CenteredTextButton(1, 2, '3', 1, 1, 'key.3.3', 90)
		zui.GraphicButton(1, 3, 'del', 1, 1, 'key.del')
		zui.CenteredTextButton(2, 0, '4', 1, 1, 'key.4.3', 90)
		zui.CenteredTextButton(2, 1, '5', 1, 1, 'key.5.3', 90)
		zui.CenteredTextButton(2, 2, '6', 1, 1, 'key.6.3', 90)
		zui.CenteredTextButton(2, 3, '0', 1, 1, 'key.0.3', 90)
		zui.CenteredTextButton(3, 0, '7', 1, 1, 'key.7.3', 90)
		zui.CenteredTextButton(3, 1, '8', 1, 1, 'key.8.3', 90)
		zui.CenteredTextButton(3, 2, '9', 1, 1, 'key.9.3', 90)
		zui.GraphicButton(3, 3, 'ok', 1, 1, 'set.mwb')

	elif cmd == 'go.iso1':	
		zui.ClearScreen()
		zui.DrawGrid(4, 4)
		zui.GraphicButton(0, 3, 'close', 1, 1, 'close')
		zui.CenteredTextButton(0, 0, 'AUTO', 1, 1, 'set.iso.Auto', 90)
		zui.CenteredTextButton(0, 1, '*500', 1, 1, 'set.iso.500', 90)
		zui.CenteredTextButton(0, 2, '640', 1, 1, 'set.iso.640', 90)
		zui.CenteredTextButton(1, 0, '800', 1, 1, 'set.iso.800', 90)
		zui.CenteredTextButton(1, 1, '1000', 1, 1, 'set.iso.1000', 90)
		zui.CenteredTextButton(1, 2, '1250', 1, 1, 'set.iso.1250', 90)
		zui.CenteredTextButton(1, 3, '1600', 1, 1, 'set.iso.1600', 90)
		zui.CenteredTextButton(2, 0, '2000', 1, 1, 'set.iso.2000', 90)
		zui.CenteredTextButton(2, 1, '*2500', 1, 1, 'set.iso.2500', 90)
		zui.CenteredTextButton(2, 2, '3200', 1, 1, 'set.iso.3200', 90)
		zui.CenteredTextButton(2, 3, '5000', 1, 1, 'set.iso.2500', 90)
		zui.CenteredTextButton(3, 0, '4000', 1, 1, 'set.iso.4000', 90)
		zui.CenteredTextButton(3, 1, '6400', 1, 1, 'set.iso.6400', 90)
		zui.CenteredTextButton(3, 2, '8000', 1, 1, 'set.iso.8000', 90)
		zui.CenteredTextButton(3, 3, '>', 1, 1, 'go.iso2', 90)

	elif cmd == 'go.iso2':	
		zui.ClearScreen()
		zui.DrawGrid(4, 4)
		zui.GraphicButton(0, 3, 'close', 1, 1, 'close')		
		zui.CenteredTextButton(0, 0, '10000', 1, 1, 'set.iso.10000', 90)
		zui.CenteredTextButton(0, 1, '12800', 1, 1, 'set.iso.12800', 90)
		zui.CenteredTextButton(0, 2, '16000', 1, 1, 'set.iso.16000', 90)
		zui.CenteredTextButton(1, 0, '20000', 1, 1, 'set.iso.20000', 90)
		zui.CenteredTextButton(1, 1, '25600', 1, 1, 'set.iso.25600', 90)
		zui.CenteredTextButton(1, 2, '32000', 1, 1, 'set.iso.32000', 90)
		zui.CenteredTextButton(1, 3, '40000', 1, 1, 'set.iso.40000', 90)
		zui.CenteredTextButton(2, 0, '51200', 1, 1, 'set.iso.51200', 90)
		zui.CenteredTextButton(3, 3, '<', 1, 1, 'go.iso1', 90)

	elif cmd == 'go.angle':	
		zui.ClearScreen()
		zui.DrawGrid(3, 3)
		zui.GraphicButton(0, 2, 'close', 1, 1, 'close')
		zui.CenteredTextButton(0, 0, 'AUTO', 1, 1, 'set.angle.Auto', 90)
		zui.CenteredTextButton(0, 1, '45', 1, 1, 'set.angle.45', 90)
		zui.CenteredTextButton(1, 0, '90', 1, 1, 'set.angle.90', 90)
		zui.CenteredTextButton(1, 1, '180', 1, 1, 'set.angle.180', 90)
		zui.CenteredTextButton(1, 2, '360', 1, 1, 'set.angle.360', 90)

	elif cmd == 'go.scene':	
		zui.ClearScreen()
		zui.DrawGrid(3, 3)
		zui.GraphicButton(0, 2, 'close', 1, 1, 'close')
		zui.GraphicButton(0, 0, 'scene.chase.hd', 1, 1, 'set.scene.chasehd')
		zui.GraphicButton(0, 1, 'scene.chase.4k', 1, 1, 'set.scene.chase4k')
		zui.GraphicButton(1, 0, 'scene.landscape', 1, 1, 'set.scene.landscape')
		zui.GraphicButton(1, 1, 'scene.landscape.night', 1, 1, 'set.scene.landscapenight')

	elif cmd == 'go.audio':	
		zui.ClearScreen()
		zui.DrawGrid(3, 3)
		zui.GraphicButton(0, 2, 'close', 1, 1, 'close')

	elif cmd == 'go.more':	
		zui.ClearScreen()
		zui.DrawGrid(4, 4)
		zui.GraphicButton(0, 3, 'close', 1, 1, 'close')

	elif cmd == 'go.video':	
		zui.ClearScreen()
		zui.DrawGrid(2, 3)
		zui.GraphicButton(1, 2, 'close', 1, 1, 'close')
		zui.CenteredTextButton(0, 0, zui.Resolution() , 1, 1, 'go.resolution', 90)
		zui.CenteredTextButton(0, 1, zui.FPS(1) , 1, 1, 'go.fps', 90)
		zui.CenteredTextButton(0, 2, zui.FPS(2) , 1, 1, 'go.fps', 90)
		zui.CenteredTextButton(1, 0, zui.LUT() , 1, 1, 'go.lut', 60)
		zui.CenteredTextButton(1, 1, zui.Codec() , 1, 1, 'go.codec', 60)

	elif cmd == 'go.resolution':	
		zui.ClearScreen()
		zui.DrawGrid(3, 4)
		zui.GraphicButton(0, 3, 'close', 1, 1, 'go.video')
		zui.CenteredTextButton(0, 0, 'C4k' , 1, 1, 'set.resolution.xx', 90)
		zui.CenteredTextButton(0, 1, 'LN' , 1, 1, 'set.resolution.xx', 60)
		zui.CenteredTextButton(0, 2, '2.4:1' , 1, 1, 'set.resolution.xx', 60)
		zui.CenteredTextButton(1, 0, '4k' , 1, 1, 'set.resolution.xx', 90)
		zui.CenteredTextButton(1, 1, 'LN' , 1, 1, 'set.resolution.xx', 60)
		zui.CenteredTextButton(1, 2, '2.4:1' , 1, 1, 'set.resolution.xx', 60)
		zui.CenteredTextButton(2, 0, 'HD' , 1, 1, 'set.resolution.xx', 90)

	else:
		# Handle Commands 
		parts = cmd.split('.')
		
		if (parts[0] == 'set'):
		
			if (parts[1] == 'iso'):
				zui.SetISO(parts[2])

			if (parts[1] == 'angle'):
				zui.SetAngle(parts[2])

			if (parts[1] == 'wb'):
				zui.SetWB(parts[2])

			if (parts[1] == 'mwb'):
				zui.SetmWB(zui.KeyBuffer() + '00')
				zui.KeyBufferClear()


			ShowScreen('')
#While loop to manage touch screen inputs

ShowScreen('')

while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
            cmd = on_touch()
            if cmd <> '':
            	ShowScreen(cmd)

        #ensure there is always a safe way to end the program if the touch screen fails
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
  	if zui.Recording():
			zui.CenteredTextButton(3, 0, zui.RunningTime(), 1, 3, '', 150)
  			
    
    pygame.display.update()
    ## Reduce CPU utilisation
    #time.sleep(0.1)
