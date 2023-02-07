#!/usr/bin/env python3
from enviroment import *  
from time import sleep
from agent import *



env = Enviroment()
ag = Agent()


for s in range( 3 ):
    env.render()
    env.distance( env.player_coords, env.target_coords )
    state = env.step( ag.selectAction())
    print( f"state >>>", state )
    sleep(2.)
