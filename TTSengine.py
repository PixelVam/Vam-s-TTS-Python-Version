from gtts import gTTS
import os as o
from time import sleep

print("TTS V engine Version 1.12")
print("Disclaimer: Every mp3 gets deleted")
while True:
    a = input("Write a sentence: ")
    print(a)
    # saves the mp3 file
    filename = "voice.mp3"
    tts = gTTS(text=a, lang='en')
    tts.save(filename)

    # gets the absolute path to play it
    filepath = o.path.abspath(filename)
    o.system("start " + filepath)

    # input for how much seconds the file is going to stay before being deleted
    b = int(input("How much time would you like when your file gets deleted?: "))
    sleep(b)

    # it deletes it
    o.remove(filename)
    print("Deleted:", filename)



