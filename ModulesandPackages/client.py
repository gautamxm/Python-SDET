
import sys

from ModulesandPackages.Pack1.Module2 import display

sys.path.append(r"D:\BEBO\Python_SDET\Python-SDET\ModulesandPackages\Pack1")
sys.path.append(r"D:\BEBO\Python_SDET\Python-SDET\ModulesandPackages\Pack1\PackA")

from Module1 import *
from Module2 import *
show()
display()

from Module3 import *
display()

