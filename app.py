#!/usr/bin/env python3
from enviroment import *  
from time import sleep
from agent import *



ag = Agent()
env = Enviroment( ag )


for s in range( 3 ):
    env.render()
    print( ">>>", s )
    '''
    env.distance( env.player_coords, env.target_coords )
    state = env.step( ag.selectAction())
    ag.rememberState = state
    print( f"state >>>", state )
    '''
    sleep(3.)
