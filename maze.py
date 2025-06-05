from time import sleep
from cell import Cell
from windows import Window

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1=x1
        self.y1=y1
        self.num_rows=num_rows
        self.num_cols=num_cols
        self.cell_size_x=cell_size_x
        self.cell_size_y=cell_size_y
        self.__win=win
        self.__cells=[]
        self.__create_cells()

    def __create_cells(self):
        for i in range(self.num_cols):
            self.__cells.append([])
            for j in range(self.num_rows):
                self.__cells[i].append(Cell(self.__win))
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.__draw_cell(i,j)
    
    def __draw_cell(self, i, j):
        draw_coord_x1=self.x1+self.cell_size_x*i
        draw_coord_y1=self.y1+self.cell_size_y*j
        draw_coord_x2=draw_coord_x1+self.cell_size_x
        draw_coord_y2=draw_coord_y1+self.cell_size_y
        
        cell=self.__cells[i][j]

        cell.draw(draw_coord_x1,draw_coord_y1,draw_coord_x2,draw_coord_y2)

        self.__animate()
    
    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        sleep(0.05)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall=False
        i=len(self.__cells)-1
        j=len(self.__cells[i])-1
        self.__cells[i][j].has_bottom_wall=False
        self.__draw_cell(0,0)
        self.__draw_cell(i,j)
        
