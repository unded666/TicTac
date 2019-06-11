# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 13:01:37 2019

@author: evan_hurwitz
"""

import pandas as pd
import numpy as np
from NCBoard import tic_tac_toe_board
# import strategy manager
# import evaluation method

class Manager:
    
    board = tic_tac_toe_board()  
    #     Initialise players
    # Player [0] = init_player ()
    # Player [1] = init_player ()
    
    def __init__ (self):
        self.board = tic_tac_toe_board() #redundant, placeholder really
        
    def request_move (self, p_x):
        
        # call strategy evaluator for player p_x. return requested move
        
        return None
    
    def implement_move (self, move):
        
        # implement requested move, return value based upon success / failure
        # of the move (ie is the move legal)
        
        return None
    
    def __invert_board (self):
        return self.board.board.values * -1
    
    
    
    
    