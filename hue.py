#!/usr/bin/python3
import time
from qhue import Bridge
from config import BRIDGE_IP, USERNAME
from config import LIGHT_ID,SLEEP_HUE, SLEEP_BRI, SLEEP_SAT

def sleepsequence():
    bridge = Bridge(BRIDGE_IP, USERNAME)
    #dim other bedroom light
    bridge.lights[1].state(on=False)
    #start sequence on chosen light (LIGHT_ID)
    bridge.lights[LIGHT_ID].state(on=True, hue=SLEEP_HUE, bri=SLEEP_BRI, sat=SLEEP_SAT)
    sleep_bri=SLEEP_BRI
    #increase period from 5.4s to 10s (6bpm) &
    start_sequence=list(range(60,100,2))
    #keep pace from this moment untill 8min after start
    end_sequence=[100]*int((8*600-sum(start_sequence))//100)
    for period in start_sequence+end_sequence:
        #print('seq,period:{}, bri:{}'.format(period,sleep_bri))
        up_transition=int(0.4*period)
        down_transition=int(0.6*period)
        sleep_bri=int(max(sleep_bri-5,SLEEP_BRI/4))
        bridge.lights[LIGHT_ID].state(on=False,transitiontime=down_transition)
        time.sleep(down_transition/10)
        bridge.lights[LIGHT_ID].state(on=True,hue=SLEEP_HUE, bri=sleep_bri, sat=SLEEP_SAT,transitiontime=up_transition)
        time.sleep(up_transition/10)
    bridge.lights[LIGHT_ID].state(on=False,transitiontime=down_transition)

if __name__ == '__main__':
    sleepsequence()
