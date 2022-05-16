from BotClass import Bot
from ConfigClass import Status, Coordinate
import time
bot = Bot()

print(bot.grab_img().getpixel(Coordinate().betStatRound))

betPrice = 10
while True:
    loseCount = 0
    loseStack = 0
    winner = 0
    balance4 = 10000
    balance8 = 10000
    balance16 = 10000
    balance32 = 10000
    total4 = 0
    total8 = 0
    total16 = 0
    total32 = 0
    betStack4 = 0
    betStack8 = 0
    betStack16 = 0
    betStack32 = 0
    while bot.grab_img().getpixel(Coordinate().greenBackground) == Status().connect:
        waitingRound = False
        betFinish = False
        calculate = False
        isContinueBet = False
        print("in loop connect")
        while bot.grab_img().getpixel(Coordinate().betStatRound) == Status().redBetReady and bot.grab_img().getpixel(Coordinate().greenBackground) == Status().connect:
            print(loseStack)
            
            time.sleep(3)
            if(bot.grab_img().getpixel(Coordinate().trackHistory) != Status().redWin and waitingRound == False):
                loseCount = loseCount + 1
                loseStack = loseStack + 1
            elif (bot.grab_img().getpixel(Coordinate().trackHistory) == Status().redWin and waitingRound == False):
                loseCount = 0
                loseStack = 0
            waitingRound = True

            if(loseCount >= 7):
                loseCount = 0
                isContinueBet = True
            
            if(loseCount == 0 and isContinueBet == False and calculate == False):
                total4 = betStack4 * 2
                total8 = betStack8 * 2
                total16 = betStack16 * 2
                total32 = betStack32 * 2
                

                print("total4",total4)
                print("total8",total8)
                print("total16",total16)
                print("total32",total32)
                calculate = True
            
            if(betFinish == False):
                print("start bet")
                betStack4 = bot.running(loseCount,betPrice)
                betStack8 = bot.running4(loseCount,betPrice)
                betStack16 = bot.running16(loseCount,betPrice)
                betStack32 = bot.running32(loseCount,betPrice)
                total4 = balance4 - betStack4
                total8 = balance8 - betStack8
                total16 = balance16 - betStack16
                total32 = balance32 - betStack32
                print("total4",total4)
                print("total8",total8)
                print("total16",total16)
                print("total32",total32)
                betFinish = True
            
            
        while bot.grab_img().getpixel(Coordinate().betStatRound) != Status().redBetReady and bot.grab_img().getpixel(Coordinate().greenBackground) == Status().connect:
            print("waiting")
            

    # bot.start_game()