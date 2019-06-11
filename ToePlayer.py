# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:52:47 2019

@author: evan_hurwitz
"""

import ToeStrats

class TTPlayer:
    play_strat = None
    
    def __init__ (self, IStrat = 'random'):
        
        self.play_strat = ToeStrats.get_strategy (IStrat)
        
    
    
    