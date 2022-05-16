from BotClass import Bot
from ConfigClass import Status, Coordinate
import time
bot = Bot()

print(bot.grab_img().getpixel(Coordinate().betStatRound))

while True:
    loseCount = 0
    
    while bot.grab_img().getpixel(Coordinate().greenBackground) == Status().connect:
        waitingRound = False
        betFinish = False
        print("in loop connect")
        while bot.grab_img().getpixel(Coordinate().betStatRound) == Status().redBetReady and bot.grab_img().getpixel(Coordinate().greenBackground) == Status().connect:
            print(loseCount)
            time.sleep(3)
            if(bot.grab_img().getpixel(Coordinate().trackHistory) != Status().redWin and waitingRound == False):
                loseCount = loseCount + 1
            elif (bot.grab_img().getpixel(Coordinate().trackHistory) == Status().redWin and waitingRound == False):
                loseCount = 0
            waitingRound = True
            
            if(betFinish == False):
                print("start bet")
                print(betFinish)
                betFinish = bot.running(loseCount)
                print(betFinish)
                
            
            
        while bot.grab_img().getpixel(Coordinate().betStatRound) != Status().redBetReady and bot.grab_img().getpixel(Coordinate().greenBackground) == Status().connect:
            print("waiting")
            

    # bot.start_game()