from PIL import ImageGrab
import os
import time
from numpy import *

import pyautogui
from ConfigClass import *
class Bot():
    def __init__(self):
        self.image_grab = ImageGrab
        self.main_path = os.path.dirname(__file__)
        self.path_photo = os.path.join(self.main_path,"photo")
    
    def grab_img(self):
        x = 1
        y = 80
        self.box = (x,y)
        img = self.image_grab.grab().convert("RGB")
        return img
        # img = self.image_grab.grab().convert("RGB")
        # img.save(f"{self.path_photo}/xxxx.jpg")

    def mouse_action(self):
        action = pyautogui
        currentMouseX, currentMouseY = action.position()
        print(currentMouseX)
        print(currentMouseY)
        # action.moveTo(coordinate[0],coordinate[1])
        action.click(clicks=1)
        
    def start_game(self):
        action = pyautogui
        action.moveTo(Coordinate().connectGame)
        action.click(clicks=2)
        time.sleep(7)
        action.moveTo(Coordinate().history)
        action.click(clicks=1)
        
    def running(self):
        action = pyautogui
    
bot = Bot()
# bot.mouse_action((50,50))
# bot.start_game()
# print(bot.grab_img().getpixel(Coordinate().redBetStat))
print(bot.grab_img().load()[Coordinate().trackHistory])
# bot.grab_img()