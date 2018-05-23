import os
import time
import json

ship_requirement = 10
damage_requirement = 1000


def get_ships(data):
    return int(data.split("producing ")[1].split(" ships")[0])

def get_damage(data):
    return int(data.split("dealing ")[1].split(" damage")[0])

def get_rank(data):
    return int(data.split("rank #")[1].split(" and")[0])

player_1_wins = 0
player_2_wins = 0
player_3_wins = 0
player_4_wins = 0
number_of_bots = 4

for num in range(1000):
    try:
        print("Currently on: {}".format(num))
        total_wins = player_1_wins + player_2_wins + player_3_wins + player_4_wins
        if player_1_wins > 0 or player_2_wins > 0 or player_3_wins > 0 or player_4_wins > 0:
            p1_pct = round(player_1_wins/(total_wins)*100.0, 2)
            p2_pct = round(player_2_wins/(total_wins)*100.0, 2)
            p3_pct = round(player_3_wins/(total_wins)*100.0, 2)
            p4_pct = round(player_4_wins/(total_wins)*100.0, 2)
            print("Player 1 win: {}%; Player 2 win: {}%;Player 3 win: {}%;Player 4 win: {}%.".format(p1_pct, p2_pct, p3_pct, p4_pct))


        bot_1 = '"python3 MyBot.py -name='+str(num)+'1" ' #enter the bot1 file name. Maintain the format.
        bot_2 = '"python3 MyBot.py -name='+str(num)+'2" ' #enter the bot2 file name. Maintain the format.
        bot_3 = '"python3 MyBot.py -name='+str(num)+'3" ' #enter the bot3 file name. Maintain the format.
        bot_4 = '"python3 MyBot.py -name='+str(num)+'4"'  #enter the bot4 file name. Maintain the format.

        cmd = './halite -d "240 160" ' + bot_1 + bot_2 + bot_3 + bot_4 + ' >> match.results'
        #print(cmd)
        os.system(cmd)

        with open('match.results', 'r') as f:
            contents = f.readlines()

            bot_log_1 = contents[-4]
            bot_log_2 = contents[-3]
            bot_log_3 = contents[-2]
            bot_log_4 = contents[-1]
            
            #Uncomment if you need to see the original format of logs
            print(bot_log_1)
            print(bot_log_2)
            print(bot_log_3)
            print(bot_log_4)

            bot_ships_1 = get_ships(bot_log_1)
            bot_dmg_1 = get_damage(bot_log_1)
            bot_rank_1 = get_rank(bot_log_1)
            
            bot_ships_2 = get_ships(bot_log_2)
            bot_dmg_2 = get_damage(bot_log_2)
            bot_rank_2 = get_rank(bot_log_2)
            
            bot_ships_3 = get_ships(bot_log_3)
            bot_dmg_3 = get_damage(bot_log_3)
            bot_rank_3 = get_rank(bot_log_3)
            
            bot_ships_4 = get_ships(bot_log_4)
            bot_dmg_4 = get_damage(bot_log_4)
            bot_rank_4 = get_rank(bot_log_4)

            print("Bot 1 rank: {} ships: {} dmg: {}".format(bot_rank_1,bot_ships_1,bot_dmg_1))
            print("Bot 2 rank: {} ships: {} dmg: {}".format(bot_rank_2,bot_ships_2,bot_dmg_2))
            print("Bot 3 rank: {} ships: {} dmg: {}".format(bot_rank_3,bot_ships_3,bot_dmg_3))
            print("Bot 4 rank: {} ships: {} dmg: {}".format(bot_rank_4,bot_ships_4,bot_dmg_4))

        if bot_rank_1 == 1:
            print("bot1 won")
            player_1_wins += 1
#            with open("weight1.vec","r") as f:

 #           if bot_ships_1 >= ship_requirement and bot_dmg_1 >= damage_requirement:
            filename = "weight"+str(num)+"1.vec"
            with open(filename,"r") as f:
                input_lines = f.readlines()
            with open("winner.weights","a") as f:
                # f.write(str(num)+'1 : ')
                for l in input_lines:
                    f.write(l)
                f.write("$$")


            filename = "nn_output"+str(num)+"1.vec"
            with open(filename,"r") as f:
                output_lines = f.readlines()
            with open("winner_NN.output","a") as f:
                f.write(str(num)+'1 : ')
                for l in output_lines:
                    f.write(l)

        elif bot_rank_2 == 1:
            print("bot2 won")
            player_2_wins += 1
            # if bot_ships_3 >= ship_requirement and bot_dmg_2 >= damage_requirement:
            filename = "weight"+str(num)+"2.vec"
            with open(filename,"r") as f:
                input_lines = f.readlines()
            with open("winner.weights","a") as f:
                # f.write(str(num)+'2 : ')
                for l in input_lines:
                    f.write(l)
                f.write("$$")

                
            filename = "nn_output"+str(num)+"2.vec"
            with open(filename,"r") as f:
                output_lines = f.readlines()
            with open("winner_NN.output","a") as f:
                f.write(str(num)+'2 : ')
                for l in output_lines:
                    f.write(l)

        elif bot_rank_3 == 1:
            print("bot3 won")
            player_3_wins += 1
            # if bot_ships_3 >= ship_requirement and bot_dmg_3 >= damage_requirement:
            filename = "weight"+str(num)+"3.vec"
            with open(filename,"r") as f:
                input_lines = f.readlines()
            with open("winner.weights","a") as f:
                # f.write(str(num)+'3 : ')
                for l in input_lines:
                    f.write(l)
                f.write("$$")

                
            filename = "nn_output"+str(num)+"3.vec"
            with open(filename,"r") as f:
                output_lines = f.readlines()
            with open("winner_NN.output","a") as f:
                f.write(str(num)+'3 : ')
                for l in output_lines:
                    f.write(l)

        elif bot_rank_4 == 1:
            print("bot4 won")
            player_4_wins += 1
            #if bot_ships_4 >= ship_requirement and bot_dmg_4 >= damage_requirement:
            filename = "weight"+str(num)+"4.vec"
            with open(filename,"r") as f:
                input_lines = f.readlines()
            with open("winner.weights","a") as f:
                # f.write(str(num)+'4 : ')
                for l in input_lines:
                    f.write(l)
                f.write("$$")
                
            filename = "nn_output"+str(num)+"4.vec"
            with open(filename,"r") as f:
                output_lines = f.readlines()
            with open("winner_NN.output","a") as f:
                f.write(str(num)+'4 : ')
                for l in output_lines:
                    f.write(l)

        time.sleep(2)
    except Exception as e:
        print(str(e))
        time.sleep(1)