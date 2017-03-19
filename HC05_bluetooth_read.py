import serial
import numpy as np
import time

ser = serial.Serial('/dev/rfcomm0', 9600)

def saveReading(temperature):
    newReading = time.strftime("%Y-%m-%d %H:%M:%S") + \
                 ',' + str(temperature) + '\n'
    
    print('Saving new reading: ' + newReading)
    with open('/home/pi/Desktop/temperatureReadings.csv', 'ab') as file:
        file.write(newReading.encode('utf-8'))


'''
def testSerial(someString):
    start = False
    temp = []
    for i in range(0, len(someString)):
        character = someString[i]
        asciiOrd = ord(character)
        #If it is a start sequence and we have already started,
        #start over.
        if (asciiOrd == 60 and start == True):
            temp = []
        #If it is a start sequence and we have not started,
        #start now
        elif (asciiOrd == 60 and start == False):
            start = True

        #If it is not a start or a stop, and we have started,
        #simply append.
        elif (asciiOrd != 60 and asciiOrd !=62 and start == True):
            temp.append(character)

        #If it is an end character, and we have started then we are done.
        elif (asciiOrd == 62 and start == True):

            #If there is something there, and it is a proper float
            if len(temp) > 0:
                try:
                    converted = float(''.join(temp))
                    saveReading(converted)
                except Exception as e:
                    print(e)

            start = False
            temp = []
'''

print("Waiting for data...")
temp = []
start = False
while (True):
    #Read one byte at a time
    if (ser.inWaiting() > 0):
        character = ser.read()
        asciiOrd = ord(character)
        #If it is a start sequence and we have already started,
        #start over.
        if (asciiOrd == 60 and start == True):
            temp = []
        #If it is a start sequence and we have not started,
        #start now
        elif (asciiOrd == 60 and start == False):
            start = True

        #If it is not a start or a stop, and we have started,
        #simply append.
        elif (asciiOrd != 60 and asciiOrd !=62 and start == True):
            temp.append(character.decode('ascii'))
        #If it is an end character, and we have started then we are done.
        elif (asciiOrd == 62 and start == True):

            #If there is something there, and it is a proper float
            if len(temp) > 0:
                try:
                    converted = float(''.join(temp))
                    saveReading(converted)
                    #Acknowledge receipt of data
                    ser.write('<5>'.encode('utf-8'))
                except Exception as e:
                    print(e)
            start = False
            temp = []
