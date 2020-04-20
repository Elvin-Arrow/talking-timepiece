import os
from gtts import gTTS
from datetime import datetime
import playsound
import threading

def speakTime(text):
    tts = gTTS(text=text, lang='en-gb')
    filename = "time.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def putTimeTogether(useTimePeriod):
    currentTime = ''
    timeNow = datetime.now().time()

    # Set time period
    timePeriod = 'AM'

    # Get hours
    hours = timeNow.strftime("%H")

    # Convert the time fron 24-h format to 12-h
    # For ease of comparison, convert time string to integer
    temp = int(hours)

    if (temp > 12):
        temp = temp - 12
        timePeriod = 'PM'

    if (temp == 0):
        temp = 12
        timePeriod = 'AM'

    # Update the hours as per updated format
    hours = str(temp)

    # Get minutes
    minutes = timeNow.strftime("%M")

    # Form the time string to be returned as per the required settings
    if useTimePeriod:
       currentTime = hours + minutes + ' ' + timePeriod
    else:
        currentTime = hours + ':' + minutes



    return currentTime

def sayTime():
    currentTime = putTimeTogether(False)
    print("Current Time =", currentTime)

    text = 'It\'s' + currentTime
    speakTime(text)


def main():
    thread = threading.Thread(target=sayTime)
    thread.start()

    # wait here for the result to be available before continuing
    thread.join()


main()
