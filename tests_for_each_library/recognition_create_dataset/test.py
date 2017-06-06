import time
import speech_recognition as sr
import librosa
language="fr-FR"
def callback(recognizer, audio):
    try:
        sentence = recognizer.recognize_google(audio, language=language)
        wave_file_name = "test.wav"
        wav_file = open(wave_file_name,"wb")
        wav_file.write(audio.get_wav_data())
        wav_file.close()
        wave, sample_rate = librosa.load(wave_file_name, mono=True, sr=None)
        wave = wave[::3]
        mfcc = librosa.feature.mfcc(wave, sr=16000)
        print sentence,mfcc

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


recognizer = sr.Recognizer()
microphone = sr.Microphone()
with microphone as source:
    recognizer.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = recognizer.listen_in_background(microphone, callback)
print stop_listening
# `stop_listening` is now a function that, when called, stops background listening

# do some other computation for 5 seconds, then stop listening and keep doing other computations
#for _ in range(500): time.sleep(0.1)  # we're still listening even though the main thread is doing other things
#stop_listening()  # calling this function requests that the background listener stop listening
while True: 
    pass
#time.sleep(0.05)
#"""

