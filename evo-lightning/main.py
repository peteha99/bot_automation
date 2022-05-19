from BotClass import Bot
from ConfigClass import Status, Coordinate
from DbConnect import Profile
import time
bot = Bot()
profile = Profile()

# print(bot.grab_img().getpixel(Coordinate().betStatRound))
profile.all_profile()
while True:
    balance4 = 10000
    balance8 = 10000
    balance16 = 10000
    balance32 = 10000
    betPrice = 10
    loseCount = 0
    loseStack = 0
    winner = 0
    betStack4 = 0
    betStack8 = 0
    betStack16 = 0
    betStack32 = 0
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
                print("4",temp4)
                print("8",temp8)
                print("16",temp16)
                print("32",temp32)
                balance4 = balance4 + temp4
                balance8 = balance8 + temp8
                balance16 = balance16 + temp16
                balance32 = balance32 + temp32

                print("total4",balance4)
                print("total8",balance8)
                print("total16",balance16)
                print("total32",balance32)
                calculate = True
            
            if(betFinish == False):
                print("start bet")
                betStack4 = bot.running(loseCount,betPrice)
                betStack8 = bot.running4(loseCount,betPrice)
                betStack16 = bot.running16(loseCount,betPrice)
                betStack32 = bot.running32(loseCount,betPrice)
                balance4 = balance4 - betStack4
                balance8 = balance8 - betStack8
                balance16 = balance16 - betStack16
                balance32 = balance32 - betStack32
                print("total4",balance4)
                print("total8",balance8)
                print("total16",balance16)
                print("total32",balance32)
                betFinish = True
            
            
        while bot.grab_img().getpixel(Coordinate().betStatRound) != Status().redBetReady and bot.grab_img().getpixel(Coordinate().greenBackground) == Status().connect:
            print("waiting")
            

    # bot.start_game()
