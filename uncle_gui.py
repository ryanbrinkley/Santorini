import tkinter as tk
from tkinter import *
#BIGJUICE
HIGHLIGHT_COLOR = 'red'
COLOR_P1 = 'deep sky blue'
COLOR_P2 = 'RoyalBlue3'
TILE_COLORS = ['SpringGreen4', 'SpringGreen3']
#STAGE = ['select','move', 'build']

TILE_OFFSET = 50
TILE_SIZE = 100
def two_D_list_from_one_D(l):
    return [[l[i+5*j] for i in range(5)] for j in range(5)]
def one_D_list_from_two_D(l):
    l_new = []
    for i in range(5):
        for j in range(5):
            l_new.append(l[i][j])
    return l_new

class GUI:
    '''
    Initializes 5x5 grid in TKinter. Needs to be given player locations
    and valid movement spaces for those characters
    '''
    def __init__(self,number_player1_workers=0,number_player2_workers=0):
        #tile_grid = [[0 for i in range(5)] for j in range(5)]
        self.tile_grid = [0 for i in range(25)] #going 1d for now i guess (cuz thats how canvas stores em anyway), also realizing i can just append oh well
        self.current_player_locations = []
        # or
        #self.current_player
        #self.player_locations
        self.number_player2_workers = number_player2_workers
        self.number_player1_workers = number_player1_workers
        self.total_workers = number_player1_workers + number_player2_workers
        self.initial_placement = True
        self.initial_placement_p1 = number_player1_workers
        self.initial_placement_p2 = number_player2_workers
        self.valid_movement_spaces = []
        self.valid_tile = set()
        self.valid_character_select = False
        self.stage = ''
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=600, height=600, borderwidth=0, highlightthickness=0, bg="black")    
        self.init_tiles()
        self.root.mainloop()
    def enter_tile(self,event):
        if self.canvas.find_withtag(CURRENT):
            self.canvas.itemconfig(CURRENT, fill="blue")          
    def leave_tile(self,event):
        if self.canvas.find_withtag(CURRENT):
            self.canvas.itemconfig(CURRENT, fill="SpringGreen3") 
        
    def click_tile(self,event):
        if self.canvas.find_withtag(CURRENT): 
            tile_clicked = event.widget.find_closest(event.x,event.y)[0] - 1
            #BIGJUICYvalid_tiles = valid_spaces(tile_clicked)
            print(tile_clicked)
            if self.STAGE == 'place':
                if self.initial_placement_p1 > 0:
                    #BIGJUICE if (valid placement):
                    self.canvas.itemconfig(self.tile_grid[tile_clicked], fill=COLOR_P1)
                    self.initial_placement_p1 -= 1
                elif self.initial_placement_p2 > 0:
                    #BIGJUICE if (valid placement):
                    self.canvas.itemconfig(self.tile_grid[tile_clicked], fill=COLOR_P2)
                    self.initial_placement_p2 -= 1
                    if self.initial_placement_p2 == 0:
                        self.initial_placement = False
            elif self.STAGE=='select':
                if not self.valid_character_select:#and if tile clicked on has your dude on it
                    self.valid_character_select = True
                    if tile_clicked in self.valid_tile:
                        self.valid_tile.remove(tile_clicked)
                    #if tile is reachable:
                    for tile in self.valid_tile:
                        self.canvas.itemconfig(self.tile_grid[tile], fill=HIGHLIGHT_COLOR) 
                elif self.valid_character_select:
                    if tile_clicked in self.valid_tile:
                        self.canvas.itemconfig(self.tile_grid[tile_clicked], fill='yellow')
                        #print(self.canvas.itemconfig(self.tile_grid[tile_clicked]))
                    self.valid_character_select = False
            elif self.STAGE=='move': 
            elif self.STAGE=='build': 
    def init_tiles(self): #make 5x5 array of tiles and make them clickable
        self.canvas.bind
        self.canvas.grid()
        for row in range(5):
            for col in range(5):
                self.tile_grid[col+5*row] = self.canvas.create_rectangle(TILE_OFFSET+col*TILE_SIZE,
                TILE_OFFSET+row*TILE_SIZE,
                TILE_OFFSET+TILE_SIZE+col*TILE_SIZE,
                TILE_OFFSET+TILE_SIZE+row*TILE_SIZE,
                fill=TILE_COLORS[(col+row)%2],tag='tile')
                #self.canvas.tag_bind(self.tile_grid[col+5*row], '<Enter>', self.enter_tile)
                #self.canvas.tag_bind(self.tile_grid[col+5*row], '<Leave>', self.leave_tile)
        self.canvas.bind("<Button-1>", self.click_tile)
        self.root.wm_title("Santoroni")s
if __name__ == '__main__':
    gui = GUI(2,2)