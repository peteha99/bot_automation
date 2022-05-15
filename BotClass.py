from multiprocessing.connection import wait
from PIL import ImageGrab
import os
import time
from numpy import *

import pyautogui
from regex import B, P
from ConfigClass import Coordinate
class Bot():
    def __init__(self):
        self.image_grab = ImageGrab
        self.main_path = os.path.dirname(__file__)
        self.path_photo = os.path.join(self.main_path,"photo")
    
    def grab_img(self):
        img = self.image_grab.grab().convert("RGB")
        return img

    def mouse_action(self,click):
        action = pyautogui
        action.click(clicks=click)
        
    def start_game(self):
        print("game start")
        time.sleep(5)
        action = pyautogui
        action.moveTo(Coordinate().connectGame)
        action.click(clicks=2)
        time.sleep(7)
        action.moveTo(Coordinate().history)
        action.click(clicks=1)
        time.sleep(10)
    def running(self,loseCount):
        result = False
        match loseCount:
            case 0:
                pyautogui.moveTo(Coordinate().bet50)
                time.sleep(0.5)
                Bot().mouse_action(1)
                time.sleep(0.5)
                pyautogui.moveTo(Coordinate().redBet)
                Bot().mouse_action(1)
                result = True
                print("bet 1")
                time.sleep(0.5)
            case 1:
                pyautogui.moveTo(Coordinate().bet50)
                time.sleep(0.5)
                Bot().mouse_action(1)
                time.sleep(0.5)
                pyautogui.moveTo(Coordinate().redBet)
                Bot().mouse_action(2)
                result = True
                print("bet 2")
                time.sleep(0.5)
            case 2:
                pyautogui.moveTo(Coordinate().bet50)
                time.sleep(0.5)
                Bot().mouse_action(1)
                time.sleep(0.5)
                pyautogui.moveTo(Coordinate().redBet)
                Bot().mouse_action(4)
                result = True
                print("bet 4")
                time.sleep(0.5)
            case _:
                print("finish")
                result = True
        pyautogui.moveTo(Coordinate().comfirm)
        time.sleep(0.5)
        Bot().mouse_action(1)
        return result
