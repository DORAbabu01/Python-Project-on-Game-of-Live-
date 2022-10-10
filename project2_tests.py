# import module that defines unit-testing framework
import unittest

# import module project2.py containing functions to test
import project2

class Project2Test(unittest.TestCase):

    def test_create_grid_from_file_1(self):
        grid = project2.create_grid_from_file('beacon.txt')
        expected = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0]]
        self.assertEqual(grid,expected)

    def test_create_grid_from_file_2(self):
        grid = project2.create_grid_from_file('blinker.txt')
        expected = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(grid,expected)

    def test_create_grid_from_file_3(self):
        grid = project2.create_grid_from_file('glider.txt')
        expected = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(grid,expected)

    def test_create_grid_from_file_4(self):
        grid = project2.create_grid_from_file('toad.txt')
        expected = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        self.assertEqual(grid,expected)

    def test_create_grid_from_file_5(self):
        grid = project2.create_grid_from_file('tub.txt')
        expected = [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(grid,expected)

    def test_save_grid_to_file_1(self):
        grid = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0]]
        project2.save_grid_to_file('saved.txt', grid)
        file = open('saved.txt')
        data = file.read().strip()
        file.close()
        expected = '6 6 0 0 0 0 0 0 0 1 1 0 0 0 0 1 1 0 0 0 0 0 0 1 1 0 0 0 0 1 1 0 0 0 0 0 0 0'
        self.assertEqual(data,expected)

    def test_save_grid_to_file_2(self):
        grid = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
        project2.save_grid_to_file('saved.txt', grid)
        file = open('saved.txt')
        data = file.read().strip()
        file.close()
        expected = '5 5 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0'
        self.assertEqual(data,expected)

    def test_save_grid_to_file_3(self):
        grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        project2.save_grid_to_file('saved.txt', grid)
        file = open('saved.txt')
        data = file.read().strip()
        file.close()
        expected = '9 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'
        self.assertEqual(data,expected)

    def test_save_grid_to_file_4(self):
        grid = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        project2.save_grid_to_file('saved.txt', grid)
        file = open('saved.txt')
        data = file.read().strip()
        file.close()
        expected = '6 6 0 0 0 0 0 0 0 1 1 1 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'
        self.assertEqual(data,expected)

    def test_save_grid_to_file_5(self):
        grid = [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
        project2.save_grid_to_file('saved.txt', grid)
        file = open('saved.txt')
        data = file.read().strip()
        file.close()
        expected = '5 5 0 0 0 0 0 0 1 0 0 0 1 0 1 0 0 0 1 0 0 0 0 0 0 0 0'
        self.assertEqual(data,expected)

    def test_grid_as_string_1(self):
        grid = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0]]
        actual = project2.grid_as_string(grid)
        expected = '. . . . . .\n. X X . . .\n. X X . . .\n. . . X X .\n. . . X X .\n. . . . . .'
        self.assertEqual(actual,expected)

    def test_grid_as_string_2(self):
        grid = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
        actual = project2.grid_as_string(grid)
        expected = '. . . . .\n. . X . .\n. . X . .\n. . X . .\n. . . . .'
        self.assertEqual(actual,expected)

    def test_grid_as_string_3(self):
        grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        actual = project2.grid_as_string(grid)
        expected = '. . . . . . . . .\n. . . . . X . . .\n. . . X . X . . .\n. . . . X X . . .\n. . . . . . . . .\n. . . . . . . . .\n. . . . . . . . .\n. . . . . . . . .\n. . . . . . . . .'
        self.assertEqual(actual,expected)

    def test_grid_as_string_4(self):
        grid = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        actual = project2.grid_as_string(grid)
        expected = '. . . . . .\n. X X X . .\nX X X . . .\n. . . . . .\n. . . . . .\n. . . . . .'
        self.assertEqual(actual,expected)

    def test_grid_as_string_5(self):
        grid = [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
        actual = project2.grid_as_string(grid)
        expected = '. . . . .\n. X . . .\nX . X . .\n. X . . .\n. . . . .'
        self.assertEqual(actual,expected)

    def test_copy_grid_1(self):
        grid = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0]]
        copy = project2.copy_grid(grid)
        # check if grid and copy have same values
        self.assertEqual(grid,copy)
        # check copy is not a shallow copy of grid
        for i in range(len(grid)):
            self.assertFalse(grid[i] is copy[i])

    def test_copy_grid_2(self):
        grid = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
        copy = project2.copy_grid(grid)
        # check if grid and copy have same values
        self.assertEqual(grid,copy)
        # check copy is not a shallow copy of grid
        for i in range(len(grid)):
            self.assertFalse(grid[i] is copy[i])

    def test_copy_grid_3(self):
        grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        copy = project2.copy_grid(grid)
        # check if grid and copy have same values
        self.assertEqual(grid,copy)
        # check copy is not a shallow copy of grid
        for i in range(len(grid)):
            self.assertFalse(grid[i] is copy[i])

    def test_copy_grid_4(self):
        grid = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        copy = project2.copy_grid(grid)
        # check if grid and copy have same values
        self.assertEqual(grid,copy)
        # check copy is not a shallow copy of grid
        for i in range(len(grid)):
            self.assertFalse(grid[i] is copy[i])

    def test_copy_grid_5(self):
        grid = [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
        copy = project2.copy_grid(grid)
        # check if grid and copy have same values
        self.assertEqual(grid,copy)
        # check copy is not a shallow copy of grid
        for i in range(len(grid)):
            self.assertFalse(grid[i] is copy[i])

    def test_get_nbr_of_neighbors_1(self):
        grid = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(project2.get_nbr_of_neighbors(0,0,grid),0)

    def test_get_nbr_of_neighbors_2(self):
        grid = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(project2.get_nbr_of_neighbors(1,2,grid),1)

    def test_get_nbr_of_neighbors_3(self):
        grid = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(project2.get_nbr_of_neighbors(2,2,grid),2)

    def test_get_nbr_of_neighbors_4(self):
        grid = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(project2.get_nbr_of_neighbors(3,2,grid),1)

    def test_get_nbr_of_neighbors_5(self):
        grid = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(project2.get_nbr_of_neighbors(0,4,grid),0)

    def test_get_nbr_of_neighbors_6(self):
        grid = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(project2.get_nbr_of_neighbors(4,0,grid),0)

    def test_get_nbr_of_neighbors_7(self):
        grid = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(project2.get_nbr_of_neighbors(4,4,grid),0)

    def test_get_nbr_of_neighbors_8(self):
        grid = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(project2.get_nbr_of_neighbors(0,2,grid),1)

    def test_get_nbr_of_neighbors_9(self):
        grid = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(project2.get_nbr_of_neighbors(2,0,grid),0)

    def test_get_nbr_of_neighbors_10(self):
        grid = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(project2.get_nbr_of_neighbors(2,4,grid),0)

    def test_get_nbr_of_neighbors_11(self):
        grid = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(project2.get_nbr_of_neighbors(4,2,grid),1)

    def test_mutate_grid_1(self):
        grid = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0]]
        mutated_grid = project2.mutate_grid(grid)
        expected = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0]]
        self.assertEqual(mutated_grid,expected)
        mutated_grid = project2.mutate_grid(mutated_grid)
        expected = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0]]
        self.assertEqual(mutated_grid,expected)

    def test_mutate_grid_2(self):
        grid = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
        mutated_grid = project2.mutate_grid(grid)
        expected = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(mutated_grid,expected)
        mutated_grid = project2.mutate_grid(mutated_grid)
        expected = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(mutated_grid,expected)

    def test_mutate_grid_3(self):
        grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        mutated_grid = project2.mutate_grid(grid)
        expected = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0,  1, 1, 0,  0], [0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(mutated_grid,expected)
        mutated_grid = project2.mutate_grid(mutated_grid)
        expected = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(mutated_grid,expected)

    def test_mutate_grid_4(self):
        grid = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        mutated_grid = project2.mutate_grid(grid)
        expected = [[0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        self.assertEqual(mutated_grid,expected)
        mutated_grid = project2.mutate_grid(mutated_grid)
        expected = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        self.assertEqual(mutated_grid,expected)
        mutated_grid = project2.mutate_grid(mutated_grid)
        expected = [[0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        self.assertEqual(mutated_grid,expected)

    def test_mutate_grid_5(self):
        grid = [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
        mutated_grid = project2.mutate_grid(grid)
        expected = [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(mutated_grid,expected)
        mutated_grid = project2.mutate_grid(mutated_grid)
        expected = [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(mutated_grid,expected)


# run the unit tests
if __name__ == '__main__':
    unittest.main(verbosity=2)
