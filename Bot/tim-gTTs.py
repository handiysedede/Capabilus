import os
import time
import pyaudio
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts=gTTS(text=text, lang="tr")
    filename="voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

#speak("Merhabalar, Digitürkün bu aya özel fırsatlarını paylaşmak amacıyla rahatsız ediyorum sizleri")
speak("Bakiyenizde 12 TL kalmıştır. Fakirlikten öldün piç.")
