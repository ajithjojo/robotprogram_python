from neuralintents import GenericAssistant
import voicecontroll as vc
import speech_recognition
import pyttsx3 as tts
import sys
speaker = tts.init()
speaker.setProperty('rate',150)

recognizer = speech_recognition.Recognizer()

assistant = GenericAssistant('intents.json', intent_methods=vc.mappings)
#assistant.train_model()
#assistant.save_model()
assistant.load_model()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            print("start listening")
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            print("stop listening")
            message =  recognizer.recognize_google(audio)
            message = message.lower()
            print(message)

        responseaudio = assistant.request(message)
        if responseaudio != 'none':           
            print(responseaudio)
            speaker.say(responseaudio) 
            speaker.runAndWait()
                

    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()    
        print("not understanding")