import os

carpeta = os.walk("027-Refactorizar")

for x,y,z in carpeta:
  print(x,y,z)