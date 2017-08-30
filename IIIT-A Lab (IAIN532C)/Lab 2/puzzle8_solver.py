'''8-PUZZLE SOLVER'''

from puzzle_solver import Puzzle

class Puzzle8(Puzzle):
    '''8-PUZZLE'''
    def __init__(self, start):
        super(Puzzle8, self).__init__([[1, 2, 3], \
                                        [4, 5, 6], \
                                        [7, 8, 0]])
        self.state = start

    def solvable(self):
        '''CHECKS IF 8-PUZZLE IS SOLVABLE FROM CURRENT STATE TO GOAL STATE'''
        flattened_state = sum(self.state, [])
        return True if super(Puzzle8, self).get_inversion_count(flattened_state) % 2 == 0 else False

    
    
