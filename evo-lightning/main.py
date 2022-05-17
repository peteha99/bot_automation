from BotClass import Bot
from ConfigClass import Status, Coordinate
import time
bot = Bot()

print(bot.grab_img().getpixel(Coordinate().betStatRound))
balance4 = 10000
balance8 = 10000
balance16 = 10000
balance32 = 10000
balance64 = 10000
betPrice = 25
loseCount = 0
loseStack = 0
winner = 0
betStack4 = 0
betStack8 = 0
betStack16 = 0
betStack32 = 0
betStack64 = 0
while True:
    
    while bot.grab_img().getpixel(Coordinate().greenBackground) == Status().connect:
        waitingRound = False
        betFinish = False
        calculate = False
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
            
            if(loseCount == 0 and calculate == False):
                temp4 = betStack4 * 2
                temp8 = betStack8 * 2
                temp16 = betStack16 * 2
                temp32 = betStack32 * 2
                temp64 = betStack64 * 2
                print("4",temp4)
                print("8",temp8)
                print("16",temp16)
                print("32",temp32)
                print("64",temp64)
                balance4 = balance4 + temp4
                balance8 = balance8 + temp8
                balance16 = balance16 + temp16
                balance32 = balance32 + temp32
                balance64 = balance64 + temp64

                print("total4",balance4)
                print("total8",balance8)
                print("total16",balance16)
                print("total32",balance32)
                print("total64",balance64)
                calculate = True
            
            if(betFinish == False):
                print("start bet")
                
                betStack4 = bot.running4(loseCount,betPrice)
                betStack8 = bot.running8(loseCount,betPrice)
                betStack16 = bot.running16(loseCount,betPrice)
                betStack32 = bot.running32(loseCount,betPrice)
                betStack64 = bot.running64(loseCount,betPrice)
                balance4 = balance4 - betStack4
                balance8 = balance8 - betStack8
                balance16 = balance16 - betStack16
                balance32 = balance32 - betStack32
                balance64 = balance64 - betStack64
                print("total4",balance4)
                print("total8",balance8)
                print("total16",balance16)
                print("total32",balance32)
                print("total64",balance64)
                betFinish = True
            
            
        while bot.grab_img().getpixel(Coordinate().betStatRound) != Status().redBetReady and bot.grab_img().getpixel(Coordinate().greenBackground) == Status().connect:
            print("waiting")
            

    bot.reconnect_game()
