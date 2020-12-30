# -*- coding: utf-8 -*-

import sys, os, time, datetime, subprocess, commands, pygame, requests, json

class zUI:

	# Constructor
	def __init__(self, pygame, screen, size):
		# Save values
		self.pygame = pygame
		self.screen = screen
		self.rows = 0
		self.cols = 0
		self.size = size
		
		self.text = (255,255,255)
		self.accent = (254,75,4)
		self.grid = (100, 100, 100)
		self.background = (0,0,0)
		self.cellwidth = 0
		self.cellheight = 0
		
		self.clickareas = []
		self.recording = False
		self.starttime = 0
		
		self.recimage = ()
	
		self.iso = 'Auto'
		self.angle = '180'
		self.movres = ''
		self.movfps = ''
		self.movvfr = ''
		self.codec = ''
		self.lut = ''
		self.wb = ''
		self.mwb = ''
		self.stepwb = ''
		
		self.keybuffer = ''
		self.savedcmd = ''
		
	def ISO(self):
		return self.iso

	def LUT(self):
		return self.lut

	def WB(self):
		return self.wb

	def mWB(self):
		return self.mwb

	def Resolution(self):		
		return self.movres
		
	def Codec(self):		
		return self.codec
		
	def FPS(self, part = 0):
		if part == 0:		
			return self.movfps + ' - ' + self.movvfr
		elif part == 1:
			return self.movfps
		else:
			return self.movvfr

	def Angle(self):
		return self.angle;
		
	def IntIso(self):
		if self.iso == 'Auto':
			return 0
		else:
			return int(self.iso)
		
	def LoadCameraState(self):
		request = requests.get("http://192.168.11.160/ctrl/get?k=iso")
		request.encoding = "UTF-8"
		state = json.loads(request.content)
		self.iso = state['value']

		request = requests.get("http://192.168.11.160/ctrl/get?k=shutter_angle")
		request.encoding = "UTF-8"
		state = json.loads(request.content)
		self.angle = state['value'].replace(u'\xb0', '')

		request = requests.get("http://192.168.11.160/ctrl/get?k=movfmt")
		request.encoding = "UTF-8"
		state = json.loads(request.content)
		parts = state['value'].split('P')
		self.movres = parts[0]
		self.movfps = parts[1]
		request = requests.get("http://192.168.11.160/ctrl/get?k=movvfr")
		request.encoding = "UTF-8"
		state = json.loads(request.content)
		self.movvfr = state['value']
		request = requests.get("http://192.168.11.160/ctrl/get?k=video_encoder")
		request.encoding = "UTF-8"
		state = json.loads(request.content)
		self.codec = state['value']
		request = requests.get("http://192.168.11.160/ctrl/get?k=lut")
		request.encoding = "UTF-8"
		state = json.loads(request.content)
		self.lut = state['value']
		request = requests.get("http://192.168.11.160/ctrl/get?k=wb")
		request.encoding = "UTF-8"
		state = json.loads(request.content)
		self.wb = state['value']
		if self.wb == 'Manual':
			request = requests.get("http://192.168.11.160/ctrl/get?k=mwb")
			request.encoding = "UTF-8"
			state = json.loads(request.content)
			self.mwb = state['value']
		else:
			self.mwb = ''
			
	def KeyBuffer(self):
		return self.keybuffer	

	def KeyBufferClear(self):
		self.keybuffer = ''	
	
	def KeyBufferAdd(self, text):
		self.keybuffer = self.keybuffer + text
	
	def KeyBufferDel(self):
		self.keybuffer = self.keybuffer[:-1]
	
	def SavedCmdClear(self):
		self.savedcmd = ''	
	
	def SavedCmd(self):
		return self.savedcmd

	def SavedCmdSet(self, cmd):
		self.savedcmd = cmd
	
	
	def SetISO(self, iso):
		request = requests.get("http://192.168.11.160/ctrl/set?iso=" + iso)
	
	def SetWB(self, wb):
		request = requests.get("http://192.168.11.160/ctrl/set?wb=" + wb)
	
	def SetmWB(self, mwb):
		request = requests.get("http://192.168.11.160/ctrl/get?k=mwb")
		request.encoding = "UTF-8"
		state = json.loads(request.content)
		if int(mwb) < int(state['min']):
			mwb = state['min']
		if int(mwb) > int(state['max']):
			mwb = state['max']
		request = requests.get("http://192.168.11.160/ctrl/set?wb=Manual")
		request = requests.get("http://192.168.11.160/ctrl/set?mwb=" + str(mwb))
	
	def SetAngle(self, angle):
		if angle != 'Auto':
			angle = angle + u'\xb0'
		request = requests.get("http://192.168.11.160/ctrl/set?shutter_angle=" + angle)
	
	def SaveRecordingImage(self, recimage):
		self.recimage = recimage

	def RecordingOn(self, row, col, name):
		self.FixGrid(row, col, 1, 1)
		self.AddImage(row, col, name, 1, 1, 1)
		self.recording = True
		self.starttime = time.time()


	def RecordingOff(self, row, col, name):
		self.FixGrid(row, col, 1, 1)
		self.AddImage(row, col, name, 1, 1, 1)
		self.recording = False
		self.starttime = 0
				
	def Recording(self):
		return self.recording

	def RunningTime(self):
		if self.recording == True:
			return str(datetime.timedelta(seconds=int(time.time() - self.starttime)))
		else:
			return '00:00:00'

	def AddClickArea(self, row, col, rowspan, colspan, cmd):
		if cmd != '':
			x = int(col * self.cellwidth + 3)
			y = int(row * self.cellheight + 3)
			width = int(self.cellwidth * colspan - 6)
			height = int(self.cellheight * rowspan - 6)
			clickarea = (x, x + width, y, y + height, cmd)
			self.clickareas.append (clickarea)
		
	def GetCommandFromClick(self, touchpos):
		x = touchpos[0]
		y = touchpos[1]
		for clickarea in self.clickareas:
			if clickarea[0] < x and clickarea[1] > x and clickarea[2] < y and clickarea[3] > y:
				return clickarea[4]
		return ''
				
	def AddLabel(self, row, col, text, factor, fontsize, rowspan, colspan, centered):
		font = self.pygame.font.Font(None,fontsize)
		label = font.render(str(text), 1, (self.text))
		rect = label.get_rect()
		x = col * self.cellwidth
		if centered == 1 or centered == 2:
			x += (self.cellwidth * colspan - rect[2]) / 2 
		y = row * self.cellheight + (self.cellheight * rowspan * factor)
		if centered == 2:
			y += (self.cellheight * rowspan - rect[3]) / 3 
		self.screen.blit(label,(x,y))

	def AddImage(self, row, col, name, factor, rowspan, colspan):
		image = self.pygame.image.load('./img/' + name + '.png')
		rect = image.get_rect()
		x = col * self.cellwidth + ((self.cellwidth * colspan - rect[2]) / 2)
		y = row * self.cellheight + ((self.cellheight * rowspan - rect[3]) / 2) * factor
		self.screen.blit(image, (x, y))

	def TextButton(self, row, col, text, rowspan, colspan, cmd, fontsize = 48):
		self.FixGrid(row, col, rowspan, colspan)
		self.AddLabel(row, col, text, 0.15, fontsize, rowspan, colspan)
		self.AddClickArea(row, col, rowspan, colspan, cmd)
			
	def CenteredTextButton(self, row, col, text, rowspan, colspan, cmd, fontsize = 48):
		self.FixGrid(row, col, rowspan, colspan)
		self.AddLabel(row, col, text, 0.15, fontsize, rowspan, colspan, 2)
		self.AddClickArea(row, col, rowspan, colspan, cmd)

	def TextButton(self, row, col, text, rowspan, colspan, cmd, fontsize = 48):
		self.FixGrid(row, col, rowspan, colspan)
		self.AddLabel(row, col, text, 0.15, fontsize, rowspan, colspan, 0)
		self.AddClickArea(row, col, rowspan, colspan, cmd)

	def GraphicButton(self, row, col, name, rowspan, colspan, cmd):
		self.FixGrid(row, col, rowspan, colspan)
		image = self.AddImage(row, col, name, 1, rowspan, colspan)
		self.AddClickArea(row, col, rowspan, colspan, cmd)
		return image

	def HybridButton(self, row, col, name, text, rowspan, colspan, cmd):
		self.FixGrid(row, col, rowspan, colspan)
		self.AddImage(row, col, name, 0.35, rowspan, colspan)
		self.AddLabel(row, col, text, 0.7, 48, rowspan, colspan, 1)
		self.AddClickArea(row, col, rowspan, colspan, cmd)

	def DoubleTextButton(self, row, col, text1, text2, rowspan, colspan, cmd, fontsize = 90):
		self.FixGrid(row, col, rowspan, colspan)
		self.AddLabel(row, col, text1, 0.2, fontsize, rowspan, colspan, 1)
		self.AddLabel(row, col, text2, 0.7, 48, rowspan, colspan, 1)
		self.AddClickArea(row, col, rowspan, colspan, cmd)


	def ClearScreen(self):
		self.clickareas = []
		self.screen.fill(self.background)
		#self.pygame.draw.rect(self.screen, self.accent, (0,0,719,719),1)
		
	def DrawGrid(self, rows, cols):
		self.rows = rows
		self.cols = cols

		self.cellwidth = int(self.size[0] / self.cols)
		self.cellheight = int(self.size[1] / self.rows)

		for x in range(self.cols-1):
			self.pygame.draw.line(self.screen, self.grid, (self.cellwidth * (x + 1), 0), (self.cellwidth * (x + 1), self.size[0] - 1), 4)

		for y in range(self.rows-1):
			self.pygame.draw.line(self.screen, self.grid, (0, self. cellheight * (y + 1)), (self.size[1], self.cellheight * (y + 1)), 4)

	def FixGrid(self, row, col, rowspan, colspan):
		if (rowspan > 0) and (colspan > 0):
			blockwidth = (self.cellwidth * colspan) - 4
			blockheight = (self.cellheight * rowspan) - 4 
			self.pygame.draw.rect(self.screen, self.background, (col * self.cellwidth + 2, row * self.cellheight + 2, blockwidth, blockheight))
		else:
			return (0,0)

	# Destructor
	#def __del__(self): 

