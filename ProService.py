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


def walk(min, max): # takes a min and max amount of steps
    stringa = random.randint(min,max) * "a"
    stringd = random.randint(min,max) * "d"
    whole = stringa + stringd
    for character in whole:
        keyboard.type(character)
        delay = 0.001
        time.sleep(delay)

def locate_pokemon(pokemon): # locates the given pokemon
    return pyautogui.locateOnScreen(pokemon + '.png', region=(750,275,825,310), grayscale=True, confidence=0.8) != None

def notify(): # sends a push note to the Pushbullet application on your phone
    push = pb.push_note('NOTIFY', 'FOUND A SHINY')

def rare_catch(method): # defines how to handle an event or shiny pokemon
    notify()
    click_ok()
    catch(method)

def click_ok(): # clicks away the "you have found a rare pokemon" pop up
    button = pyautogui.locateOnScreen('ok.png', region=(550,275,825,510), grayscale=True, confidence=0.8)
    x, y = pyautogui.center(button)
    pyautogui.click(x, y)

def check_poison(): # checks and heals poisoned pokemon
    if pyautogui.locateOnScreen('psn.png', region=(0,275,475,470), grayscale=True, confidence=0.8) != None:
        button = pyautogui.locateOnScreen('pecha_berry.png', confidence=0.8)
        x, y = pyautogui.center(button)
        pyautogui.click(x, y)
        time.sleep(1)
        button = pyautogui.locateOnScreen('give_marowak.png', grayscale=True, confidence=0.8)
        x, y = pyautogui.center(button)
        pyautogui.click(x, y)


class battle_actions: # defines every action that can be used in battles
    def breloom(method): # a given method used on breloom to make pokemon weak to catch
        while pyautogui.locateOnScreen('choose_pokemon.png', region=(550,275,825,510), grayscale=True, confidence=0.8) == None:
            if pyautogui.locateOnScreen('rare_encounter.png', grayscale=True, confidence=0.8) != None:
                rare_catch(method)
                return True
            keyboard.type("2")
            time.sleep(0.6)
        keyboard.type("2")
        return False

    def marowak(method): #  a given method used on marowak to make pokemon weak to catch
        while pyautogui.locateOnScreen('choose_pokemon.png', region=(550,275,825,510), grayscale=True, confidence=0.8) == None:
            if pyautogui.locateOnScreen('rare_encounter.png', grayscale=True, confidence=0.8) != None:
                rare_catch(method)
                return True
            keyboard.type("2")
            time.sleep(0.6)
        keyboard.type("3")
        return False

    def false_swipe(): # uses the move false swipe
        while pyautogui.locateOnScreen('choose_attack.png', region=(550,275,825,510), grayscale=True, confidence=0.8) == None:
            keyboard.type("1")
            time.sleep(0.6)
        keyboard.type("3")

    def spore(): # uses the move spore
        while pyautogui.locateOnScreen('choose_attack.png', region=(550,275,825,510), grayscale=True, confidence=0.8) == None:
            keyboard.type("1")
            time.sleep(0.6)
        keyboard.type("1")
        time.sleep(1)

    def throw_balls(): # throw balls at wild pokemon till pokemon is caught
        while pyautogui.locateOnScreen('wild_battle.png', region=(550,275,825,510), grayscale=True, confidence=0.8) != None:
            while pyautogui.locateOnScreen('choose_item.png', region=(550,275,825,510), grayscale=True, confidence=0.8) == None and pyautogui.locateOnScreen('wild.png', region=(550,275,825,510), grayscale=True, confidence=0.8) != None:
                keyboard.type("3")
                time.sleep(0.6)
            keyboard.type("1")

    def catch(method="onlyfs", gender=None): # catches pokemon based on method and certain gender
        if gender != None:
            if pyautogui.locateOnScreen(gender + '.png', region=(550,275,825,310), grayscale=True, confidence=0.8):
                catch(method)
                return True
            else:
                keyboard.type("4")

        elif method == "onlyfs" or method == "fsonly":
            if battle_actions.breloom(method):
                return True
            battle_actions.false_swipe()
            battle_actions.throw_balls()

        elif method == "onlyfs2" or method == "fsonly2":
            if battle_actions.marowak(method):
                return True
            battle_actions.false_swipe()
            battle_actions.throw_balls()

        elif method == "fsspore" or method == "sporefs":
            if battle_actions.breloom(method):
                return True
            battle_actions.false_swipe()
            battle_actions.spore()
            battle_actions.throw_balls()

        elif method == "spore":
            if battle_actions.breloom(method):
                return True
            battle_actions.spore()
            battle_actions.throw_balls()