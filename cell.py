from windows import Line, Point

class Cell:
    def __init__(self, win):

        self.has_left_wall = True
        self.has_bottom_wall = True
        self.has_right_wall = True
        self.has_top_wall = True

        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win= win
    
    def draw(self, new_x1, new_y1, new_x2, new_y2):
        self.__x1=min(new_x1, new_x2)
        self.__x2=max(new_x1, new_x2)
        self.__y1=max(new_y1, new_y2)
        self.__y2=min(new_y1, new_y2)
        
        if self.has_left_wall:
            po1=Point(self.__x1, self.__y1)
            po2=Point(self.__x1, self.__y2)
            li=Line(po1, po2)
            self.__win.draw_line(li, "Black")
        
        if self.has_bottom_wall:
            po1=Point(self.__x1, self.__y1)
            po2=Point(self.__x2, self.__y1)
            li=Line(po1, po2)
            self.__win.draw_line(li, "Black")
        
        if self.has_right_wall:
            po1=Point(self.__x2, self.__y1)
            po2=Point(self.__x2, self.__y2)
            li=Line(po1, po2)
            self.__win.draw_line(li, "Black")
        
        if self.has_top_wall:
            po1=Point(self.__x1, self.__y2)
            po2=Point(self.__x2, self.__y2)
            li=Line(po1, po2)
            self.__win.draw_line(li, "Black")
