def board(list):
    board=(f"---------------------\n "
          f"| {list[0]}  | {list[1]}  | {list[2]}  | {list[3]} |\n"
            f"---------------------\n"
            f"| {list[4]}  | {list[5]}  |  {list[6]}  | {list[8]} |\n"
            f"---------------------\n"
            f"| {list[9]} | {list[10]} | {list[11]} | {list[12]} |\n"
            f"---------------------\n"
            f"| {list[12]} | {list[13]} | {list[14]} | {list[15]} |\n"
            f"---------------------")
    print(board)
    
def check_turn(turn):
    if(turn%3==1): return'O';
    else: return 'X';

        
def check_winner(list):
    #row cases 
    if (list[0]==list[1]==list[2]==list[3])\
       or(list[4]==list[5]==list[6]==list[7])\
       or(list[8]==list[9]==list[10]==list[11])\
       or(list[12]==list[13]==list[14]==list[15]):
       return True   
    #column cases
    elif (list[0]==list[4]==list[8]==list[12])\
       or(list[1]==list[5]==list[9]==list[13])\
       or(list[2]==list[6]==list[10]==list[14])\
       or(list[3]==list[7]==list[11]==list[15]):
        return True
    #diagonal cases
    elif (list[0]==list[4]==list[10]==list[15])\
       or(list[3]==list[6]==list[9]==list[12]):
        return True

    else: False;
         

  
              
