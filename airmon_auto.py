import os
from time import sleep, time
from wifi import Cell
import subprocess

print("This Project Have been done For School , you use its on our own resbonsiblity")
time.sleep(2)
os.system('clear')
cell=Cell.all("wlan0")

for x in xrange(0,len(cell)):
    print ("The network name that aviable:" + str(cell[x]))

#line creator
cmd = ['echo', 'I like potatos']
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

o, e = proc.communicate()

print('Output: ' + o.decode('ascii'))
print('Error: '  + e.decode('ascii'))
print('code: ' + str(proc.returncode))



