import itertools

def win(current_game):
   
    #horizontal
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] !=0:
            return True
        else:
            return False

    for row in game:
        print(row)
        if all_same(row):
            print (f"Player {row[0]} is the winner horizontally")
            return True
       

    #diagonal        
    r_diag = []
    l_diag = []
    for ix in range(len(game)):
        r_diag.append(game[ix][ix])
        l_diag.append(game[(2-length)-ix][ix])
    if all_same(r_diag):
        print (f"Player {r_diag[0]} is the winner diagonally (\\)")
        return True
       
    if all_same(l_diag):
        print (f"Player {l_diag[0]} is the winner reversed diagonally (/)")
        return True
    
    #vertical    
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print (f"Player {row[0]} is the winner vertically")
            return True

    return False        


def game_board(game_map, player=0, row=0, col=0, display= False):
    try:
        if game_map[row][col] != 0:
            print("This position is already filled!! Choose another")
            return game_map, False
        print( "   0  1  2 ")
        if not display:
            game_map[row][col] = player
        for count, row in enumerate(game_map):
            print(count,row), True
        return game_map, True

    except IndexError as e:
        print("Error:  ", e)
        return game_map, False

    except Exception as e:
        print("Error:  ", e)
        return game_map, False

play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]] #tic tac toe gme map
    length = len(game)  

    game_won = False
    game, _ = game_board(game, display = True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player  = next(player_choice) 
        print(f"Current Player is : {current_player}")
        played = False

        while not played:
            column_choice   = int(input("What column do you want to play?   (0, 1, 2): "))
            row_choice      = int(input("What row do you want to play?      (0, 1, 2): "))
            game, played    = game_board(game, current_player, row_choice, column_choice,)

        if win(game):
            game_won = True  
            again = input(" \n Game Over \n Do you wish to play again? (y/n)")            
            if again.lower() == "y":
                print(" Restarting... ")
            elif again.lower() == "n":
                print(" Thank you for playing :) ")      
                play = False
            else:
                print(" Option not present")
                play = False





'''
game = game_board(game, player = 2, row = 1, col=2)
game = game_board(game,  player = 1, row = 3, col=1)    
'''

