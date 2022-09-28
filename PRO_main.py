import ProService
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from pynput.keyboard import Controller as KeyboardController
from pushbullet import Pushbullet
from pynput.mouse import Button, Controller as MouseController

API_KEY = "o.VkYFfGZrQrsBwojE78slpyYC9LO4XqBK"
keyboard = KeyboardController()
mouse = MouseController()
pb = Pushbullet(API_KEY)

stepmin = 24
stepmax = 31

poke = "gible"
gender = None
method = "sporefs"

poke2 = "chansey"
gender2 = None
method2 = "spore"

count = 0
disconnects = 0

while 1:
    if pyautogui.locateOnScreen('wild_battle.png', region=(750,275,825,310), grayscale=True, confidence=0.8) == None:
        ProService.walk(stepmin, stepmax)
    elif ProService.locate_pokemon(poke):
        ProService.catch(method, gender)
        #ProService.check_poison()
    #elif ProService.locate_pokemon(poke2):
        #ProService.catch(method2, gender2)
    elif pyautogui.locateOnScreen('rare_encounter.png', grayscale=True, confidence=0.8) != None:
        ProService.notify()
        ProService.click_ok()
        ProService.catch("spore")
    else:
        keyboard.type("4")
    if count % 1500 == 0:
        if pyautogui.locateOnScreen('homescreen.png', grayscale=True, confidence=0.8) != None:
            # move the pointer
            mouse.position = (840, 750)
            # Press and release
            mouse.press(Button.left)
            mouse.release(Button.left)
            time.sleep(15)
            keyboard.type("5")
            time.sleep(2)
            disconnects += 1
    count += 1


