#!/usr/bin/env python3
from enviroment import *  
from time import sleep
from agent import *



ag = Agent()
env = Enviroment( ag )    #init self.reset()


for s in range( 4 ):
    env.render()
    state, done = env.step(ag.selectAction( ))
    ag.rememberState( state )
    print( state )
    sleep(3.)

    if done:
        print( "Episode done" )
        break
