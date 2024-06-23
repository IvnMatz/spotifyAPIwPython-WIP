import os
import sys

def Cpath():
    dir_ac = os.path.dirname(os.path.abspath(__file__))
    dir_1 = os.path.join(dir_ac, '..', 'src')
    sys.path.append(dir_1)
