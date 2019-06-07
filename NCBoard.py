# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:19:27 2019

@author: evan_hurwitz
"""

import pandas as pd
import numpy as np

class tic_tac_toe_board:
    board = pd.DataFrame ()
    
    
    def __init__ (self):
        
        for X in list('ABC'):
            self.board [X] = [0, 0, 0]
        self.board.index = list ('XYZ')
        
    def __is_winner (self, rowz, colz):
        """ determine if a set of three indices on the board produces a winner
            returns 0 if no winner, 1 if 1s win, -1 if -1s win
        """
        
        O = []
        for i, R in enumerate(rowz):
            C = colz [i]
            O.append (self.board [C][R])
        
        if np.abs (sum(O)) == 3:
            if sum(O) == 3:
                return 1
            else:
                return -1
        else:
            return 0
    
    def board_shape (self, InShape : np.ndarray):
        Dummy = pd.DataFrame (InShape, columns = self.board.columns,
                              index = self.board.index)
        self.board = Dummy
        
    def reset_board (self):
        self.board = self.board.replace ([-1, 0, 1], 0)
        
    def draw_board (self):
        rail = '   |'*2
        gutter = '-'*11
        visu = self.board.copy()
        visu = visu.replace ([-1, 0, 1], ['X', ' ', 'O'])
        for PRow in list ('XYZ'):
            print (rail)
            print (' {} | {} | {} '.format (visu.loc[PRow]['A'], 
                   visu.loc[PRow]['B'], visu.loc[PRow]['C']))
            print (rail)
            if PRow != 'Z':
                print (gutter)
        
    def __is_available (self, Row, Column):
        V = self.board [Column][Row]
        if V == 0:
            return True
        else:
            return False
        
    def __place_piece (self, Row, Column, Val):
        if self.__is_available(Row, Column):
            self.board [Column][Row] = Val
            O = True
        else:
            O = False
        
        return O
    
    def __valid_moves (self):
        rowz = list('XYZ')
        colz = list ('ABC')
        O = []
        for R in rowz:
            for C in colz:
                if self.__is_available (R, C):
                    O.append ([R, C])
        return O
    
    def place_piece (self, Row, Column, Val):
        placed = self.__place_piece (Row, Column, Val)
        if not placed:
            print ('piece not placed, square already taken')
    
    def show_valid_moves(self):
        Moves = self.__valid_moves()
        print (Moves)
    
    def __extract_rowcols (self, InCoords):
        rowz = []
        colz = []
        for coord in InCoords:
            rowz.append (coord[0])
            colz.append (coord[1])
            
        return rowz, colz    
    
    def __game_result (self):
        """ determines if there is currently a winner. Returns the following:
                -1 : X wins
                0  : not ended
                1  : O wins
                2  : draw
        """
        scenarios = []
        # rows
        for R in list ('XYZ'):
            scenarios.append ([[R, 'A'], [R, 'B'], [R, 'C']])
        for C in list ('ABC'):
            scenarios.append ([['X', C], ['Y', C], ['Z', C]])
        scenarios.append ([['X', 'A'], ['Y', 'B'], ['Z', 'C']])
        scenarios.append ([['X', 'C'], ['Y', 'B'], ['Z', 'A']])
        result = 0
        for scen in scenarios:
            rz, cz = self.__extract_rowcols (scen)
            R = self.__is_winner (rz, cz)
            if R != 0:
                result = R
        if result == 0: #check for a draw
            valid_moves = self.__valid_moves()
            if len(valid_moves) == 0:
                result = 2
        return result
    
    def who_won(self):
        R = self.__game_result()
        result_key = {0 : 'The game is still ongoing',
                      1 : 'Noughts have won the game',
                      -1 : 'Crosses have won the game',
                      2 : 'The game has ended in a draw'}
        print (result_key[R])
        
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
