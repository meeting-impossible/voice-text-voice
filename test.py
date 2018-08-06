import pyaudio
import wave
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index.html")
def record():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "record.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    return ("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    return ("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()


# r = sr.Recognizer()
# test = sr.AudioFile("record.wav")
# with test as source:
#     r.adjust_for_ambient_noise(source)
#     audio = r.record(source)
# type(audio)
# text = r.recognize_google(audio,language="zh-CN")

# translator = Translator()
# translations = translator.translate(text,dest = 'zh-CN')
# aft = translations.text


# tts = gTTS(text = aft, lang="zh-CN")
# tts.save("output.wav")
# os.system("mpg321 output.wav")

if __name__ == "__main__":
    app.run(debug=True)