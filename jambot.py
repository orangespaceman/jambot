import os
import random
import time
import RPi.GPIO as GPIO
import pygame

# button
buttonSwitchPin = 23
buttonState = 0
lastButtonState = 0

# play
is_playing = False
pygame.init()
pygame.mixer.init()
sfx_path = "/home/pi/jambot/sfx"

# GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonSwitchPin, GPIO.IN)

while True:
    # get state
    is_playing = pygame.mixer.music.get_busy()
    buttonState = GPIO.input(buttonSwitchPin)

    # play
    if buttonState is 1 and lastButtonState is not 1 and is_playing is not True:
        sfx = random.choice(os.listdir(sfx_path))
        pygame.mixer.music.load("%s/%s" % (sfx_path, sfx))
        pygame.mixer.music.play()
        print sfx

    lastButtonState = buttonState
    time.sleep(0.5)
