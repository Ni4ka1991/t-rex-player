#!/usr/bin/env python3

#TORCH
import torch
from torch import nn

#OTHER
import time
import random
import numpy as np
from helper_func import *
from data import *
from detect2 import *
from os import system
from selenium import webdriver


#system( "clear" )

##Connect to browser

browser = webdriver.Chrome( './drivers/chromedriver.exe' )

