import os

carpeta = os.walk("027-Refactorizar")

for x, y, z in carpeta:
    y[:] = [d for d in y if ".history" not in d]
    z = [f for f in z if ".history" not in f]

    print(x, y, z)