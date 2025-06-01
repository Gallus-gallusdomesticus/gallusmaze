from windows import *
from cell import Cell

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

    win.wait_for_close()


if __name__ == "__main__": 
    main()
        