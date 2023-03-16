#!/usr/bin/env python3
from enviroment import *  
from time import sleep
from agent import *



ag = Agent()
env = Enviroment( ag )    #init self.reset()


for s in range( 8 ):
    env.render()
    print( f"last_state", ag.last_state())
    state, done = env.step(ag.selectAction( ))
    ag.rememberState( state )
    #print( state )
    sleep(4.)

    if done:
        print( "Episode done" )
        break
