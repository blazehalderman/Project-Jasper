import random

# models for game pieces, players, ships, board(s)

#Piece class
class PieceClass:
    def __init__(self, char, rowX, colY, num_colY):
        self.char = char
        self.rowX = rowX
        self.colY = colY
        self.act_rowX = chr(ord('@') + (rowX//2))
        self.act_colY = num_colY

    #CREATE FUNCTION FOR RUNNING ALL FUNCTIONS

#Board class
class BoardClass:
    def __init__(self, file):
        self.file = file
        self.board_data = []
        self.board_pieces = []

    #CREATE FUNCTION FOR RUNNING ALL FUNCTIONS

    #prints current board file
    def print_board_file(self):
        with open(self.file) as f:
            print(f.read() + "\n\n")
        f.closed

    #reads a file and saves data into 2d array
    def read_board_file(self):
        with open(self.file) as f:
            for line in f:
                for i in line.strip().split('\n'):
                    self.board_data.append(i)
        f.closed
    
    #sorts through file 2d array and identifies valid points
    def clean_board_file(self):
        stored_pieces = []
        for row in range(len(self.board_data)):
            num_colY = 0
            for col in range(len(self.board_data[row])):
                if(self.board_data[row][col:col+3] == '| |'):
                    num_colY+=1
                    new_piece = PieceClass(self.board_data[row][col+1], row, col+1, num_colY)
                    stored_pieces.append(new_piece)
    
        for i in stored_pieces:
            print(str(i.act_rowX) + ' ' + str(i.act_colY))
    
    def board_piece_validate(self, valid_cord, board_pieces):
        for i in board_pieces:
            print(i.act_rowX)
            print(i.act_rowY)

#Ship class
class ShipClass:
    def __init__(self, ship_length, ship_type):
        self.ship_length = ship_length
        self.ship_type = ship_type
        self.ship_cord_store = []

    #CREATE FUNCTION FOR RUNNING ALL FUNCTIONS

    #validates coordinates based on proper Battleship Cord syntax
    def ship_cord_validate(self, temp_ship):
        while(True):
            temp = []
            temp_cords = input("Please select placement coordinate range for " + temp_ship.ship_type + 
            ": length - " + str(temp_ship.ship_length) + ":")
            try: 
                for i in temp_cords.strip().split(' '):
                    temp.append(i)
                if(len(temp) != 2):
                    raise Exception("ERROR: Invalid entry, Please enter no more/less then a cord pair (A2 B2)")
                count = 0
                for j in temp:
                    ind = 0
                    for k in j:
                        if(k.isalpha() and ind == 0):
                            ind += 1
                            continue
                        elif(k.isnumeric() and ind <= 2 and ind != 0):
                            ind += 1
                            continue
                        else:
                            raise Exception("ERROR: Invalid entry, Please enter valid cords (height, width) ex. A2 B2")
                    count += 1
                if(count == len(temp)):
                    return temp
            except ValueError:
                raise Exception("Invalid entry, please enter an alphanumeric character followed by a maximum of 2 digits (heigth, width) ex. A10 B10")
            except Exception as e:
                print(e)  
        
#Player class
class PlayerClass:
    def __init__(self):
        self.name = ''
        self.board = []
        self.default_ship_list = []
    
    #initiates player name
    def player_name_init(self):
        player_name = input("Welcome to Battleship! Please enter your name: ")
        self.name = player_name

    #initiates player board
    def player_board_init(self):
        board = input("Please enter the Battleship map you wish to play(must follow specific formats in board.txt): ")
        board_file = BoardClass(board)
        board_file.read_board_file()
        board_file.clean_board_file()
        self.board = board_file

    #initiates default ship list
    def player_default_ship_init(self):
        ship_carrier = ShipClass(5, "Aircraft Carrier")
        ship_battle = ShipClass(4, "Battleship")
        ship_destroyer = ShipClass(3, "Destroyer")
        ship_submarine = ShipClass(3, "Submarine")
        ship_patrol = ShipClass(2, "Patrol Boat")
        self.default_ship_list.append(ship_carrier)
        self.default_ship_list.append(ship_battle)
        self.default_ship_list.append(ship_destroyer)
        self.default_ship_list.append(ship_submarine)
        self.default_ship_list.append(ship_patrol)

    #Searches default ship piece
    def default_ship_name_locate(self):
        temp_storage = input("Please select a ship to place on the board(ship name): ")
        for i in self.default_ship_list:
            if(i.ship_type == temp_storage):
                return (i)

# Battleship game class
class BattleshipGameClass:
    # define players array
    def __init__(self):
        self.player_list = []
    
    def player_setup(self):
        active_player = PlayerClass()
        state = False
        while(not state):    
            active_player.player_name_init()
            try:
                if(len(self.player_list) > 0):
                    for player in self.player_list:
                        if (player.name == active_player.name):
                            print("Player found! Welcome back, " + player.name)
                            active_player = player
                            state = True
                            break
                else:
                    self.player_list.append(active_player)
                    print("This is a new user, welcome " + active_player.name + "!")
                    state = True
            except NameError:
                raise Exception("There was an error, please try again")

        active_player.player_board_init()
        active_player.player_default_ship_init()
        #list boats size stored and types
        for i in active_player.default_ship_list:
            print(i.ship_length)
            print(i.ship_type)
        
        return(active_player)

    #boat placement
    def boat_placement(self, player):
        ship_located = player.default_ship_name_locate()
        print(ship_located)
        print("\n" + ship_located.ship_type + " Located\n")
        cur_board = player.board
        cur_pieces = cur_board.board_pieces
        ship_cord_validated = ship_located.ship_cord_validate(ship_located)
        cur_board.board_piece_validate(ship_cord_validated, cur_pieces)
        print("Boat placement code here")
    
    #game actions
    def game_start(self):
        player = self.player_setup()

        print(player.default_ship_list[0])

        # implement into move functions
        player.board.print_board_file()

        # ship coordinate validate(move to player class function)
        self.boat_placement(player)
        
        print("game is running!")

    def game_end(self):
        print("game has ended!")

    def game_end_turn(self):
        print("turn has ended")

    def game_set_winner(self):
        print("winner is " + self.active_player.name)
        return