import unittest
from unittest.mock import patch, mock_open

from sympy.physics.vector import Point

from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr , Edge , Facet


class TestPolyedr(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """200.0 0.0 0.0 0.0
5 5 8
-1.0 -1.0 0.0
1.0 -1.0 0.0
1.0 1.0 0.0
-1.0 1.0 0.0
0.0 0.0 1.5
4 1 2 3 4
3 1 2 5
3 2 3 5
3 3 4 5
3 4 1 5"""

        cube_data = '''1.0    0.0    0.0    0.0
8       2       8
1.0    2.0     0.0
3.0    2.0     0.0
3.0    -2.0    0.0
1.0    -2.0    0.0
0.0    1.0     -1.0
4.0    1.0     -1.0
4.0    -1.0    -1.0
0.0    -1.0    -1.0
4       1    2    3    4
4       5    6    7    8'''
        fake_file_path1 = 'data/holey_box.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file1:
            self.piro = Polyedr(fake_file_path1)


        fake_file_path2 = 'data/ababa.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=cube_data)) as _file:
            self.cube2 = Polyedr(fake_file_path2)




    def test_num_vertexes(self):
        self.assertEqual(len(self.piro.vertexes), 5)

    def test_num_facets(self):
        self.assertEqual(len(self.piro.facets), 5)

    def test_num_edges(self):
        self.assertEqual(len(self.piro.edges), 16)

    def test_func1(self):
        self.assertEqual(self.piro.calculate(),0)

    def test_func2(self):
        self.assertEqual(self.cube2.calculate(),8)


