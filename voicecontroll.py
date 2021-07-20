import pyttsx3 as tts
import sys
from neuralintents import GenericAssistant
speaker = tts.init()
speaker.setProperty('rate',150)

assistant = GenericAssistant('intents.json')

def createnote():
    global recognizer
    speaker.say("what do you want to write?")
    speaker.runAndWait()

    done = False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say("choose a file name")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename =  recognizer.recognize_google(audio)
                filename = filename.lower()
           
            with    open(filename, 'w') as f:
                f.write(note)
                done = True
                speaker.say("saved the note {filename}")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Please try again")
            speaker.runAndWait()

   

def quit():
        speaker.say("Bye") 
        speaker.runAndWait()
        sys.exit(0)


mappings = {        
       "createnote": createnote,
       "exit": quit
}
