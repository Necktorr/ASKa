import vosk
import sys
import sounddevice as sd
import queue
import json

class VA_Listen_Module():
    def __init__(self) -> None:
        self.model = vosk.Model("model_small")
        self.samplerate = 16000
        self.device = 1

        self.q = queue.Queue()

        self.isWork = True

    def q_callback(self, indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(indata))

    def start_listen(self, callback):
        self.isWork = True

        with sd.RawInputStream(samplerate=self.samplerate, blocksize=8000, 
                            device=self.device, dtype='int16',
                            channels=1, callback=self.q_callback):

            rec = vosk.KaldiRecognizer(self.model, self.samplerate)

            while self.isWork:
                data = self.q.get()
                if rec.AcceptWaveform(data):
                    callback(json.loads(rec.Result())["text"])
                #else:
                #    print(rec.PartialResult())
                
    def stop_listen(self):
        self.isWork = False