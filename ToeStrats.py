# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:55:34 2019

@author: evan_hurwitz
"""

import random

class toe_strat:
    
    s_call = None
    u_call = None
    
    def __init__ (self, strat):
        stratcall = self.get_strategy (strat)
        updatecall = self.get_update (strat)
        self.s_call = stratcall
        self.u_call = updatecall
        
    def call_strat (self, **kwargs):
        return self.s_call (**kwargs)
    
    def update_strat (self, **kwargs):
        
        self.u_call (**kwargs)

    def __random_strat (board, moves):
    
        return random.choice (moves)

    def __update_random_strat (**args):
    
        return Null
    
    def get_strategy (self, strat) :
    
        strat_list = {'random' : self.__random_strat}
    
        return strat_list [strat]
    
    def get_update (self, strat):
        
        strat_list = {'random' : self.__update_random_strat}        
        
        return strat_list [strat]
    
    