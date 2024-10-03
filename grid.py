import tkinter as tk


CELL_SIZE = 50
grid_dimension = (4, 4)
current_pos = (0, 0)


def draw_grid(canvas, grid_size):
    rows, cols = grid_size
    for row in range(rows):
        for col in range(cols):
            upper_corner = (row * CELL_SIZE, col * CELL_SIZE)
            lower_right_corner = (row * CELL_SIZE + CELL_SIZE, col * CELL_SIZE + CELL_SIZE)
            canvas.create_rectangle(upper_corner, lower_right_corner, fill='gold')

def draw_player(canvas, position):
    canvas.delete("player")
    x,y = position
    x_pixel= x* CELL_SIZE + CELL_SIZE // 4
    y_pixel = y*CELL_SIZE + CELL_SIZE // 4
    canvas.create_oval(x_pixel , y_pixel, x_pixel + CELL_SIZE //2 , y_pixel + CELL_SIZE// 2 , fill='white', tags='player')


def key_pressed(event):
    global current_pos
    key = event.keysym
    if key== 'w':
        current_pos= (current_pos[0], max(0, current_pos[1]- 1))
    elif key== 's':
        current_pos= (current_pos[0], min(grid_dimension[1]-1 , current_pos[1] + 1))
    elif key== 'a':
            current_pos= (max(0, current_pos[0] -1), current_pos[1])
    elif key== 'd':
           current_pos= (min(grid_dimension[0] -1, current_pos[0]+1), current_pos[1])
    draw_player(canvas,current_pos)
    
app = tk.Tk()
app.geometry('800x600')
app.title('MAZE')

canvas = tk.Canvas(app, width=600, height=400, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)

draw_grid(canvas, grid_dimension)
draw_player(canvas, current_pos)

canvas.focus_set()
app.bind("<KeyPress>", key_pressed) 

app.mainloop()



