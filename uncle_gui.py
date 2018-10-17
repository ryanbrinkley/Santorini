
import tkinter as tk
from tkinter import *
from Game import *
#BIGJUICE
HIGHLIGHT_COLOR = 'red'
PLAYER_COLORS = {'P1': 'deep sky blue', 'P2': 'RoyalBlue3'}
TILE_COLORS = ['SpringGreen4', 'SpringGreen3']
TILE_OFFSET = 50
TILE_SIZE = 100

class GUI:
    '''
    Initializes 5x5 grid in TKinter. Needs to be given player locations
    and valid movement spaces for those characters
    '''
    def __init__(self,number_player1_workers=0,number_player2_workers=0):
        self.tile_grid = [0 for i in range(25)] 
        self.current_player_locations = []
        self.game = Game()
        self.stage = self.game.stage
        self.moved_from_tile = 0
        self.number_player2_workers = number_player2_workers
        self.number_player1_workers = number_player1_workers
        self.total_workers = number_player1_workers + number_player2_workers
        self.initial_placement = True
        self.initial_placement_p1 = number_player1_workers
        self.initial_placement_p2 = number_player2_workers
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=600, height=600, borderwidth=0, highlightthickness=0, bg="black")    
        self.init_tiles()
        self.root.mainloop()
#    def enter_tile(self,event):
#        if self.canvas.find_withtag(CURRENT):
#            self.canvas.itemconfig(CURRENT, fill="blue")          
#    def leave_tile(self,event):
#        if self.canvas.find_withtag(CURRENT):
#            self.canvas.itemconfig(CURRENT, fill="SpringGreen3")     
    def click_tile(self,event):
        if self.canvas.find_withtag(CURRENT): 
            tile_clicked = event.widget.find_closest(event.x,event.y)[0] - 1
            self.stage = self.game.get_stage()
            valid_tiles = self.game.valid_spaces(tile_clicked)
            print(tile_clicked)
            print(self.game.stage)
            print(self.game.currPlayer)
            if self.stage == 'PLACE':
                if tile_clicked in self.game.valid_spaces(tile_clicked):
                        if self.initial_placement_p1 > 0:
                                self.canvas.itemconfig(self.tile_grid[tile_clicked], fill=PLAYER_COLORS['P1'])
                                self.initial_placement_p1 -= 1
                        elif self.initial_placement_p2 > 0:
                                self.canvas.itemconfig(self.tile_grid[tile_clicked], fill=PLAYER_COLORS['P2'])
                                self.initial_placement_p2 -= 1
                        self.game.place_workers(tile_clicked)
            elif self.stage=='SELECT':
                for tile in valid_tiles:
                    self.canvas.itemconfig(self.tile_grid[tile], fill=HIGHLIGHT_COLOR)
                    self.moved_from_tile = tile_clicked 
            elif self.stage=='MOVE': 
               if tile_clicked in valid_tiles:
                    self.canvas.itemconfig(self.tile_grid[tile_clicked], fill='yellow')
                    self.canvas.itemconfig(self.tile_grid[tile_clicked], fill=TILE_COLORS[0])
                    
            elif self.stage=='BUILD':
                if tile_clicked in valid_tiles:
                    self.canvas.itemconfig(self.tile_grid[tile_clicked], fill='blue')
                    

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
        self.root.wm_title("Santoroni")
if __name__ == '__main__':
    gui = GUI(2,2)
