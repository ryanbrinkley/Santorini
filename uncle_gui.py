import tkinter as tk
from tkinter import *
from Game import *
from Character import pos_to_coord

HIGHLIGHT_COLOR = 'gray25' # ['red', 'yellow']
PLAYER_COLORS = {'P1': 'deep sky blue', 'P2': 'RoyalBlue3'}
BUILDING_COLORS = ['purple1', 'purple3', 'purple4', 'gray15']
TILE_COLORS = ['SpringGreen4', 'SpringGreen3']
TILE_OFFSET = 50
TILE_SIZE = 80
TILE_SIZE_HALF = 50
BUILDING_HEIGHT = 20

class GUI:
    '''
    LMBO
    '''
    def __init__(self):
        self.tile_grid = [0 for i in range(25)]
        self.building_sides = [[0 for j in range(6)]for i in range(25)]
        self.game = Game()
        self.stage = self.game.stage
        self.moved_from_tile = 0
        self.player_list = []
        self.number_player1_workers = self.game.player1.numWorkers
        self.number_player2_workers = self.game.player2.numWorkers
        self.total_workers = self.number_player1_workers + self.number_player2_workers
        self.initial_placement_p1 = self.number_player1_workers
        self.initial_placement_p2 = self.number_player2_workers
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=800, height=600, borderwidth=0, highlightthickness=0, bg="black")    
        self.init_tiles()
        self.transform_to_isometric()
        self.root.mainloop()
  
    def click_tile(self, event):
        if self.canvas.find_withtag(CURRENT):
            clicked = event.widget.find_closest(event.x,event.y)
            tile_clicked = clicked[0] - 1
            if 'worker' in self.canvas.gettags(clicked):
                tile_clicked = self.player_list[tile_clicked-25]['current_tile']
            self.stage = self.game.stage
            print(tile_clicked)
            if self.stage == "PLACE" or self.stage == "SELECT":
                self.valid_tiles = self.game.valid_spaces(tile_clicked)
            if tile_clicked in self.valid_tiles:
                if self.stage == 'PLACE':
                    self.game.place_workers(tile_clicked)
                    tile_coords = self.canvas.coords(self.tile_grid[tile_clicked])
                    del tile_coords[6:8]
                    del tile_coords[2:4]
                    tile_coords[0] = tile_coords[0] - 30
                    tile_coords[1] = tile_coords[1] - 20
                    tile_coords[2] = tile_coords[2] + 30
                    tile_coords[3] = tile_coords[3] - 20
                    if self.initial_placement_p1 > 0:
                            self.player_list.append({'player_number': 1,'current_tile': tile_clicked,
                                'canvas_object': self.canvas.create_oval(*tile_coords,fill=PLAYER_COLORS['P1'],tags='worker')})
                            self.initial_placement_p1 -= 1
                    elif self.initial_placement_p2 > 0:
                            self.player_list.append({'player_number': 2,'current_tile': tile_clicked,
                                'canvas_object': self.canvas.create_oval(*tile_coords,fill=PLAYER_COLORS['P2'],tags='worker')})
                            self.initial_placement_p2 -= 1

                elif self.stage=='SELECT':
                    self.game.select_worker(tile_clicked)
                    self.valid_tiles = self.game.valid_spaces(tile_clicked)
                    self.moved_from_tile = tile_clicked
                    self.set_highlighted_positions()
                elif self.stage=='MOVE':
                    self.game.move_worker(tile_clicked)
                    self.valid_tiles = self.game.valid_spaces(tile_clicked)
                    # Reset the tiles to normal state
                    self.highlighted_tiles.remove(tile_clicked)
                    self.highlighted_tiles.add(self.moved_from_tile)
                    self.reset_tiles(self.highlighted_tiles)
                    self.canvas.itemconfig(self.tile_grid[tile_clicked], stipple='')

                    self.moved_from_tile = tile_clicked
                    self.set_player_positions()
                    self.set_highlighted_positions()
                    self.order()

                elif self.stage=='BUILD':
                    self.game.build(tile_clicked)  
                    self.reset_tiles(self.highlighted_tiles)
                    self.building_tile(tile_clicked)
                    self.order()

    def init_tiles(self): #make 5x5 array of tiles and make them clickable
        self.canvas.bind
        self.canvas.grid()
        for row in range(5):
            for col in range(5):
                self.tile_grid[col+5*row] = self.canvas.create_polygon(TILE_OFFSET+col*TILE_SIZE,TILE_OFFSET+row*TILE_SIZE, #POINT 1
                    TILE_OFFSET+TILE_SIZE+col*TILE_SIZE, TILE_OFFSET+row*TILE_SIZE, #POINT 2
                    TILE_OFFSET+TILE_SIZE+col*TILE_SIZE, TILE_OFFSET+TILE_SIZE+row*TILE_SIZE, #POINT 3
                    TILE_OFFSET+col*TILE_SIZE, TILE_OFFSET+TILE_SIZE+row*TILE_SIZE, #POINT 4
                    fill=TILE_COLORS[(col+row)%2],tags='tile',outline='black')
        self.canvas.bind("<Button-1>", self.click_tile)
        self.root.wm_title("Santoroni")

    # Set all tiles to appropriate player colors
    # had to make this due to powers like switching player positions
    def set_player_positions(self):
        p1_workers, p2_workers = self.game.get_player_positions()
        for index, position in enumerate(p1_workers):
            x = self.canvas.coords(self.tile_grid[position])
            del x[6:8]
            del x[2:4]
            x[0] = x[0] - 30
            x[1] = x[1] - 20
            x[2] = x[2] + 30
            x[3] = x[3] - 20
            self.canvas.coords(self.player_list[index]['canvas_object'],*x)
            self.player_list[index]['current_tile'] = position
        for index,position in enumerate(p2_workers):
            x = self.canvas.coords(self.tile_grid[position])
            del x[6:8]
            del x[2:4]
            x[0] = x[0] - 30
            x[1] = x[1] - 20
            x[2] = x[2] + 30
            x[3] = x[3] - 20
            self.canvas.coords(self.player_list[index+self.number_player1_workers]['canvas_object'],*x)
            self.player_list[index+self.number_player1_workers]['current_tile'] = position
    # highlight tiles with stipple, need better highlight method but best I could do 
    # for now
    def set_highlighted_positions(self):
        self.highlighted_tiles = set()
        for tile in self.valid_tiles:
            self.highlighted_tiles.add(tile)
            self.canvas.itemconfig(self.tile_grid[tile], stipple=HIGHLIGHT_COLOR)
    def transform_to_isometric(self):
        for tile in self.tile_grid:
            current = self.canvas.coords(tile)
            new_coords = []
            for i in range(0,8,2):
                new_coords.append(current[i] - current[i+1] + 400)
                new_coords.append((current[i] + current[i+1])/2+100)
            self.canvas.coords(tile,*new_coords)     

    # Reset tiles passed to function to default board colors / building colors
    def reset_tiles(self, tiles_to_reset):
        for tile in tiles_to_reset:
            self.canvas.itemconfig(self.tile_grid[tile], stipple='')
            height = self.game.spaces[tile].height
            if height > 0:
                self.canvas.itemconfig(self.tile_grid[tile], fill='white smoke')
            elif tile % 2 == 0: 
                self.canvas.itemconfig(self.tile_grid[tile], fill=TILE_COLORS[0])
            else:
                self.canvas.itemconfig(self.tile_grid[tile], fill=TILE_COLORS[1])
    def building_tile(self,tile):
        x = self.canvas.coords(self.tile_grid[tile])
        height = self.game.spaces[tile].height
        if height != 4: #not a dome
            for i in range(1,len(x),2):
                x[i] -= BUILDING_HEIGHT
            self.canvas.coords(self.tile_grid[tile],*x)
            for i in range(1,len(x),2):
                x[i] += BUILDING_HEIGHT
            self.canvas.itemconfig(self.tile_grid[tile],fill='white smoke')
            self.canvas.itemconfig(self.tile_grid[tile],tags='building')
            y = self.canvas.coords(self.tile_grid[tile])
            right_side = [y[2],y[3],x[2],x[3],x[4],x[5],y[4],y[5]]
            left_side = [y[4],y[5],x[4],x[5],x[6],x[7],y[6],y[7]]
            self.building_sides[tile][(height-1)*2] = self.canvas.create_polygon(*right_side,fill='gainsboro',outline='black',tags='building')
            self.building_sides[tile][(height-1)*2+1] = self.canvas.create_polygon(*left_side,fill='snow',outline='black',tags ='building')
        elif height == 4:
            pass #make a dome, figure out later lawl
    def order(self):
        for tile in range(25):
            height = self.game.spaces[tile].height
            self.canvas.tag_raise(self.tile_grid[tile])
            for i in range(2*height):
                self.canvas.tag_raise(self.building_sides[tile][i])
            for player in self.player_list:
                if player['current_tile']==tile:
                    self.canvas.tag_raise(player['canvas_object'])
if __name__ == '__main__':
    gui = GUI()
