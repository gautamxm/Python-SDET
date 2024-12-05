
import sys
sys.path.append(r"D:\BEBO\Python_SDET\Python-SDET\PracticeSession_14\Inventory")

from Product import *

p1 = product("TV", 10000, 2)
p1.update(2)
p1.display()