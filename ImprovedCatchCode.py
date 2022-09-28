from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import ProService
from pynput.keyboard import Controller

while 1:
    if pyautogui.locateOnScreen(pokemon + '.png', region=(550,275,825,510), grayscale=True, confidence=0.8) != None:
        rare_counter = 0
        while pyautogui.locateOnScreen('choose_pokemon.png', region=(550,275,825,510), grayscale=True, confidence=0.8) == None:
            keyboard.press_and_release("2")
            time.sleep(0.6)
            rare_counter += 1
            if rare_counter % 20 == 0:
                ProService.rare_catch(pokemon, method)
        keyboard.press_and_release("2")
        while pyautogui.locateOnScreen('choose_attack.png', region=(550,275,825,510), grayscale=True, confidence=0.8) == None:
            keyboard.press_and_release("1")
            time.sleep(0.6)
        keyboard.press_and_release("3")
        while pyautogui.locateOnScreen('wild_battle.png', region=(550,275,825,510), grayscale=True, confidence=0.8) != None:
            while pyautogui.locateOnScreen('choose_item.png', region=(550,275,825,510), grayscale=True, confidence=0.8) == None and pyautogui.locateOnScreen('wild_battle.png', region=(550,275,825,510), grayscale=True, confidence=0.8) != None:
                keyboard.press_and_release("3")
                time.sleep(0.6)
            keyboard.press_and_release("1")
    else:
        keyboard.press_and_release("4")
    ProService.walk(20, 30)

