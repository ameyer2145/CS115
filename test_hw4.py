'''
Created on Sep 29, 2018
I pledge my honor that I have abided by the Stevens Honor System
@author: Andrea Meyer
username: ameyer
'''
import unittest
import hw4
class Test(unittest.TestCase):
    def testRow(self):# Replace pass with real test code. Use self.assertEqual.
        self.assertEqual(hw4.pascal_row(7), [1, 7, 21, 35, 35, 21, 7, 1])
        self.assertEqual(hw4.pascal_row(13), [1, 13, 78, 286, 715, 1287, 1716, 1716, 1287, 715, 286, 78, 13, 1])
        self.assertEqual(hw4.pascal_row(2), [1, 2, 1])
        self.assertEqual(hw4.pascal_row(6), [1, 6, 15, 20, 15, 6, 1])
        self.assertEqual(hw4.pascal_row(24), [1, 24, 276, 2024, 10626, 42504, 134596, 346104, 735471, 1307504, 1961256, 2496144, 2704156, 2496144, 1961256, 1307504, 735471, 346104, 134596, 42504, 10626, 2024, 276, 24, 1])
    def test10(self):
        self.assertEqual(hw4.pascal_triangle(11), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1], [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1], [1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1]])
        self.assertEqual(hw4.pascal_triangle(8), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1]])
        self.assertEqual(hw4.pascal_triangle(1), [[1], [1, 1]])
        self.assertEqual(hw4.pascal_triangle(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])
        self.assertEqual(hw4.pascal_triangle(9), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]])
    
if __name__ == "__main__":
    unittest.main()