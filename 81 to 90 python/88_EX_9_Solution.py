# Shoutouts to everyone
import pyttsx3
engine = pyttsx3.init()
names = ["ayaz", "Code with Harry", "panda", "apna College"]
for name in names:
  engine.say(f"Shoutout to {name}!")

engine.runAndWait()