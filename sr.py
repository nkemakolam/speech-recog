import speech_recognition as sr
sr.__version__

r = sr.Recognizer()

harvard = sr.AudioFile("male.wav")
with harvard as source:
    print("processing clear wav file")
    audio = r.record(source)
try:
    s = r.recognize_google(audio)
    print("Text: "+s)
except Exception as e:
    print("Exception: "+str(e))


#for noisy  audio file 
noisy = sr.AudioFile("h_noise.wav")
with  noisy as source:
    print("processing noicy wav file")
    
    noisy_audio = r.adjust_for_ambient_noise(source, duration=0.5)
    
try:
    s = r.recognize_google(noisy_audio)
    print("Text: "+s)
except Exception as e:
    print("Exception: "+str(e))


#using actual lapttop microphone
mic = sr.Microphone(device_index=0)
sr.Microphone.list_microphone_names()

with mic as source:
    
    print("testing mic")
    r.adjust_for_ambient_noise(source, duration=2)
    audio_mic = r.listen(source)
try:
    s = r.recognize_google(audio_mic)
    print("Text: "+s)
except Exception as e:
    print("Exception: "+str(e))


# For other languages 
harvard = sr.AudioFile("f_m.wav")
with harvard as source:
    print("processing clear wav file in french")
    audio = r.record(source)
try:
    s = r.recognize_google(audio,language="fr-FR")
    print("Text: "+s)
except Exception as e:
    print("Exception: "+str(e))
