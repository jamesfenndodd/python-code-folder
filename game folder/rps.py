
def draw():
    print("sorry this round was a draw")
#    rd = rd + 1
    print(rd)

def compwin():
    comp_sc = comp_sc + 1
    print(comp_sc)
    print("sorry the bot won this round")
 #   rd = rd + 1
    print(rd)

def plwin():
    player_sc = player_sc + 1
    print(player_sc)
    print("well done you won this round")
  #  rd = rd + 1
    print(rd)

def mainmenu():

    while rd<=3:
        comp = random.randint(1,3)
        player=int(input("enter 1 for paper 2 for scissors and 3 for rock"))
        rd+=1
        if comp == 1:
            if player == 2:
                plwin()
            elif player == 1:
                draw()
            else:
                compwin()
        elif comp == 2:
            if player == 3:
                plwin()
            elif player == 2:
                draw()
            else:
                compwin()
        elif comp == 3:
            if player == 1:
                plwin()
            elif player == 3:
                draw()
            else:
                compwin()
    print("thats the end of the game")
    if comp_sc > player_sc:
        print("the bot won the game with", comp_sc, "compared to your score of", player_sc,)
    else:
        print("you won the game with", player_sc, "compared to the bot's score of", comp_sc,)


rd = 0
player_sc = 0
comp_sc = 0

import random
print("hello and welcome to the rock paper scissors game")
mainmenu()

