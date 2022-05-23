from BotClass import Bot
from ConfigClass import Status, Coordinate
from DbConnect import Profile,Game
import time
from datetime import datetime
bot = Bot()
profile = Profile()
game = Game()
dataProfile = profile.all_profile()
dataProfiles = list(dataProfile)
id = 0
name = 1
solutionCode = 2
balance = 3
descrition = 4
winrate = 5


resGameHistory = []
betPrice = 10
loseCount = 0
loseStack = 0
winStack = 0
betStack = 0
isWin = False
tmpBet = 0


now = datetime.now()
timestamp = datetime.timestamp(now)
while True:
    
    while bot.grab_img().getpixel(Coordinate().greenBackground) == Status().connect:
        waitingRound = False
        betFinish = False
        calculate = False
        print("in loop connect")
        while bot.grab_img().getpixel(Coordinate().betStatRound) == Status().redBetReady and bot.grab_img().getpixel(Coordinate().greenBackground) == Status().connect:
            time.sleep(2)
            if(bot.grab_img().getpixel(Coordinate().trackHistory) != Status().redWin and waitingRound == False):
                color = "GREEN"
                if(bot.grab_img().getpixel(Coordinate().trackHistory) == Status().blackWin):
                    color = "BLACK"
                gameHistoryData = [(color,loseStack,timestamp)]
                loseCount = loseCount + 1
                loseStack = loseStack + 1
                winStack = 0
                tmpBet = tmpBet + 1
                resGameHistory = game.save_game_history(gameHistoryData)
                print("loseCount",loseCount)
            elif (bot.grab_img().getpixel(Coordinate().trackHistory) == Status().redWin and waitingRound == False):
                
                tmpBet = 0
                print("loseCount",loseCount)
                winStack = winStack + 1
                gameHistoryData = [('RED',winStack,timestamp)]
                resGameHistory = game.save_game_history(gameHistoryData)
            waitingRound = True
            
            if(winStack > 0 and calculate == False):
                isWin = True
                tempDataLoop = []
                for item in dataProfiles:
                    if(item[solutionCode] >= loseStack):
                        print("solution win")
                        print(item[solutionCode])
                        tempBalance = betStack * 2
                        profile.update_profile(item[balance] + tempBalance, item[0])
                        time.sleep(0.1)
                        print("balance")
                        print(tempBalance)
                dataProfile = profile.all_profile()
                dataProfiles = list(dataProfile)
                calculate = True
                loseCount = 0
                loseStack = 0

            if(betFinish == False):
                tmpData = []
                for i in range(len(dataProfiles)):
                    tmpData.append((dataProfiles[i][id],resGameHistory,isWin,now))
                profile.profile_history_insert(tuple(tmpData))
                print("start bet")
                for item in dataProfiles:
                    betStack = bot.running(loseCount,betPrice,item[solutionCode])
                    tempBalance = item[balance] - betStack
                    profile.update_profile(tempBalance, item[0])
                    time.sleep(0.1)
                # if(loseStack > 4 or loseStack == 0):
                # bot.running_real(loseCount,10,5)
                print("betStack")
                print(betStack)
                dataProfile = profile.all_profile()
                dataProfiles = list(dataProfile)
                betFinish = True
                print("waiting")
            
            
        while bot.grab_img().getpixel(Coordinate().betStatRound) != Status().redBetReady and bot.grab_img().getpixel(Coordinate().greenBackground) == Status().connect:
            val = []
            

    # bot.reconnect_game()