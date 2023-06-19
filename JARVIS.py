import speech_recognition as sr
import os
import sys

# Якщо немає звуку
# pip install pyttsx3
import pyttsx3
engine = pyttsx3.init()
# engine.say("Say")
# engine.runAndWait()


def talk(words):
    print(words)
    engine.say(words)
    engine.runAndWait()
    # os.system("say " + words)


talk("Hi, can I help you?")

