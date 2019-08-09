import os
from time import sleep, time
from wifi import Cell
import subprocess




def main():

    print("This Project Have been done For School , you use its on our own resbonsiblity")

    cmd = ['airmon-ng start wlan0']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    o, e = proc.communicate()

    print('Output: ' + o)
    print('Error: '  + e)


if __name__ == '__main__':
    main()

