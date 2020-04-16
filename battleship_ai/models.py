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
        self.view_board_data = []
        self.board_pieces = []
        self.boats_placed = []
        self.max_col = 10
        self.max_row = 'J'

    #CREATE FUNCTION FOR RUNNING ALL FUNCTIONS
    #CREATE A NEW BLANK BOARD AND FILL WITH BOATS ETC
        '''board = []
	    for i in range(10):
		    board_row = []
		    for j in range(10):
			    board_row.append(-1)
		    board.append(board_row)'''

    #prints current board file
    def print_board_data(self):
        count = 0
        for i in range(len(self.view_board_data)):
            print(self.view_board_data[i])
            count += 1
        print(count)
        print('\n')

    def print_board_file(self):
        with open(self.file) as f:
            print(f.read() + "\n\n")
        f.closed

    #reads a file and saves data into 2d array
    def read_board_file(self):
        with open(self.file) as f:
            #self.view_board_data = [line.split('\n') for line in f]
            for line in f:
                for j in line.split('\n'):
                    self.view_board_data.append(j)

            for line in f:
                for i in line.strip().split('\n'):
                    self.board_data.append(i)
        f.closed
    
    #sorts through file 2d array and identifies valid points
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
        
        #print cords of board
        #for i in self.board_pieces:
            #print(str(i.rowX) + ' ' + str(i.colY))
    
    #completes validation of coords and places ship on board
    def place_ship_board(self, valid_cord, temp_ship, board):
        #loop through board
        if(valid_cord[0][0] != valid_cord[1][0] and int(valid_cord[0][1: len(valid_cord[1])]) == int(valid_cord[1][1: len(valid_cord[1])])):
            dist = abs(ord(valid_cord[0][0]) - ord(valid_cord[1][0])) + 1
            if(dist == temp_ship.ship_length):
                #if the row specified first is greater, make second head
                if(valid_cord[0][0] > valid_cord[1][0]):
                    head = int(ord(valid_cord[0][1]) - ord('@') + 3)
                else:
                    head = int(ord(valid_cord[0][0]) - ord('@') + 3)
                #placing piece on board
                y = int(valid_cord[0][1: len(valid_cord[0])]) * 4
                print(str(head) + ' ' +str(y))
                #place data for board pieces
                board.print_board_data
                print(head)
                print(y)
                #print(board.view_board_data)
                board.view_board_data[y][head]
                print(board.view_board_data[y])
                #for y in range(dist):
                    #print(board.view_board_data[head + x][y])
                    #board.board_pieces[head].char = temp_ship.ship_char
                    #print(board.board_pieces[head].char)
                    
                print("ship fits")
                return(False)
            else:
                raise Exception("ERROR: Invalid entry, (" + valid_cord[0][0] + ", " + valid_cord[0][1: len(valid_cord[1])] + "), " + 
                "(" + valid_cord[1][0] + ", " + valid_cord[1][1: len(valid_cord[1])] + ") row does not match")
        else:
            if(int(valid_cord[0][1: len(valid_cord[0])]) >= 10 or int(valid_cord[1][1 : len(valid_cord[1])]) >= 10):
                dist = abs(int(valid_cord[0][1: len(valid_cord[0])]) - int(valid_cord[1][1 : len(valid_cord[1])])) + 1
            else:
                dist = abs(int(valid_cord[0][1]) - int(valid_cord[1][1])) + 1
                print(dist)
            if(dist == temp_ship.ship_length):
                
                print("ship fits")
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

    #validates syntax of coordinates
    def ship_cord_validate(self, temp_ship, board):
        d = True
        while(d):
            valid_cord = []
            temp_cords = input("\nPlease select coordinate range for - \n\n" + temp_ship.ship_type + 
            "\nsize: " + str(temp_ship.ship_length) + "\n\ncoordinates:")
            try: 
                for i in temp_cords.strip().split(' '):
                        valid_cord.append(i)              
                if(len(valid_cord) != 2):
                    raise Exception("ERROR: Invalid entry, Please enter no more/less then a cord pair (A2 B2)")

                if ((valid_cord[0][0].isalpha() and valid_cord[0][0] <= board.max_row) and (valid_cord[1][0].isalpha() and valid_cord[1][0] <= board.max_row) and 
                (valid_cord[1][1: len(valid_cord[1])].isnumeric() and int(valid_cord[1][1: len(valid_cord[1])]) <= board.max_col) and (valid_cord[1][1: len(valid_cord[1])].isnumeric() and int(valid_cord[1][1: len(valid_cord[1])]) <= board.max_col)):
                    #if valid_cord[0][0] is in the same col as valid_cord[1][0] and +length, -length(up or down max)
                    #return true or false
                    print("HERE")
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
        board_type = input("\nPlease enter the type of Battleship map\n\n\t1: Default\t2:Custom\n\nType: ")
        if(board_type == '1'):
            board_file = BoardClass("board.txt")
            board_file.read_board_file()
            board_file.clean_board_file()
            self.board = board_file
        elif(board_type == '2'):
            board = input("Please enter custom map file(in this directory): ")
            board_file = BoardClass(board)
            board_file.read_board_file()
            board_file.clean_board_file()
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

    #Searches default ship piece
    def default_ship_name_locate(self):
        state = True
        boat_found = False
        while(state):
            temp_input = input("\nBoat Placement\nSelect a boat to place (Ref): ")
            try:
                if(len(temp_input) != 1):
                    raise Exception("Invalid entry, please review ship ref and try again")
                else:
                    for boat in self.default_ship_list:
                        if(boat.ship_char == temp_input):
                            boat_found = True
                            print(boat.ship_type + " ship located")
                            boat.ship_cord_validate(boat, self.board)
                            #appends boat to new boat array
                            self.board.boats_placed.append(boat)
                            state = False
                            break
                        if (not boat_found):
                            raise Exception("Invalid entry, please review ship ref and try again")
            except ValueError:
                raise Exception("Invalid entry, please review ship ref and try again")
            except Exception as e:
                print(e) 

        #boat placement
    def boat_placement(self):
        # place all 5 default boats
        while(len(self.board.boats_placed) != 5):
            self.default_ship_name_locate()
        return

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
        #list boats size stored and types
        #for i in active_player.default_ship_list:
            #print(i.ship_length)
            #print(i.ship_type)
        
        return(active_player)
    
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
        player = self.player_setup()

        # implement into move functions
        player.board.print_board_file()
        print("\tAircraft Carrier\tBattleship\tDestroyer\tSubmarine\tPatrol Boat\n" +
        "ref:\t       A\t\t    B\t\t    D\t\t    S\t\t     P\n" +
        "size:\t       5\t\t    4\t\t    4\t\t    3\t\t     2\n" + 
        "piece:\t     <000>\t\t  <00>\t\t  <00>\t\t   <0>\t\t    <>\n")
        # ship coordinate validate(move to player class function)
        player.boat_placement()
        
        print("game is running!")

    def game_end(self):
        print("game has ended!")

    def game_end_turn(self):
        print("turn has ended")

    def game_set_winner(self):
        print("winner is ")
        return