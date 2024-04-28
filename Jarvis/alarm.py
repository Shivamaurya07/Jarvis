import pyttsx3
import datetime
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def ring(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            speak("Alarm ringing, sir")
            os.startfile("music.mp3")  # You can choose any music or ringtone
            break

# Read the previous alarm time from file
with open("Alarmtext.txt", "rt") as file:
    previous_alarm_time = file.read().strip()

# If there was a previous alarm time, delete it
if previous_alarm_time:
    speak("Previous alarm deleted.")
    with open("Alarmtext.txt", "w") as file:
        file.truncate(0)

# Set the new alarm time
speak("Please set the new alarm time.")
new_alarm_time = input("New alarm time (HH:MM:SS): ")

# Write the new alarm time to the file
with open("Alarmtext.txt", "w") as file:
    file.write(new_alarm_time)

# Run the alarm function
ring(new_alarm_time)
