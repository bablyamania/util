import tm1637
import time
from datetime import datetime


tm = tm1637.TM1637(clk = 18, dio = 17)
clear = [0,0,0,0]
tm.write(clear)
time.sleep(5)


S = 'This is pretty cool'
tm.scroll(S,delay=250)
time.sleep(2)
tm.write(clear)
time.sleep(1)


now = datetime.now()
hh = int(datetime.strftime(now,'%H'))
mm = int(datetime.strftime(now,'%M'))
tm.numbers(hh,mm,colon=True)
time.sleep(2)
tm.write(clear)
