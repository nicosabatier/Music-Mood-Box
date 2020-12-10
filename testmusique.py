from omxplayer.player import OMXPlayer
from time import sleep
import random
import sys
from pathlib import Path
from Adafruit_IO import Client
aio = Client('victorioo93310','aio_gyfw541n4r5hM0tc6sYArCN5ywCs')

data = aio.receive('playlist')
#ambiance = data.value
#ambiance = sys.argv[1]
#print (ambiance)
ambiance = 'reggae'
print (ambiance)
sleep(5)
wordlist = []
with open('/home/pi/Documents/' + ambiance +".csv") as file:
       for line in file:
           wordlist.append(line)
wordlist = list(map(lambda x : x[:-2], wordlist))
wordlist[0] = wordlist[0][3:]
word = random.choice(wordlist)
print(word)
path = ('/home/pi/Music/' + word)

Music = Path(path)
player = OMXPlayer(Music)

sleep(30)

player.quit()
