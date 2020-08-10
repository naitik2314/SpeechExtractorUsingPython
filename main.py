import speech_recognition as sr
import moviepy.editor as mp

clip = mp.VideoFileClip(r"ep1.mp4") #Your video name in Semicolon and it can be in the same directory so no need to specify the path, but if it is another directory, name should be specified.
clip.audio.write_audiofile(r"converted.wav")

r = sr.Recognizer()

audio = sr.AudioFile("converted.wav")

with audio as source:
    audio_file = r.record(source)
    result = r.recognize_google(audio_file)

#exporting the result
with open('recognized.txt' ,mode='w') as file:
    file.write("Recognized Speech:")
    file.write(result)
    print("Ready!")