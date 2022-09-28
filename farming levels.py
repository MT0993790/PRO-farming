from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from pynput.keyboard import Controller



loop = True
encounters = 0
turn = -1

# farming levels with misdreavus perish song, protect and momento trick
while loop:
    if pyautogui.locateOnScreen('wild.png', region=(550,275,825,310), grayscale=True, confidence=0.8) == None:
        stringa = random.randint(20,30) * "a"
        stringd = random.randint(20,30) * "d"
        whole = stringa + stringd
        for character in whole:
            keyboard.press_and_release(character)
            delay = 0.001
            time.sleep(delay)
    else:
        encounters += 1
        while pyautogui.locateOnScreen('wild.png', region=(550,275,825,310), grayscale=True, confidence=0.8) != None:
            turn += 1
            #perish song
            if turn != 3:
                while pyautogui.locateOnScreen('misdreavus_moves.png', region=(550,275,825,510), grayscale=True, confidence=0.8) == None:
                    keyboard.press_and_release("1")
                    time.sleep(0.6)
            if turn == 0:
                keyboard.press_and_release("1")
            if turn == 1:
                keyboard.press_and_release("2")
            if turn == 2:
                keyboard.press_and_release("3")
            if turn == 3:
                while pyautogui.locateOnScreen('choose_pokemon.png', region=(550,275,825,510), grayscale=True, confidence=0.8) == None:
                    time.sleep(1)
                keyboard.press_and_release("6")
                turn = -1
                while pyautogui.locateOnScreen('wild.png', region=(550,275,825,310), grayscale=True, confidence=0.8) != None:
                    time.sleep(2.8)
                    if pyautogui.locateOnScreen('no.png', region=(550,275,825,510), grayscale=True, confidence=0.8) != None:
                        button = pyautogui.locateOnScreen('no.png', region=(550,275,825,510), grayscale=True, confidence=0.8)
                        x, y = pyautogui.center(button)
                        pyautogui.click(x, y)
    if encounters == 5:
        loop = False