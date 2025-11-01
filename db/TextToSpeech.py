import pyttsx3

class TextToSpeech:
    def sayText(self, text):
        engine = pyttsx3.init()
        engine.setProperty('volume',1.0)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 160)

        engine.say(text)
        engine.runAndWait()
        engine.stop()