# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:55:34 2019

@author: evan_hurwitz
"""

import random

def __random_strat (board, moves):
    
    return random.choice (moves)

def get_strategy (strat) :
    
    strat_list = {'random' : __random_strat}
    
    return strat_list [strat]