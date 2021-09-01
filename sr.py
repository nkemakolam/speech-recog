import speech_recognition as sr
sr.__version__

r = sr.Recognizer()

harvard = sr.AudioFile("male.wav")
with harvard as source:
    audio = r.record(source)
try:
    s = r.recognize_google(audio)
    print("Text: "+s)
except Exception as e:
    print("Exception: "+str(e))
type(audio)
#r.recognize_google(audio)
