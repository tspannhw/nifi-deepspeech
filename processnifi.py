from deepspeech import Model
import json
import datetime
# forked from https://progur.com/2018/02/how-to-use-mozilla-deepspeech-tutorial.html
import scipy.io.wavfile as wav
import sys
"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""

import pyaudio
import wave

RATE = 16000
BLOCKS_PER_SECOND = 50
BLOCK_SIZE = int(RATE / float(BLOCKS_PER_SECOND))
FORMAT = pyaudio.paInt16
CHANNELS =1
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
CHUNK = 1024

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=BLOCK_SIZE)

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

now = datetime.datetime.now()
row = { }
row['systemtime'] = now.strftime('%m/%d/%Y %H:%M:%S')

ds = Model(sys.argv[1], 26, 9, sys.argv[2], 500)
fs, audio = wav.read(WAVE_OUTPUT_FILENAME)
row ['voice_string'] = ds.stt(audio, fs)
json_string = json.dumps(row)
print (json_string)
