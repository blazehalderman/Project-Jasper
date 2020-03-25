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

#Board class
class BoardClass:
    def __init__(self, file):
        self.file = file
        self.board_data = []
        self.board_pieces = []

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

#Ship class
class ShipClass:
    def __init__(self, ship_length, ship_type):
        self.ship_length = ship_length
        self.ship_type = ship_type
        self.ship_cord_store = []

    #validates coordinates based on proper Battleship Cord syntax
    def ship_piece_validate(self, temp_ship, board_pieces):
        while(True):
            temp = []
            temp_cords = input("Please select placement coordinate range for " + temp_ship.ship_type + 
            ": length - " + str(temp_ship.ship_length) + ":")
            try: 
                for i in temp_cords.strip().split(' '):
                    temp.append(i)
                if(len(temp) != 2):
                    raise Exception("ERROR: Invalid entry, Please enter no more/less then a coordinate pair (A2 B2)")
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
                            print("ERROR: Invalid entry, Please enter valid cords (height, width) ex. A2 B2")
                            break
                    else:
                        count += 1
                        continue
                    break
                if(count == len(temp)):
                    return temp
            except ValueError:
                print("Invalid entry, please enter an alphanumeric character followed by a maximum of 2 digits (heigth, width) ex. A10 B10")
            except Exception as e:
                print(e)  
        
#Player class
class PlayerClass:
    def __init__(self, name, board, default_ship_list):
        self.name = name
        self.board = board
        self.default_ship_list = default_ship_list

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
    
    # game actions
    def game_start(self):
        default_ship_array = []
        
        player_name = input("Welcome to Battleship! Please enter your name: ")
        player_board = input("Please enter the Battleship map you wish to play(must follow specific formats in board.txt): ")
        
        #initalizing board, player, default ships
        board_file = BoardClass(player_board)
        board_file.read_board_file()
        board_file.clean_board_file()
        
        ship_carrier = ShipClass(5, "Aircraft Carrier")
        ship_battle = ShipClass(4, "Battleship")
        ship_destroyer = ShipClass(3, "Destroyer")
        ship_submarine = ShipClass(3, "Submarine")
        ship_patrol = ShipClass(2, "Patrol Boat")

        default_ship_array.append(ship_carrier)
        default_ship_array.append(ship_battle)
        default_ship_array.append(ship_destroyer)
        default_ship_array.append(ship_submarine)
        default_ship_array.append(ship_patrol)
        
        # store all information into active player
        active_player = PlayerClass(player_name, board_file, default_ship_array)
        self.player_list.append(active_player)
        
        #list boats size stored and types
        for i in active_player.default_ship_list:
            print(i.ship_length)
            print(i.ship_type)

        return (active_player)
    
    #game data management
    def game_run(self, player):
        ship_located = player.default_ship_name_locate()
        print("\n" + ship_located.ship_type + " Located\n")
        player.board.print_board_file()
        board = player.board
        pieces = board.board_pieces
        ship_located.ship_piece_validate(ship_located, pieces)
        print("game is running!")

    def game_end(self):
        print("game has ended!")

    def game_end_turn(self):
        print("turn has ended")

    def game_set_winner(self):
        print("winner is " + self.active_player.name)
        return