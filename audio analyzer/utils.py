# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  Author :    WangJingyao
-------------------------------------------------
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchaudio
from IPython.display import Audio, display
import IPython.display as ipd

def record(seconds=3):

	from google.colab import output as colab_output
	from base64 import b64decode
	from io import BytesIO
	from pydub import AudioSegment

	RECORD = (
	b"const sleep  = time => new Promise(resolve => setTimeout(resolve, time))\n"
	b"const b2text = blob => new Promise(resolve => {\n"
	b"  const reader = new FileReader()\n"
	b"  reader.onloadend = e => resolve(e.srcElement.result)\n"
	b"  reader.readAsDataURL(blob)\n"
	b"})\n"
	b"var record = time => new Promise(async resolve => {\n"
	b"  stream = await navigator.mediaDevices.getUserMedia({ audio: true })\n"
	b"  recorder = new MediaRecorder(stream)\n"
	b"  chunks = []\n"
	b"  recorder.ondataavailable = e => chunks.push(e.data)\n"
	b"  recorder.start()\n"
	b"  await sleep(time)\n"
	b"  recorder.onstop = async ()=>{\n"
	b"    blob = new Blob(chunks)\n"
	b"    text = await b2text(blob)\n"
	b"    resolve(text)\n"
	b"  }\n"
	b"  recorder.stop()\n"
	b"})"
	)
	RECORD = RECORD.decode("ascii")

	print(f"Recording started for {seconds} seconds.")
	display(ipd.Javascript(RECORD))
	s = colab_output.eval_js("record(%d)" % (seconds * 1000))
	print("Recording ended.")
	b = b64decode(s.split(",")[1])

	fileformat = "wav"
	filename = f"_audio.{fileformat}"
	AudioSegment.from_file(BytesIO(b)).export(filename, format=fileformat)
	#audio = torchaudio.load(filename)
	#waveform = torch.reshape(audio[0], (1, audio[0].shape[0]))
	#return waveform
	return torchaudio.load(filename)
    

def predict(tensor, device, model):
	#
	new_sample_rate = 8000
	sample_rate = 44100
	transform = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=new_sample_rate)

	# Use the model to predict the label of the waveform
	tensor = tensor.to(device)
	tensor = transform(tensor)
	tensor = model(tensor.unsqueeze(0))
	#tensor = get_likely_index(tensor)
	#tensor = index_to_label(tensor.squeeze())
	return tensor.argmax(dim=-1)

def loadModel(model, path):
	checkpoint = torch.load(path)
	model.load_state_dict(checkpoint['model_state_dict'])

	optimizer = optim.Adam(model.parameters())
	optimizer.load_state_dict(checkpoint['optimizer_state_dict'])

	scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)
	scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)

	epoch = checkpoint['epoch']
	loss = checkpoint['loss']
	print(f"Loaded model with epoch:{epoch} and loss:{loss}")
	return model, optimizer, scheduler

def save_checkpoint(model, optimizer, epoch, loss, model_name):
	PATH = './' + model_name + '.tar'
	state = {
	    'epoch': epoch,
	    'model_state_dict': model.state_dict(),
	    'optimizer_state_dict': optimizer.state_dict(),
	    'loss': loss
	  }
	torch.save(state, PATH)
	print(f"Saved checkpoint at epoch {state['epoch']} with loss {state['loss']}")

def pad_sequence(batch):
	# Make all tensor in a batch the same length by padding with zeros
	batch = [item.t() for item in batch]
	batch = torch.nn.utils.rnn.pad_sequence(batch, batch_first=True, padding_value=0.)
	return batch.permute(0, 2, 1)


def collate_fn(batch):
	# A data tuple has the form:
	# waveform, label

	tensors, targets = [], []

	# Gather in lists, and encode labels as indices
	for waveform, label in batch:
		tensors += [waveform]
		targets += [torch.tensor(label)]

	# Group the list of tensors into a batched tensor
	tensors = pad_sequence(tensors)
	targets = torch.stack(targets)

	return tensors, targets

def number_of_correct(pred, target):
	# count number of correct predictions
	return pred.squeeze().eq(target).sum().item()


def get_likely_index(tensor):
	# find most likely label index for each element in the batch
	return tensor.argmax(dim=-1)
