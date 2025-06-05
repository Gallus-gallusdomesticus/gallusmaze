from windows import *
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
  
    
    cell1 = Cell(win)
    cell1.has_top_wall = False  # This cell won't draw its top wall

    cell2 = Cell(win)
    cell2.has_right_wall = False  # This one misses its right wall

    cell3 = Cell(win)
    cell3.has_left_wall = False
    cell3.has_bottom_wall = False

    cell1.draw(10, 10, 50, 50)
    cell2.draw(60, 10, 100, 50)
    cell3.draw(10, 60, 50, 100)

    cell1.draw_move(cell2, False)
    cell1.draw_move(cell3, True)

    cell2.draw_move(cell3, False)

    win.wait_for_close()

    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze._Maze__break_entrance_and_exit()

    win.wait_for_close()


if __name__ == "__main__": 
    main()
        