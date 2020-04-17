import random

# models for game pieces, players, ships, board(s)

#Piece class
"""class PieceClass:
    def __init__(self, char, rowX, colY, num_colY):
        self.char = char
        self.rowX = rowX
        self.colY = colY
        self.act_rowX = chr(ord('@') + (rowX//2))
        self.act_colY = num_colY
    #CREATE FUNCTION FOR RUNNING ALL FUNCTIONS
"""
#Board class
class BoardClass:
    def __init__(self, file):
        self.file = file
        #self.board_data = []
        self.raw_board_data = []
        self.raw_attack_board_data = []
        self.game_board = []
        self.game_attack_board = []
        #self.board_pieces = []
        self.boats_placed = []
        self.max_col = 10
        self.max_row = 'J'

    def create_game_board(self):
        while("" in self.raw_board_data):
            self.raw_board_data.remove("")
        for i in range(len(self.raw_board_data)):
            board_row = []
            for j in range(len(self.raw_board_data[i])):
                if(self.raw_board_data[i][j] == ' ' and i >= 2 and i <= 21 and j >= 4):
                    board_row.append(-1)
                else:
                    board_row.append(self.raw_board_data[i][j])
            self.game_board.append(board_row)

    def create_game_attack_board(self):
        while("" in self.raw_board_data):
            self.raw_board_data.remove("")
        for i in range(len(self.raw_board_data)):
            board_row = []
            for j in range(len(self.raw_board_data[i])):
                if(self.raw_board_data[i][j] == ' ' and i >= 2 and i <= 21 and j >= 4):
                    board_row.append(-1)
                else:
                    board_row.append(self.raw_board_data[i][j])
            self.game_attack_board.append(board_row)

    #prints game board
    def print_board_data(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j] == -1):
                    print(' ', end="")
                else:
                    print(board[i][j], end="")
            print()
        print('\n')

    #print game board file
    def print_board_file(self):
        with open(self.file) as f:
            print(f.read() + "\n\n")
        f.closed

    #reads a file and saves data into 2d array - for game board population
    def read_board_file(self):
        with open(self.file) as f:
            #self.view_board_data = [line.split('\n') for line in f]
            for line in f:
                for i in line.split('\n'):
                    self.raw_board_data.append(i)
        """    for line in f:
                for i in line.strip().split('\n'):
                    self.board_data.append(i)"""
        f.closed
    
    #sorts through file 2d array and identifies valid points
    """
    def clean_board_file(self):
        num_rowX = 1
        for row in range(len(self.board_data)):
            num_colY = 0
            for col in range(len(self.board_data[row])):
                if(self.board_data[row][col:col+3] == '| |'):
                    num_colY+=1
                    if (num_colY > self.max_col):
                        self.max_col = num_colY
                    new_piece = PieceClass(self.board_data[row][col+1], row, col+1, num_colY)
                    self.board_pieces.append(new_piece)
            num_rowX+=1
            if(num_rowX > ord(self.max_row)):
                self.max_row = chr(ord('@') + (num_rowX//2))
                """
        
        #print cords of board
        #for i in self.board_pieces:
            #print(str(i.rowX) + ' ' + str(i.colY))
    
    def place_ship_validate_x(self, temp_ship, board, dist, head, y):
        if(board.game_board[head][y - 1] == -1):
            for x in range(dist):
                if(board.game_board[head][y - 1] == -1):
                    head += 2
                else:
                    return(False)
            return(True)
        else:
            return (False)

    def place_ship_validate_y(self, temp_ship, board, dist, head, x):
        if(board.game_board[x][head - 1] == -1):
            for d in range(dist):
                if(board.game_board[x][head - 1] == -1):
                    head += 2
                else:
                    return(False)
            return(True)
        else:
            return(False)

    #completes validation of coords and places ship on board
    def place_ship_board(self, valid_cord, temp_ship, board):
        #loop through board
        if(valid_cord[0][0] != valid_cord[1][0] and int(valid_cord[0][1: len(valid_cord[1])]) == int(valid_cord[1][1: len(valid_cord[1])])):
            dist = abs(ord(valid_cord[0][0]) - ord(valid_cord[1][0])) + 1
            if(dist == temp_ship.ship_length):
                #if the row specified first is greater, make second head
                if(valid_cord[0][0] > valid_cord[1][0]):
                    head = int(abs((ord(valid_cord[0][1]) - ord('@')) * 2) + 3)
                else:
                    head = int(abs((ord(valid_cord[0][0]) - ord('@')) * 2) + 3)
                x = int(valid_cord[0][1: len(valid_cord[0])]) * 2
                #validation for future placement
                if(self.place_ship_validate_y(temp_ship, board, dist, head, x)):
                    for d in range(dist):
                        if(board.game_board[x][head - 1] == -1):
                            board.game_board[x][head - 1] = temp_ship.ship_char
                            head += 2
                        else:
                            break
                    self.print_board_data(self.game_board)
                else:
                    self.print_board_data(self.game_board)
                    raise Exception("Coordinates overlap an existing ship")
                return(False)
            else:
                raise Exception("ERROR: Invalid entry, (" + valid_cord[0][0] + ", " + valid_cord[0][1: len(valid_cord[1])] + "), " + 
                "(" + valid_cord[1][0] + ", " + valid_cord[1][1: len(valid_cord[1])] + ") row does not match")
        else:
            if(int(valid_cord[0][1: len(valid_cord[0])]) >= 10 or int(valid_cord[1][1 : len(valid_cord[1])]) >= 10):
                dist = abs(int(valid_cord[0][1: len(valid_cord[0])]) - int(valid_cord[1][1 : len(valid_cord[1])])) + 1
            else:
                dist = abs(int(valid_cord[0][1]) - int(valid_cord[1][1])) + 1
            if(dist == temp_ship.ship_length):
                if(int(valid_cord[0][1: len(valid_cord[0])]) > int(valid_cord[1][1 : len(valid_cord[1])])):
                    head = (int(valid_cord[1][1 : len(valid_cord[1])]) * 2)
                else:
                    head = (int(valid_cord[0][1: len(valid_cord[0])]) * 2)
                y = int(abs((ord(valid_cord[0][0]) - ord('@')) * 2) + 3)
                #validation for future placement
                if(self.place_ship_validate_x(temp_ship, board, dist, head, y)):
                    for x in range(dist):
                        if(board.game_board[head][y - 1] == -1):
                            #piece placement after validation
                            board.game_board[head][y - 1] = temp_ship.ship_char
                            head += 2
                        else:
                            break
                    self.print_board_data(self.game_board)
                else:
                    self.print_board_data(self.game_board)
                    raise Exception("Coordinates overlap an existing ship")
                return(False)
            else:
                raise Exception("ERROR: Invalid entry, does not meet boat size. ("+ valid_cord[0][0: len(valid_cord[0])] + ")" + 
                "(" + valid_cord[1][0: len(valid_cord[1])] + ") distance is " + str(dist))
            

#Ship class
class ShipClass:
    def __init__(self, ship_length, ship_type, ship_char):
        self.ship_length = ship_length
        self.ship_type = ship_type
        self.ship_char = ship_char
        self.ship_cord_store = []
        self.ship_hit_count = 0

    #validates syntax of coordinates
    def ship_cord_validate(self, temp_ship, board):
        d = True
        while(d):
            # if player type is player
            valid_cord = []
            temp_cords = input("\nPlease select coordinate range for - \n\n" + temp_ship.ship_type + 
            "\nsize: " + str(temp_ship.ship_length) + "\n\ncoordinates:")
            try: 
                for i in temp_cords.strip().split(' '):
                        valid_cord.append(i)              
                if(len(valid_cord) != 2):
                    raise Exception("ERROR: Invalid entry, Please enter no more/less then a cord pair (A2 B2)")

                if ((valid_cord[0][0].isalpha() and valid_cord[0][0] <= board.max_row) and (valid_cord[1][0].isalpha() and valid_cord[1][0] <= board.max_row) and 
                (valid_cord[0][1: len(valid_cord[0])].isnumeric() and int(valid_cord[0][1: len(valid_cord[0])]) <= board.max_col) and (valid_cord[1][1: len(valid_cord[1])].isnumeric() and int(valid_cord[1][1: len(valid_cord[1])]) <= board.max_col)):
                    #if valid_cord[0][0] is in the same col as valid_cord[1][0] and +length, -length(up or down max)
                    #return true or false
                    d = board.place_ship_board(valid_cord, temp_ship, board)
                else:
                    raise Exception("ERROR: Invalid entry, Please enter valid cords (height, width) ex. A2 B2")
            except ValueError:
                raise Exception("Invalid entry, please enter an alphanumeric character followed by a maximum of 2 digits (heigth, width) ex. A10 B10")
            except Exception as e:
                print(e)
        
#Player class
class PlayerClass:
    def __init__(self):
        self
    
    #initiates player name
    def player_name_init(self):
        player_name = input("\nWelcome to Battleship! Please enter your name: ")
        self.name = player_name

    #initiates player board
    def player_board_init(self):
        if(hasattr(self, "computer_player")):
            self.computer_player.board = self.board
        else:
            board_type = input("\nPlease enter the type of Battleship map\n\n\t1: Default\t2:Custom\n\nType: ")
            if(board_type == '1'):
                board_file = BoardClass("board.txt")
                board_file.read_board_file()
                #board_file.clean_board_file()
                board_file.create_game_board()
                board_file.create_game_attack_board()
                self.board = board_file
            elif(board_type == '2'):
                board = input("Please enter custom map file(in this directory): ")
                board_file = BoardClass(board)
                board_file.read_board_file()
                #board_file.clean_board_file()
                board_file.create_game_board()
                board_file.create_game_attack_board()
                self.board = board_file
            else:
                raise Exception("Please enter only 1 or 2 as your answer!")
            print("\n")

    #initiates default ship list
    def player_default_ship_init(self):
        ship_list = []
        ship_carrier = ShipClass(5, "Aircraft Carrier", "A")
        ship_battle = ShipClass(4, "Battleship", "B")
        ship_destroyer = ShipClass(3, "Destroyer", "D")
        ship_submarine = ShipClass(3, "Submarine", "S")
        ship_patrol = ShipClass(2, "Patrol Boat", "P")
        ship_list.append(ship_carrier)
        ship_list.append(ship_battle)
        ship_list.append(ship_destroyer)
        ship_list.append(ship_submarine)
        ship_list.append(ship_patrol)
        self.default_ship_list = ship_list

    def player_computer_init(self, computer_player):
        self.computer_player = computer_player

    def print_default_ship_list(self):
        if(self.default_ship_list):
            i = 1
            print("name:\t   " + self.default_ship_list[0].ship_type, end='')
            while(i < len(self.default_ship_list)):
                print("\t" + self.default_ship_list[i].ship_type, end='')
                i +=1
            print()
            i = 1
            print("ref:\t        " + self.default_ship_list[0].ship_char, end='')
            while(i < len(self.default_ship_list)):
                print("\t        " + self.default_ship_list[i].ship_char, end='')
                i+=1
            print()
            i = 1
            print("size:\t        " + str(self.default_ship_list[0].ship_length), end='')
            while(i < len(self.default_ship_list)):
                print("\t        " + str(self.default_ship_list[i].ship_length), end='')
                i+=1
            print()
        else:
            return

    #Searches default ship piece
    def default_ship_name_locate(self):
        state = True
        boat_found = False
        while(state):
            #if player, ask for input
            if(hasattr(self, "computer_player")):
                print("COMPUTER DECISION")
                index = random.choice(self.default_ship_list)
                char_input = self.default_ship_list[index].ship_char
                print(char_input)
            else:
                # else computer, makes choice
                char_input = input("\nBoat Placement\nSelect a boat to place (Ref): ")
                if(len(char_input) != 1):
                        raise Exception("Invalid entry, please review ship ref and try again")
            try:
                i = 0
                for boat in self.default_ship_list:
                    if(boat.ship_char == char_input):
                        boat_found = True
                        print(boat.ship_type + " ship located")
                        boat.ship_cord_validate(boat, self.board)
                        #appends boat to new boat array
                        self.board.boats_placed.append(boat)
                        self.default_ship_list.pop(i)
                        self.print_default_ship_list()
                        state = False
                        break
                    else:
                        i+=1
                        continue
                if (not boat_found):
                        raise Exception("Invalid entry, please review ship ref and try again")
            except ValueError:
                raise Exception("Invalid entry, please review ship ref and try again")
            except Exception as e:
                print(e) 

        #boat placement
    def boat_placement(self):
        # place all 5 default boats
        while(len(self.board.boats_placed) < 5):
            print("BOATS BEING PLACED")
            self.default_ship_name_locate()
        print("All boats have been placed!")
    
    def ship_char_locate(self, boat_char):
        print(self.default_ship_list)
        for i in range(len(self.board.boats_placed)):
            if(self.board.boats_placed[i].ship_char == boat_char):
                return(i)

# Battleship game class
class BattleshipGameClass:
    # define players array
    def __init__(self):
        self.player_list = []
        self.turn_count = 0
    
    def player_setup(self):
        active_player = PlayerClass()
        state = False
        while(not state):    
            active_player.player_name_init()
            try:
                if(len(self.player_list) > 0):
                    for player in self.player_list:
                        if (player.name == active_player.name):
                            print("\nPlayer found! Welcome back, " + player.name)
                            active_player = player
                            state = True
                            break
                else:
                    self.player_list.append(active_player)
                    print("\nThis is a new user, welcome " + active_player.name + "!")
                    state = True
            except NameError:
                raise Exception("\nThere was an error, please try again")

        active_player.player_board_init()
        active_player.player_default_ship_init()
        self.active_player = active_player
    
    def computer_setup(self):
        #creates new player object
        computer_player = PlayerClass()
        #initates player_computer on player class
        self.active_player.player_computer_init(computer_player)
        #assigns board to player_computer
        self.active_player.player_board_init()
        #assign default ships to player_computer
        self.active_player.computer_player.player_default_ship_init()
        #adjust boat placement with predefined values for placement - later implement AI
        self.active_player.computer_player.boat_placement()

    #game actions
    def game_start(self):
        print(" _           _   _   _           _     _       \n" +
        "| |         | | | | | |         | |   (_)      \n" +
        "| |__   __ _| |_| |_| | ___  ___| |__  _ _ __  \n" +
        "|  _ \ / _  | __| __| |/ _ \/ __|  _ \| |  _ \ \n" +
        "| |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |\n" +
        "|_.__/ \__,_|\__|\__|_|\___||___/_| |_|_|  __/ \n" +
        "                                        | |    \n" +
        "                                        |_|   ")
        # player creation
        self.player_setup()
        #create computer/AI(basic ai for now) or another player
        self.active_player.board.print_board_file()
        self.active_player.print_default_ship_list()
        # player ship placement
        self.active_player.boat_placement()
        self.computer_setup()
        #While(not game_win or game_end)
        #While game win or game end doesnt exist continue playing
        #player turn
        self.game_turn_start(self.active_player, self.turn_count)
        #print board data
        #computer turn
        self.game_turn_start(self.active_player.computer_player, self.turn_count)
        #print board data
        self.game_end()

    def game_end(self):
        print("game has ended!")

    #CHANGE FOR MULTI-PLAYER FORMAT
    def game_turn_start(self, player, turn_count):
        #while ships are on board
        state = True
        while(state):
            #get user coord guess for attack action
            valid_cord = []
            game_board = player.board.game_board
            game_attack_board = player.board.game_attack_board

            player.board.print_board_data(game_attack_board)
            str_split = input("\n\nPlease enter an attack coordinate\n\n coordinate: ")
            try:
                for i in str_split.strip().split(' '):
                    valid_cord.append(i)
                if(len(valid_cord) != 1):
                    raise Exception("\nERROR: Please enter only a single coordinate")
                #validate user coord
                if ((valid_cord[0][0].isalpha() and valid_cord[0][0] <= player.board.max_row) and 
                    (valid_cord[0][1: len(valid_cord[0])].isnumeric() and int(valid_cord[0][1: len(valid_cord[0])]) <= player.board.max_col)):
                        y = int(abs((ord(valid_cord[0][0]) - ord('@')) * 2) + 3)
                        x = int(valid_cord[0][1: len(valid_cord[0])]) * 2
                        # check if spot has been guessed already, if the current point is a boat, check if is hit or miss
                        if(game_board[x][y - 1] != -1 and game_attack_board[x][y - 1] == -1):
                            #boat locate for boat search to increase hit count
                            boat_found = player.ship_char_locate(game_board[x][y - 1])
                            #prints hit action
                            print("\n" + player.board.boats_placed[boat_found].ship_type + " has been hit!\n")
                            #boat hit action
                            game_attack_board[x][y - 1] = game_board[x][y - 1]
                            #increase ship_hit count
                            player.board.boats_placed[boat_found].ship_hit_count += 1
                            #check if the current hit count matches the length of boat; boat sunk
                            if(player.board.boats_placed[boat_found].ship_hit_count == 
                                player.board.boats_placed[boat_found].ship_length):
                                print("Ship sunk!")
                                #ships_sunk += 1
                            #end of turn
                            state = False
                        elif(game_board[x][y - 1] != -1 and game_attack_board[x][y - 1] != -1):
                            print("\nSpot has already been guessed, please choose another coordinate\n")
                        else:
                            print("\n" + str(valid_cord[0][0: len(valid_cord[0])]) + " was a miss!\n")
                            game_attack_board[x][y - 1] = '*'
                            #end of turn
                            state = False
                        
                else:
                    raise Exception("ERROR: Please enter a valid attack point")
            except ValueError:
                raise Exception("\nThere was an error, please try again")
            except Exception as e:
                print(e) 

    def game_set_winner(self):
        print("winner is ")
        return