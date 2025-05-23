import random
player_01="Player_01"
player_02="Player_02"
print()
#lst=['1','2','3','4','5','6','7','8','9']
lst=['-','-','-','-','-','-','-','-','-']
used=[]
corner=[0,2,6,8]
available=[0,1,2,3,4,5,6,7,8]

def board():
    lst_2d = [lst[i:i+3] for i in range(0, 9, 3)]
    print("                 ----- ----- -----")
    for i in range(3):
        print("                |  ",end="")
        for j in range(3):
            print(lst_2d[i][j],end="  |  ")
        print("")
        print("                 ----- ----- -----")
    print("\n\n")



def play_with_friend():
    board()
    print("\n\n             BEGINING THE MATCH WITH FRIEND.....\n")
    while True:
        while True:
            x=input(f"Player {player_01}: ")
            if x in ["1",'2',"3",'4','5','6','7','8','9']:
                x=int(x)-1
                if x not in used:
                    lst[x]="X"
                    board()
                    print("\n\n")
                    used.append(x)
                    break
        if lst[0]+lst[1]+lst[2]=="XXX" or lst[3]+lst[4]+lst[5]=="XXX" or lst[6]+lst[7]+lst[8]=="XXX" or lst[0]+lst[4]+lst[8]=="XXX" or lst[2]+lst[4]+lst[6]=="XXX" or lst[0]+lst[3]+lst[6]=="XXX" or lst[1]+lst[4]+lst[7]=="XXX" or lst[2]+lst[5]+lst[8]=="XXX":
            print(f"{player_01} won the match !!!")
            break
        elif len(used)==9:
            print("The game ended in a tie....")
            break

        while True:
            y=input(f"Player {player_02}: ")
            if y in ["1",'2',"3",'4','5','6','7','8','9']:
                y=int(y)-1
                if y not in used:
                    lst[y]="O"
                    board()
                    print("\n\n")
                    used.append(y)
                    break
        if lst[0]+lst[1]+lst[2]=="OOO" or lst[3]+lst[4]+lst[5]=="OOO" or lst[6]+lst[7]+lst[8]=="OOO" or lst[0]+lst[4]+lst[8]=="OOO" or lst[2]+lst[4]+lst[6]=="OOO" or lst[0]+lst[3]+lst[6]=="OOO" or lst[1]+lst[4]+lst[7]=="OOO" or lst[2]+lst[5]+lst[8]=="OOO":
            print(f"{player_02} won the match !!!")
            break
        elif len(used)==9:
            print("The game ended in a tie....")
            break




def play_with_bot():
    def check_winner_P():
        if lst[0]+lst[1]+lst[2]=="XXX" or lst[3]+lst[4]+lst[5]=="XXX" or lst[6]+lst[7]+lst[8]=="XXX" or lst[0]+lst[4]+lst[8]=="XXX" or lst[2]+lst[4]+lst[6]=="XXX" or lst[0]+lst[3]+lst[6]=="XXX" or lst[1]+lst[4]+lst[7]=="XXX" or lst[2]+lst[5]+lst[8]=="XXX":
            print(f"{player_01} won the match !!!")
            return True
        elif len(used)==9:
            print("The game ended in a tie....")
            return True
        return False

    def check_winner_C():
        if lst[0]+lst[1]+lst[2]=="OOO" or lst[3]+lst[4]+lst[5]=="OOO" or lst[6]+lst[7]+lst[8]=="OOO" or lst[0]+lst[4]+lst[8]=="OOO" or lst[2]+lst[4]+lst[6]=="OOO" or lst[0]+lst[3]+lst[6]=="OOO" or lst[1]+lst[4]+lst[7]=="OOO" or lst[2]+lst[5]+lst[8]=="OOO":
            print(f"BOT, won the match !!!")
            return True
        elif len(used)==9:
            print("The game ended in a tie....")
            return True
        return False

    board()
    print("\n\n             BEGINING THE MATCH WITH BOT.....\n")

    while True:
        while True:
            x=input(f"{player_01}: ")
            if x in ["1",'2',"3",'4','5','6','7','8','9']:
                x=int(x)-1
                if x not in used:
                    lst[x]="X"
                    board()
                    used.append(x)
                    available.remove(x)
                    if x==0 or x==2 or x==6 or x==8:
                        corner.remove(x)
                    break
        game=check_winner_P()
        if game == True:
            break


        while True:
            y=25
            for i in available:
                lst[i]="O"
                if lst[0]+lst[1]+lst[2]=="OOO" or lst[3]+lst[4]+lst[5]=="OOO" or lst[6]+lst[7]+lst[8]=="OOO" or lst[0]+lst[4]+lst[8]=="OOO" or lst[2]+lst[4]+lst[6]=="OOO" or lst[0]+lst[3]+lst[6]=="OOO" or lst[1]+lst[4]+lst[7]=="OOO" or lst[2]+lst[5]+lst[8]=="OOO":
                    y=i
                    break
                lst[i]="-"
            if check_winner_C():
                break

            block=False
            for i in available:
                lst[i]="X"
                if lst[0]+lst[1]+lst[2]=="XXX" or lst[3]+lst[4]+lst[5]=="XXX" or lst[6]+lst[7]+lst[8]=="XXX" or lst[0]+lst[4]+lst[8]=="XXX" or lst[2]+lst[4]+lst[6]=="XXX" or lst[0]+lst[3]+lst[6]=="XXX" or lst[1]+lst[4]+lst[7]=="XXX" or lst[2]+lst[5]+lst[8]=="XXX":
                    y=i
                    block=True
                    break
                lst[i]="-"
            if block:
                break

            if 4 in available:
                y=4
                break
            elif lst[0]=='-' or lst[2]=='-' or lst[6]=='-' or lst[8]=='-':
                y=random.choice(corner)
                break
            else:
                y=random.choice(available)
                break

        lst[y]="O"
        print(f"BOT: {y}")
        board()
        used.append(y)
        available.remove(y)
        game=check_winner_C()
        if y==0 or y==2 or y==6 or y==8:
            corner.remove(y)
        if game == True:
            break










print("\n                                       Welcome to  Tic_Tac_Toe")
print("\n\n1. Press 1 to play with Friend.")
print("2. Press 2 to play with BOT.\n")
while True: 
    x=input("Enter your choice: ")
    if x=='1' or x=='2':
        x=int(x)
        break
    else:
        print("OOps! Out of option.....")
print("\n\n\n")
if x==1:
    play_with_friend()
elif x==2:
    play_with_bot()