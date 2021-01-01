# -*- coding: utf-8 -*-

import sys, os, time, datetime, subprocess, pygame, requests, json

class zUI:

	# Constructor
	def __init__(self, pygame, screen, size):
		# Save values
		self.pygame = pygame
		self.screen = screen
		self.rows = 0
		self.cols = 0
		self.size = size
		
		self.ipaddress = '192.168.11.160'
		self.root = '/home/pi/python/zremote'
			
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
		
		self.pollstart = time.time()
	
		self.WaitForConnection()

	def RequestGet(self, params):
		# print("http://" + self.ipaddress + params)
		try:
			request = requests.get("http://" + self.ipaddress + params, timeout=5)
		except Exception as e:
			sys.exit(e)
		else:
			return request
	
	def WaitForConnection(self):
		font = self.pygame.font.Font(None,90)
		label = font.render('Waiting for connection', 1, (self.text))
		rect = label.get_rect()
		self.screen.blit(label,(0,0))
		self.pygame.display.update()

		connected = False
		while not connected:
			try:
				request = requests.get("http://192.168.11.160/ctrl/mode?action=query")
			except:				
				connected = False
				try:
					request = requests.get("http://10.98.32.1/ctrl/mode?action=query")
				except:				
					connected = False
					time.sleep(1)
				else:
					connected = True
					self.ipaddress = '10.98.32.1'
			else:
				connected = True
				print ('Hello')
				self.ipaddress = '192.168.11.160'
		
	def FixDot(self, tofix):
		return tofix.replace('|', '.')
		
		
	def ISO(self):
		return self.iso

	def LUT(self):
		return self.lut

	def WB(self):
		return self.wb

	def mWB(self):
		return self.mwb

	def Resolution(self):		
		return self.movres.replace('(Low Noise)', 'LN')
		
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
		request = self.RequestGet("/ctrl/get?k=iso")
		request.encoding = "UTF-8"
		state = json.loads(request.content)
		self.iso = state['value']

		request = self.RequestGet("/ctrl/get?k=shutter_angle")
		request.encoding = "UTF-8"
		state = json.loads(request.content)
		self.angle = state['value'].replace(u'\xb0', '')

		request = self.RequestGet("/ctrl/get?k=resolution")
		request.encoding = "UTF-8"
		state = json.loads(request.content)
		self.movres = state['value']
		request = self.RequestGet("/ctrl/get?k=project_fps")
		request.encoding = "UTF-8"
		state = json.loads(request.content)
		self.movfps = state['value']
		request = self.RequestGet("/ctrl/get?k=movvfr")
		request.encoding = "UTF-8"
		state = json.loads(request.content)
		self.movvfr = state['value']
		request = self.RequestGet("/ctrl/get?k=video_encoder")
		request.encoding = "UTF-8"
		state = json.loads(request.content)
		self.codec = state['value']
		request = self.RequestGet("/ctrl/get?k=lut")
		request.encoding = "UTF-8"
		state = json.loads(request.content)
		self.lut = state['value']
		request = self.RequestGet("/ctrl/get?k=wb")
		request.encoding = "UTF-8"
		state = json.loads(request.content)
		self.wb = state['value']
		if self.wb == 'Manual':
			request = self.RequestGet("/ctrl/get?k=mwb")
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
		request = self.RequestGet("/ctrl/set?iso=" + iso)
	
	def SetWB(self, wb):
		request = self.RequestGet("/ctrl/set?wb=" + wb)
	
	def SetAngle(self, angle):
		if angle != 'Auto':
			angle = angle + u'\xb0'
		request = self.RequestGet("/ctrl/set?shutter_angle=" + angle)
	
	def SetmWB(self, mwb):
		request = self.RequestGet("/ctrl/get?k=mwb")
		request.encoding = "UTF-8"
		state = json.loads(request.content)
		if int(mwb) < int(state['min']):
			mwb = state['min']
		if int(mwb) > int(state['max']):
			mwb = state['max']
		request = self.RequestGet("/ctrl/set?wb=Manual")
		request = self.RequestGet("/ctrl/set?mwb=" + str(mwb))
	
	def SetResolution(self, resolution):
		request = self.RequestGet("/ctrl/set?resolution=" + self.FixDot(resolution))
	
	def SetFPS(self, fps):
		request = self.RequestGet("/ctrl/set?project_fps=" + self.FixDot(fps))
	
	def SetVFR(self, vfr):
		request = self.RequestGet("/ctrl/set?movvfr=" + vfr)
	
	def SetLUT(self, lut):
		request = self.RequestGet("/ctrl/set?lut=" + self.FixDot(lut))
	
	def SetCodec(self, codec):
		request = self.RequestGet("/ctrl/set?video_encoder=" + self.FixDot(codec))
	
	def SetQuick(self, quick):
		try:
			filein = open(self.root + '/quick/' + quick + '.txt', 'r')
		except:
			fileout = open(self.root + '/quick/' + quick + '.txt', 'w')
			fileout.write('resolution=4K\n')
			fileout.write('video_encoder=ProRes 422\n')
			fileout.write('project_fps=25\n')
			fileout.write('movvfr=Off\n')
			fileout.write('lut=Z-Log2\n')
			fileout.write('shutter_angle=180°\n')
			fileout.write('wb=Manual\n')
			fileout.write('mwb=5600\n')
			fileout.close()
	
		# self.SetResolution('1920x1080')
		filein = open(self.root + '//quick/' + quick + '.txt', 'r')
		lines = filein.readlines()
		filein.close()
		for line in lines:
			request = self.RequestGet("/ctrl/set?" + line[:-1])
			
	def SaveRecordingImage(self, recimage):
		self.recimage = recimage

	def Poll(self):

		if (int(time.time() - self.pollstart)) > 0:
			request = self.RequestGet("/ctrl/mode?action=query")
			state = json.loads(request.content)
			recstate = state['msg']
		
			if (recstate == 'rec') and self.recording:
				self.FixGrid(0, 3, 1, 1)
				self.AddImage(0, 3, 'record', 1, 1, 1)
				self.recording = False
				self.starttime = 0
			
			if (recstate == 'rec_ing') and not self.recording:
				self.FixGrid(0, 3, 1, 1)
				self.AddImage(0, 3, 'stop', 1, 1, 1)
				self.recording = True
				self.starttime = time.time()
	
			self.pollstart = time.time()

	def RecordingOn(self, row, col, name):
		request = self.RequestGet("/ctrl/rec?action=start") 
		
		self.FixGrid(row, col, 1, 1)
		self.AddImage(row, col, name, 1, 1, 1)
		self.recording = True
		self.starttime = time.time()


	def RecordingOff(self, row, col, name):
		request = self.RequestGet("/ctrl/rec?action=stop")
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
		image = self.pygame.image.load(self.root + '/img/' + name + '.png')
		rect = image.get_rect()
		x = col * self.cellwidth + ((self.cellwidth * colspan - rect[2]) / 2)
		y = row * self.cellheight + ((self.cellheight * rowspan - rect[3]) / 2) * factor
		self.screen.blit(image, (x, y))

	def Wait(self):
		# print('wait')
		image = self.pygame.image.load(self.root + '/img/wait.png')
		self.screen.blit(image, (0, 0))
		self.pygame.display.update()

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

