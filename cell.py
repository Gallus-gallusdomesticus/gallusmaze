from windows import Line, Point

class Cell:
    def __init__(self, win=None):

        self.has_left_wall = True
        self.has_bottom_wall = True
        self.has_right_wall = True
        self.has_top_wall = True

        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win= win

        self.visited=False
    
    def _draw_wall(self, po1, po2, has_wall):
        li=Line(po1,po2)
        if self.__win is not None:
            if has_wall:
                self.__win.draw_line(li, "Black")
            else:
                self.__win.draw_line(li, "#d9d9d9")


    def draw(self, new_x1, new_y1, new_x2, new_y2):
        self.__x1=min(new_x1, new_x2)
        self.__x2=max(new_x1, new_x2)
        self.__y1=max(new_y1, new_y2)
        self.__y2=min(new_y1, new_y2)
        
        
        po1=Point(self.__x1, self.__y1)
        po2=Point(self.__x1, self.__y2)
        self._draw_wall(po1,po2,self.has_left_wall)
              
        po1=Point(self.__x1, self.__y1)
        po2=Point(self.__x2, self.__y1)
        self._draw_wall(po1,po2,self.has_bottom_wall)

        po1=Point(self.__x2, self.__y1)
        po2=Point(self.__x2, self.__y2)
        self._draw_wall(po1,po2,self.has_right_wall)  

        po1=Point(self.__x1, self.__y2)
        po2=Point(self.__x2, self.__y2)
        self._draw_wall(po1,po2,self.has_top_wall)
            
                
            

    def get_center_point(self):
        center_x=(self.__x1+self.__x2)/2
        center_y=(self.__y1+self.__y2)/2
        return Point(center_x, center_y)

    def draw_move(self, to_cell, undo=False):
        color="gray"
        if not undo:
            color="red"
        
        po1=self.get_center_point()
        po2=to_cell.get_center_point()

        li=Line(po1, po2)

        if self.__win==None:
            return
        self.__win.draw_line(li, color)

    
        

        

        
