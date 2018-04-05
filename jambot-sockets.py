import logging
logging.getLogger('socketIO-client-nexus').setLevel(logging.DEBUG)
logging.basicConfig()

import os
import pygame
from subprocess import call
from socketIO_client_nexus import SocketIO, LoggingNamespace

import config

# play
pygame.init()
pygame.mixer.init()
sfx_path = "/home/pi/jambot/sfx"


def on_connect():
    print('connect')
    socketIO.emit('jambot')


def on_disconnect():
    print('disconnect')


def on_reconnect():
    print('reconnect')


def on_say(words):
    print('on_say', words)
    call(['espeak "' + words + '"'], shell=True)


def on_play(file):
    print('on_play', file)
    pygame.mixer.music.load("%s/%s" % (sfx_path, file))
    pygame.mixer.music.play()


socketIO = SocketIO(config.websocket["url"],
                    config.websocket["port"], LoggingNamespace)
socketIO.on('connect', on_connect)
socketIO.on('disconnect', on_disconnect)
socketIO.on('reconnect', on_reconnect)

# Listen
socketIO.on('say', on_say)
socketIO.on('play', on_play)
socketIO.wait()
