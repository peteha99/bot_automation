
from PIL import ImageGrab
import os
import time

import pyautogui
from ConfigClass import Coordinate
class Bot():
    pyautogui.FAILSAFE = False
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

    def reconnect_game(self):
        print("game start")
        time.sleep(5)
        action = pyautogui
        action.moveTo(Coordinate().closeTab)
        action.click(clicks=1)
        time.sleep(5)
        action.moveTo(Coordinate().playGame)
        action.click(clicks=1)
        action.moveTo(Coordinate().fullScreen)
        action.click(clicks=1)
        action.press("down",2)
        action.moveTo(500,912)
        time.sleep(5)
        action.moveTo(451,979)
        action.click(clicks=1)
        time.sleep(7)
        action.moveTo(Coordinate().display)
        action.click(clicks=1)
        time.sleep(10)
        
    def running(self,loseCount,betPrice,maxLoseCount):
        bet = 0
        if(loseCount <= maxLoseCount):
            bet = 1
            while(loseCount):
                bet*=2
                loseCount-=1
            # pyautogui.moveTo(Coordinate().bet10)
            # time.sleep(0.5)
            # Bot().mouse_action(1)
            # time.sleep(0.5)
            # pyautogui.moveTo(Coordinate().redBet)
            # Bot().mouse_action(bet)
            # time.sleep(0.5)
            # pyautogui.moveTo(Coordinate().comfirm)
            # time.sleep(0.5)
            bet = betPrice * bet
        else :
           print("wait for bet ")
           print(maxLoseCount)

        return bet

    def running_real(self,loseCount,betPrice,maxLoseCount):
        bet = 0
        if(loseCount <= maxLoseCount):
            bet = 1
            while(loseCount):
                bet*=2
                loseCount-=1
            pyautogui.moveTo(Coordinate().bet10)
            time.sleep(0.5)
            Bot().mouse_action(1)
            time.sleep(0.5)
            pyautogui.moveTo(Coordinate().redBet)
            Bot().mouse_action(bet)
            print("real bet ",bet)
            time.sleep(0.5)
            pyautogui.moveTo(Coordinate().comfirm)
            time.sleep(0.5)
            bet = betPrice * bet
        else :
           print("wait for bet")
        return bet
