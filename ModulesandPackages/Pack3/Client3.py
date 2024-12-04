import sys
sys.path.append(r"D:\BEBO\Python_SDET\Python-SDET\ModulesandPackages\Pack1")
sys.path.append(r"D:\BEBO\Python_SDET\Python-SDET\ModulesandPackages\Pack2")

from Employe import  *
from Student import  *

obj1 = employee()
obj1.emp(23,"Lucifer")

obj2 = student()
obj2.std("Gautam", 23)

