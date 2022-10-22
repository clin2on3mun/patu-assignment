import os
from helper import board, check_turn, check_winner

list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

playing = True

turn=0

prev_turn=-1;

complete = False



while playing:
    os.system('cls' if os.name=="nt" else "clear")
    board(list)
    if prev_turn==turn:
        print("invalid entry ,please pick another one")
    prev_turn=turn    
    print("Player " + str((turn%2)+1) + "'s turn: Pick your spot or press q to quit")
   

    choice=input()
    
    if choice=='q':
        playing=False
    elif str.isdigit(choice) and int(choice) in list:
        if not list[int(choice)-1] in {'X','O'}:
            turn +=1;
            list[int(choice)-1]=check_turn(turn)

    if check_winner(list): playing, complete=False, True
    if turn>15: playing = False
    
    
os.system('cls' if os.name=="nt" else "clear")
board(list)
if complete:
    if check_turn(turn)=='X': print("player 1 wins")
    else:("player 2 wins")

else:
    print("No winner")

print("Thanks for playing")



   
    
    


            

