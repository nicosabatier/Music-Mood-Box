# -*- coding: utf-8 -*-
import struct
import serial
import random
from datetime import datetime
from time import sleep

def get_bytes_from_esp(ser):
    number = b''
    for i in range(4):
        number+=ser.read()
    return number

def read_from_esp(tty):

    ser = serial.Serial('/dev/{}'.format(tty), 9600, timeout=1)
    ser.flush()

    number=get_bytes_from_esp(ser)
    number2=get_bytes_from_esp(ser)
    number3=get_bytes_from_esp(ser)

    value = struct.unpack('i' , number)[0]
    value2 = round(struct.unpack('f',number2)[0], 2)
    value3 = struct.unpack('i',number3)[0]

    return value, value2, value3

def get_category_from_luminosity(luminosity):
    if luminosity < 200 :
        return "very_calm"
    elif luminosity < 500:
        return "calm"
    elif luminosity < 800:
        return "ambiant"
    else:
        return "caliente"

def get_category_from_temperature(temperature):
    if temperature < 15:
        return "basse"
    elif temperature < 25:
        return "moderee"
    else :
        return "elevee"

def get_category_from_mouvement(mouvement):
    if mouvement == 0:
        return "pas_de_mouvement"
    else:
        return "mouvement"

def get_category_from_sensors(luminosity, temperature, mouvement):
    luminosity_cat = get_category_from_luminosity(luminosity)
    temperature_cat= get_category_from_temperature(temperature)
    mouvement_cat =  get_category_from_mouvement(mouvement)

    if mouvement_cat == "pas_de_mouvement":
        if temperature_cat in ["basse", "moderee"]:
            if luminosity_cat in ["very_calm", "calm"]:
                return "calme"
            else:
                return "discussion"
        else: # elevee
            return "plage"
    else: # mouvement
        if temperature_cat in ["moderee", "elevee"]:
            if luminosity_cat in ["calm", "ambiant"]:
                return "soirée"
            elif luminosity_cat == "caliente":
                return "fete"
            else : # very_calm
                return "repas"
        else : # temperature elevee
            if luminosity_cat in ["ambiant", "caliente"]:
                return "fete"
            elif luminosity_cat == "calm":
                return "plage"
            else: # very_calm
                return "repas" # instrumetal

if __name__ == '__main__':
    while True:
        sleep(0.5)
        luminosity, temperature, mouvement = read_from_esp('ttyUSB0')
        print("luminosity:", luminosity, get_category_from_luminosity(luminosity))
        print("temperature:", temperature,"C")
        print("mouvement:", mouvement)
        music_cat = get_category_from_sensors(luminosity, temperature, mouvement)
        print("ambiance environnement :", music_cat)
        print("----------------")

        from Adafruit_IO import RequestError, Client, Feed, Data
        aio=Client("victorioo93310","aio_gyfw541n4r5hM0tc6sYArCN5ywCs")
        try:
         ambiance = aio.feeds('ambiance')
        except RequestError :
         ambiance_feed = Feed(name='ambiance')
         ambiance_feed = aio.create_feed('vvhvh')

        aio.send_data(ambiance.key, music_cat)  
    
