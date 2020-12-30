import requests
import pygame
import json

# initialize game engine
pygame.init()

window_width=800
window_height=480

animation_increment=10
clock_tick_rate=20

# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)


# Set title to the window
pygame.display.set_caption("Hello World")

dead=False

clock = pygame.time.Clock()
background_image = pygame.image.load("assets\Main Screen2.png").convert()



#startup requests
model = requests.get('http://192.168.1.7/info')
left_gain = requests.get('http://192.168.1.7/ctrl/get?k=audio_in_l_gain')
right_gain = requests.get('http://192.168.1.7/ctrl/get?k=audio_in_r_gain')
assist_tools = requests.get('http://192.168.1.7/ctrl/get?k=assitool_display')
assist_exposure = requests.get('http://192.168.1.7/ctrl/get?k=assitool_exposure')
shutter_operation = requests.get('http://192.168.1.7/ctrl/get?k=sht_operation')
shutter_speed = requests.get('http://192.168.1.7/ctrl/get?k=shutter_time')
shutter_angle = requests.get('http://192.168.1.7/ctrl/get?k=shutter_angle')
iso_control = requests.get('http://192.168.1.7/ctrl/get?k=iso_ctrl')
iso = requests.get('http://192.168.1.7/ctrl/get?k=iso')
iris = requests.get('http://192.168.1.7/ctrl/get?k=iris')
eND = requests.get('http://192.168.1.7/ctrl/get?k=eND')
FPS = requests.get('http://192.168.1.7/ctrl/get?k=project_fps')
VFR = requests.get('http://192.168.1.7/ctrl/get?k=movvfr')
codec = requests.get('http://192.168.1.7/ctrl/get?k=video_encoder')
image = requests.get('http://192.168.1.7/ctrl/get?k=lut')
resolution = requests.get('http://192.168.1.7/ctrl/get?k=resolution')
card_space = requests.get('http://192.168.1.7/ctrl/rec?action=remain')
white_balance = requests.get('http://192.168.1.7/ctrl/get?k=wb')
battery = requests.get('http://192.168.1.7/ctrl/get?k=battery_voltage')



#print the response text (the content of the requested file):

# print(white_balance.json())


while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    screen.blit(background_image, [0, 0])

    pygame.display.flip()
    clock.tick(clock_tick_rate)