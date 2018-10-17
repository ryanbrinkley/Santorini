import tkinter as tk
from tkinter import *
HIGHLIGHT_COLOR = 'red'
TILE_COLORS = ['SpringGreen4', 'SpringGreen3']
TILE_OFFSET = 50
TILE_SIZE = 100
def enter_tile(event):
    if canvas.find_withtag(CURRENT):
        canvas.itemconfig(CURRENT, fill="blue")
        
def leave_tile(event):
    if canvas.find_withtag(CURRENT):
        canvas.itemconfig(CURRENT, fill="SpringGreen3") 
def click_tile(event):
    if canvas.find_withtag(CURRENT): #and tile clicked on has your dude on it
        tile_selected = event.widget.find_closest(event.x,event.y)[0] - 1
        valid_tile = set()
        valid_tile.add(event.widget.find_closest(event.x-TILE_SIZE, event.y)[0]-1)
        valid_tile.add(event.widget.find_closest(event.x-TILE_SIZE, event.y+TILE_SIZE)[0]-1)
        valid_tile.add(event.widget.find_closest(event.x-TILE_SIZE, event.y-TILE_SIZE)[0]-1)
        valid_tile.add(event.widget.find_closest(event.x+TILE_SIZE, event.y)[0]-1)
        valid_tile.add(event.widget.find_closest(event.x+TILE_SIZE, event.y+TILE_SIZE)[0]-1)
        valid_tile.add(event.widget.find_closest(event.x+TILE_SIZE, event.y-TILE_SIZE)[0]-1)
        valid_tile.add(event.widget.find_closest(event.x, event.y+TILE_SIZE)[0]-1)
        valid_tile.add(event.widget.find_closest(event.x, event.y-TILE_SIZE)[0]-1)
        if tile_selected in valid_tile:
            valid_tile.remove(tile_selected)
        #if tile is reachable:
        for tile in valid_tile:
            canvas.itemconfig(tile_grid[tile], fill=HIGHLIGHT_COLOR)

        #canvas.itemconfig(CURRENT, fill= HIGHLIGHT_COLOR)
        #canvas.itemconfig(event.widget.find_closest(event.x-TILE_SIZE, event.y), fill = HIGHLIGHT_COLOR)
        #canvas.itemconfig(event.widget.find_closest(event.x-TILE_SIZE, event.y+TILE_SIZE), fill = HIGHLIGHT_COLOR)
        #canvas.itemconfig(event.widget.find_closest(event.x-TILE_SIZE, event.y-TILE_SIZE), fill = HIGHLIGHT_COLOR)
        #canvas.itemconfig(event.widget.find_closest(event.x+TILE_SIZE, event.y), fill = HIGHLIGHT_COLOR)
        #canvas.itemconfig(event.widget.find_closest(event.x+TILE_SIZE, event.y+TILE_SIZE), fill = HIGHLIGHT_COLOR)
        #canvas.itemconfig(event.widget.find_closest(event.x+TILE_SIZE, event.y-TILE_SIZE), fill = HIGHLIGHT_COLOR)
        #canvas.itemconfig(event.widget.find_closest(event.x, event.y+TILE_SIZE), fill = HIGHLIGHT_COLOR)
        #canvas.itemconfig(event.widget.find_closest(event.x, event.y-TILE_SIZE), fill = HIGHLIGHT_COLOR)
        
#tile_grid = [[0 for i in range(5)] for j in range(5)]
tile_grid = [0 for i in range(25)] #going 1d for now i guess (cuz thats how canvas stores em anyway), also realizing i can just append oh well
root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=600, borderwidth=0, highlightthickness=0, bg="black")
canvas.grid()
for c in range(5): #row and column are switched oh well, fix later or never
    for r in range(5):
        tile_tag = ''.join(('r',str(r),'c',str(c)))
        tile_grid[r+5*c] = canvas.create_rectangle(TILE_OFFSET+r*TILE_SIZE,
            TILE_OFFSET+c*TILE_SIZE,
            TILE_OFFSET+TILE_SIZE+r*TILE_SIZE,
            TILE_OFFSET+TILE_SIZE+c*TILE_SIZE,
            fill=TILE_COLORS[(r+c)%2], tags=tile_tag)
        canvas.tag_bind(tile_grid[r+5*c], '<Enter>', enter_tile)
        canvas.tag_bind(tile_grid[r+5*c], '<Leave>', leave_tile)
canvas.bind("<Button-1>", click_tile)
root.wm_title("Santoroni")
root.mainloop()
