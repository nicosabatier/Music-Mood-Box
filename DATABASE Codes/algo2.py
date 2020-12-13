# coding: utf-8
import csv
import sys
import time
from Adafruit_IO import RequestError, Client, Feed, Data

aio = Client("victorioo93310","aio_gyfw541n4r5hM0tc6sYArCN5ywCs")

data = aio.receive('ambiance')
ambiance = data.value
time = time.strftime("%d-%m-%Y %H:%M")

with open('Ambience.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 1
    for row in csv_reader:
        if row[0] == ambiance:
                play = row[1]
                line_count += 1
        else:
                line_count += 1


with open('historique.csv', mode='a') as historique_file:
                historique_writer = csv.writer(historique_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                historique_writer.writerow([play , time ])


try:
 playlist = aio.feeds('playlist')
except RequestError :
 playlist_feed = Feed(name='playlist')
 playlist_feed = aio.create_feed(playlist_feed)

aio.send_data(playlist.key, play)




