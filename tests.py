import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells1(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._Maze__break_entrance_and_exit()
        i=len(m1._Maze__cells)-1
        j=len(m1._Maze__cells[i])-1
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
        self.assertEqual(
            m1._Maze__cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m1._Maze__cells[i][j].has_bottom_wall,
            False
        )
    def test_maze_create_cells2(self):
        num_cols = 150
        num_rows = 200
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._Maze__break_entrance_and_exit()
        i=len(m1._Maze__cells)-1
        j=len(m1._Maze__cells[i])-1
        
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
        self.assertEqual(
            m1._Maze__cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m1._Maze__cells[i][j].has_bottom_wall,
            False
        )

if __name__ == "__main__":
    unittest.main()