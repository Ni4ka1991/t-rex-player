#plot-test.py module

import matplotlib.pyplot as plt
from time import time, sleep 
import numpy as np

tensor = np.random.randn( 10, 10 )
img = plt.imshow( tensor )

plt.show()


