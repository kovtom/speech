# Egyszerű hangfelismerő program amely a SpeechRecognition library-t használja
import speech_recognition as sr

# Hangfelismerő objektum létrehozása
recognizer = sr.Recognizer()

# Mikrofon objektum létrehozása
with sr.Microphone() as source:
    print("Kérlek beszélj!")
    audio = recognizer.listen(source)

# Hang szöveggé alakítása
text = None
print("Hangfelismerés folyamatban...")
try:
    text = recognizer.recognize_google(audio, language="hu-HU")
    print("Felismert szöveg: " + text)
except sr.UnknownValueError:
    print("A program nem tudta felismerni a hangot!")
except sr.RequestError as e:
    print("Hiba történt a Google Speech API használata közben; {0}".format(e))

from gtts import gTTS
import os

# A felismert szöveg hanngál alakítása
if text:
    tts = gTTS(text=text, lang='hu')
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")
else:
    tts = gTTS(text="Nem sikerült felismerni a hangot!", lang='hu')
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")
