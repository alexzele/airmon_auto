from os import system, os
from time import sleep, time
from wifi import Cell

print("This Project Have been done For School , you use its on our own resbonsiblity")
time.sleep(2)
os.system('clear')
cell=Cell.all("wlan0")

for x in xrange(0,len(cell)):
    print ("The network name that aviable:" + str(cell[x]))






