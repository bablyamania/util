import time
import matplotlib.pyplot as plt
from drawnow import *
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
cnt = 0
plt.ion()
adc.start_adc(0, gain=GAIN)
print('Reading ADS1x15 channel 0')
value = []

def makeFig():
    plt.ylim(-20000,20000)
    plt.title('Oscilloscope')
    plt.grid(True)
    plt.ylabel('ADC outputs')
    plt.plot(value, 'ro-', label='Channel 0')
    plt.legend(loc='lower right')

while (True):
    values = adc.get_last_result()
    print('Channel 0: {0}'.format(value))
    time.sleep(0.5)
    value.append(int(values))
    drawnow(makeFig)
    plt.pause(.000001)
    cnt = cnt+1
    if(cnt>50):
        value.pop(0)