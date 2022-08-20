# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  Author :    WangJingyao
-------------------------------------------------
"""

# !pip install speechbrain
# !pip install transformers
# !pip install pydub
# !pip install librosa

import time
from time import perf_counter
import numpy as np
import matplotlib.pyplot as plt
import librosa
from pydub import AudioSegment
import os
from google.colab import files
import moviepy.editor
from transformers import pipeline

from speechbrain.pretrained import EncoderDecoderASR

asr_model2 = EncoderDecoderASR.from_hparams(source="speechbrain/asr-crdnn-rnnlm-librispeech", savedir="pretrained_models/asr-crdnn-rnnlm-librispeech")

def transcribe_audio(fileList = []):
  listOfText = []
  if fileList == [] :
    uploaded = files.upload()
    listOfAudios = list(uploaded.keys())
  else:
    listOfAudios = fileList
  
  a = perf_counter()
  for file in listOfAudios:
    duration = librosa.get_duration(filename=file)
    t1 = 0
    t2 = duration * 1000 if duration < 30 else 30000
    textTemp = ""
    j = 1
    i = 1
    final_fragment = False
    while t2 <= duration*1000 and not final_fragment:
      final_fragment = True if t2 == duration * 1000 else False
      newAudio = AudioSegment.from_wav(file)
      newAudio = newAudio[t1:t2]
      name = 'Audio_' + str(j) + '_segment_' + str(i) + '.wav'
      newAudio.export(name, format="wav")
      t1 += 30000
      t2 = duration * 1000 if t2 + 30000 > duration * 1000 else t2 + 30000
      i+= 1
      print("\nAnalizando: " + name)
      resAux = asr_model2.transcribe_file(os.getcwd() + "/" + name)
      textTemp = textTemp + " " + resAux
    
    listOfText.append(textTemp[1:])
    j += 1
  print("\nTerminado en: " + str(f'{perf_counter() - a:.2f}') + " seg.\n")

  return listOfText

def transcribe_video(fileList = []):
  listOfText = []
  if fileList == [] :
    uploaded = files.upload()
    listOfAudios = list(uploaded.keys())
  else:
    listOfAudios = fileList
  a = perf_counter()
  for file in listOfAudios:
    duration = librosa.get_duration(filename=file)
    j = 1
    i = 1
    video = moviepy.editor.VideoFileClip(os.getcwd() + "/" + file)
    audio = video.audio
    nameVideo = "AudioExtraction_Video_" + str(j) + (".wav")
    print("\nExporting audio from video: " + file + "\nTo: " + nameVideo)
    audio.write_audiofile(os.getcwd() + "/" + nameVideo)
    t1 = 0
    t2 = duration * 1000 if duration < 30 else 30000
    textTemp = ""
    
    final_fragment = False
    while t2 <= duration*1000 and not final_fragment:
      final_fragment = True if t2 == duration * 1000 else False
      newAudio = AudioSegment.from_wav(nameVideo)
      newAudio = newAudio[t1:t2]
      name = 'Video_' + str(j) + '_segment_' + str(i) + '.wav'
      newAudio.export(name, format="wav")
      t1 += 30000
      t2 = duration * 1000 if t2 + 30000 > duration * 1000 else t2 + 30000
      i+= 1
      print("\nAnalizando: " + name)
      resAux = asr_model2.transcribe_file(os.getcwd() + "/" + name)
      textTemp = textTemp + " " + resAux
    
    listOfText.append(textTemp[1:])
    j += 1
  print("\nTerminado en: " + str(f'{perf_counter() - a:.2f}') + " seg.\n")

  return listOfText