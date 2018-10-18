import tkinter as tk
from tkinter import *
from Game import *

HIGHLIGHT_COLOR = ['red', 'yellow']
PLAYER_COLORS = {'P1': 'deep sky blue', 'P2': 'RoyalBlue3'}
BUILDING_COLORS = ['purple1', 'purple3', 'purple4', 'black']
TILE_COLORS = ['SpringGreen4', 'SpringGreen3']
TILE_OFFSET = 50
TILE_SIZE = 100

class GUI:
    '''
    Initializes 5x5 grid in TKinter. Needs to be given player locations
    and valid movement spaces for those characters
    '''
    def __init__(self):
        self.tile_grid = [0 for i in range(25)] 
        self.current_player_locations = []
        self.game = Game()
        self.stage = self.game.stage
        self.moved_from_tile = 0
        self.number_player1_workers = self.game.player1.numWorkers
        self.number_player2_workers = self.game.player2.numWorkers
        self.total_workers = self.number_player1_workers + self.number_player2_workers
        self.initial_placement = True
        self.initial_placement_p1 = self.number_player1_workers
        self.initial_placement_p2 = self.number_player2_workers
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

            if self.stage == "PLACE" or self.stage == "SELECT":
                self.valid_tiles = self.game.valid_spaces(tile_clicked)

            print(tile_clicked)
            # print("Stage: " + self.game.stage)
            # print("Players Turn: " + str(self.game.activePlayer))
            # print(self.valid_tiles)

            if tile_clicked in self.valid_tiles:
                if self.stage == 'PLACE':
                    if self.initial_placement_p1 > 0:
                            self.canvas.itemconfig(self.tile_grid[tile_clicked], fill=PLAYER_COLORS['P1'])
                            self.initial_placement_p1 -= 1
                    elif self.initial_placement_p2 > 0:
                            self.canvas.itemconfig(self.tile_grid[tile_clicked], fill=PLAYER_COLORS['P2'])
                            self.initial_placement_p2 -= 1
                    self.game.place_workers(tile_clicked)

                elif self.stage=='SELECT':
                    self.game.select_worker(tile_clicked)
                    self.valid_tiles = self.game.valid_spaces(tile_clicked)
                    self.movable_tiles = set()
                    for tile in self.valid_tiles:
                        self.movable_tiles.add(tile)
                        self.canvas.itemconfig(self.tile_grid[tile], fill=HIGHLIGHT_COLOR[0])
                        self.moved_from_tile = tile_clicked

                elif self.stage=='MOVE':
                    self.game.move_worker(tile_clicked)
                    self.valid_tiles = self.game.valid_spaces(tile_clicked)

                    if self.game.activePlayer == 1:
                        self.canvas.itemconfig(self.tile_grid[tile_clicked], fill=PLAYER_COLORS['P1'])
                    else:
                        self.canvas.itemconfig(self.tile_grid[tile_clicked], fill=PLAYER_COLORS['P2'])
                    
                    self.movable_tiles.remove(tile_clicked)
                    self.movable_tiles.add(self.moved_from_tile)
                    self.reset_tiles(self.movable_tiles)

                    self.buildable_tiles = set()
                    for tile in self.valid_tiles:
                        self.buildable_tiles.add(tile)
                        self.canvas.itemconfig(self.tile_grid[tile], fill=HIGHLIGHT_COLOR[1])
                        
                elif self.stage=='BUILD':
                    self.game.build(tile_clicked)
                    height = self.game.spaces[tile_clicked].height - 1
                    self.canvas.itemconfig(self.tile_grid[tile_clicked], fill=BUILDING_COLORS[height])  
                    self.buildable_tiles.remove(tile_clicked)
                    self.reset_tiles(self.buildable_tiles)    

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

    def reset_tiles(self, tiles_to_reset):
        for tile in tiles_to_reset:
            height = self.game.spaces[tile].height
            if height > 0:
                self.canvas.itemconfig(self.tile_grid[tile], fill=BUILDING_COLORS[height - 1])
            elif tile % 2 == 0: 
                self.canvas.itemconfig(self.tile_grid[tile], fill=TILE_COLORS[0])
            else:
                self.canvas.itemconfig(self.tile_grid[tile], fill=TILE_COLORS[1])

if __name__ == '__main__':
    gui = GUI()
