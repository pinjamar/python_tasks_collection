#opcija flush u naredbi print, po defaultu flush = False

import time

print("\nIspis Dobra vecer uz flush = True\n")
print("Dobra", end=" ", flush = True)
time.sleep(2)
print("vecer")

print("\nIspis Dobra vecer uz flush = False\n")
print("Dobra", end=" ", flush = False)
time.sleep(2)
print("vecer")