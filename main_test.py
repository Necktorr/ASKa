import os
import torch

import sounddevice as sd

import time

local_file = 'model.pt'
speaker = 'xenia'  # 'aidar', 'baya', 'kseniya', 'xenia', 'random'
sample_rate = 48000  # 8000, 24000, 48000
language = 'ru'
model_id = 'ru_v3'

put_accent = True
put_yo = True
device = torch.device('cpu')


model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language='ru',
                                     speaker='ru_v3')

model.to(device)

example_text = '  кедр в сосновой роще заблестал розами чёрными  '

audio = model.apply_tts(text=example_text,
                        speaker=speaker,
                        sample_rate=sample_rate,
                        put_accent=put_accent,
                        put_yo=put_yo)


print(example_text)

sd.play(audio, sample_rate)

time.sleep(len(audio) / sample_rate)
sd.stop()