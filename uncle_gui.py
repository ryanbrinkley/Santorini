import tkinter as tk
from tkinter import *
HIGHLIGHT_COLOR = 'red'
TILE_COLORS = ['SpringGreen4', 'SpringGreen3']
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
    def __init__(self):
        #tile_grid = [[0 for i in range(5)] for j in range(5)]
        self.tile_grid = [0 for i in range(25)] #going 1d for now i guess (cuz thats how canvas stores em anyway), also realizing i can just append oh well
        self.current_player_locations = []
        # or
        #self.current_player
        #self.player_locations
        self.valid_movement_spaces = []
        self.valid_tile = set()
        self.valid_character_select = False
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=600, height=600, borderwidth=0, highlightthickness=0, bg="black")    
        self.canvas.bind
        self.canvas.grid()
        for row in range(5): #row and column are switched oh well, fix later or never
            for col in range(5):
                tile_tag = ''.join(('row',str(row),'col',str(col)))
                self.tile_grid[col+5*row] = self.canvas.create_rectangle(TILE_OFFSET+col*TILE_SIZE,
                TILE_OFFSET+row*TILE_SIZE,
                TILE_OFFSET+TILE_SIZE+col*TILE_SIZE,
                TILE_OFFSET+TILE_SIZE+row*TILE_SIZE,
                fill=TILE_COLORS[(col+row)%2], tags=tile_tag)
                self.canvas.tag_bind(self.tile_grid[col+5*row], '<Enter>', self.enter_tile)
                self.canvas.tag_bind(self.tile_grid[col+5*row], '<Leave>', self.leave_tile)
        self.canvas.bind("<Button-1>", self.click_tile)
        self.root.wm_title("Santoroni")
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
            print(tile_clicked)
            if not self.valid_character_select:#and if tile clicked on has your dude on it
                self.valid_character_select = True
                self.valid_tile.clear() 
                #self.valid_tile = set()
                self.valid_tile.add(event.widget.find_closest(event.x-TILE_SIZE, event.y)[0]-1)
                self.valid_tile.add(event.widget.find_closest(event.x-TILE_SIZE, event.y+TILE_SIZE)[0]-1)
                self.valid_tile.add(event.widget.find_closest(event.x-TILE_SIZE, event.y-TILE_SIZE)[0]-1)
                self.valid_tile.add(event.widget.find_closest(event.x+TILE_SIZE, event.y)[0]-1)
                self.valid_tile.add(event.widget.find_closest(event.x+TILE_SIZE, event.y+TILE_SIZE)[0]-1)
                self.valid_tile.add(event.widget.find_closest(event.x+TILE_SIZE, event.y-TILE_SIZE)[0]-1)
                self.valid_tile.add(event.widget.find_closest(event.x, event.y+TILE_SIZE)[0]-1)
                self.valid_tile.add(event.widget.find_closest(event.x, event.y-TILE_SIZE)[0]-1)
                if tile_clicked in self.valid_tile:
                    self.valid_tile.remove(tile_clicked)
                #if tile is reachable:
                for tile in self.valid_tile:
                    self.canvas.itemconfig(self.tile_grid[tile], fill=HIGHLIGHT_COLOR) 
            elif self.valid_character_select:
                if tile_clicked in self.valid_tile:
                    self.canvas.itemconfig(self.tile_grid[tile_clicked], fill='yellow')
                self.valid_character_select = False

if __name__ == '__main__':
    gui = GUI()