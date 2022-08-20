# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  Author :    WangJingyao
-------------------------------------------------
"""
import torch
import torch.nn as nn
import torch.nn.functional as F

# M5 MODEL
class M5(nn.Module):
  def __init__(self, n_input=1, n_output=2, stride=16, n_channel=32): # n_channel=32
    super().__init__()
    self.conv1 = nn.Conv1d(n_input, n_channel, kernel_size=80, stride=stride)
    self.bn1 = nn.BatchNorm1d(n_channel)
    self.pool1 = nn.MaxPool1d(4)
    self.conv2 = nn.Conv1d(n_channel, n_channel, kernel_size=3)
    self.bn2 = nn.BatchNorm1d(n_channel)
    self.pool2 = nn.MaxPool1d(4)
    self.conv3 = nn.Conv1d(n_channel, 2 * n_channel, kernel_size=3)
    self.bn3 = nn.BatchNorm1d(2 * n_channel)
    self.pool3 = nn.MaxPool1d(4)
    self.conv4 = nn.Conv1d(2 * n_channel, 2 * n_channel, kernel_size=3)
    self.bn4 = nn.BatchNorm1d(2 * n_channel)
    self.pool4 = nn.MaxPool1d(4)
    self.fc1 = nn.Linear(2 * n_channel, n_output)
    
    print('M5 model')
    print('Model n_input', n_input)
    print('Model n_output', n_output)

  def forward(self, x):
    x = self.conv1(x)
    x = F.relu(self.bn1(x))
    x = self.pool1(x)
    x = self.conv2(x)
    x = F.relu(self.bn2(x))
    x = self.pool2(x)
    x = self.conv3(x)
    x = F.relu(self.bn3(x))
    x = self.pool3(x)
    x = self.conv4(x)
    x = F.relu(self.bn4(x))
    x = self.pool4(x)
    x = F.avg_pool1d(x, x.shape[-1])
    x = x.permute(0, 2, 1)
    x = self.fc1(x)

    return F.log_softmax(x, dim=2)

  def count_parameters(self):
    return sum(p.numel() for p in self.parameters() if p.requires_grad)

# M11 MODEL
class M11(nn.Module):
  def __init__(self, n_input=1, n_output=2, stride=4, n_channel=32):
    super().__init__()
    self.conv1 = nn.Conv1d(n_input, n_channel, kernel_size=80, stride=stride)
    self.bn1 = nn.BatchNorm1d(n_channel)
    self.pool1 = nn.MaxPool1d(4)

    self.conv2 = nn.Conv1d(n_channel, n_channel, kernel_size=3,padding=1)
    self.bn2 = nn.BatchNorm1d(n_channel)
    self.conv3 = nn.Conv1d(n_channel, n_channel, kernel_size=3,padding=1)
    self.bn3 = nn.BatchNorm1d(n_channel)
    self.pool2 = nn.MaxPool1d(4)

    self.conv4 = nn.Conv1d(n_channel, 2 * n_channel, kernel_size=3,padding=1)
    self.bn4 = nn.BatchNorm1d(2 * n_channel)
    self.conv5 = nn.Conv1d(2 * n_channel, 2 * n_channel, kernel_size=3,padding=1)
    self.bn5 = nn.BatchNorm1d(2 * n_channel)
    self.pool3 = nn.MaxPool1d(4)

    self.conv6 = nn.Conv1d(2 * n_channel, 4 * n_channel, kernel_size=3,padding=1)
    self.bn6 = nn.BatchNorm1d(4 * n_channel)
    self.conv7 = nn.Conv1d(4 * n_channel, 4 * n_channel, kernel_size=3,padding=1)
    self.bn7 = nn.BatchNorm1d(4 * n_channel)
    self.conv8 = nn.Conv1d(4 * n_channel, 4 * n_channel, kernel_size=3,padding=1)
    self.bn8 = nn.BatchNorm1d(4 * n_channel)
    self.pool4 = nn.MaxPool1d(4)

    self.conv9 = nn.Conv1d(4 * n_channel, 8 * n_channel, kernel_size=3,padding=1)
    self.bn9 = nn.BatchNorm1d(8 * n_channel)
    self.conv10 = nn.Conv1d(8 * n_channel, 8 * n_channel, kernel_size=3,padding=1)
    self.bn10 = nn.BatchNorm1d(8 * n_channel)

    self.fc1 = nn.Linear(8 * n_channel, n_output)

    print('M11 model')
    print('Model n_input', n_input)
    print('Model n_output', n_output)

  def forward(self, x):
    x = self.conv1(x)
    x = F.relu(self.bn1(x))
    x = self.pool1(x)

    x = self.conv2(x)
    x = F.relu(self.bn2(x))
    x = self.conv3(x)
    x = F.relu(self.bn3(x))
    x = self.pool2(x)

    x = self.conv4(x)
    x = F.relu(self.bn4(x))
    x = self.conv5(x)
    x = F.relu(self.bn5(x))
    x = self.pool3(x)

    x = self.conv6(x)
    x = F.relu(self.bn6(x))
    x = self.conv7(x)
    x = F.relu(self.bn7(x))
    x = self.conv8(x)
    x = F.relu(self.bn8(x))
    x = self.pool4(x)

    x = self.conv9(x)
    x = F.relu(self.bn9(x))
    x = self.conv10(x)
    x = F.relu(self.bn10(x))

    x = F.avg_pool1d(x, x.shape[-1])
    x = x.permute(0, 2, 1)
    x = self.fc1(x)

    return F.log_softmax(x, dim=2)

  def count_parameters(self):
    return sum(p.numel() for p in self.parameters() if p.requires_grad)



# M18 MODEL
class M18(nn.Module):
  def __init__(self, n_input=1, n_output=2, stride=4, n_channel=32):
    super().__init__()
    self.conv1 = nn.Conv1d(n_input, n_channel, kernel_size=80, stride=stride)
    self.bn1 = nn.BatchNorm1d(n_channel)
    self.pool1 = nn.MaxPool1d(4, stride=None)

    self.conv2 = nn.Conv1d(n_channel, n_channel, kernel_size=3,padding=1)
    self.bn2 = nn.BatchNorm1d(n_channel)
    self.conv3 = nn.Conv1d(n_channel, n_channel, kernel_size=3,padding=1)
    self.bn3 = nn.BatchNorm1d(n_channel)
    self.conv4 = nn.Conv1d(n_channel, n_channel, kernel_size=3,padding=1)
    self.bn4 = nn.BatchNorm1d(n_channel)
    self.conv5 = nn.Conv1d(n_channel, n_channel, kernel_size=3,padding=1)
    self.bn5 = nn.BatchNorm1d(n_channel)
    self.pool2 = nn.MaxPool1d(4, stride=None)

    self.conv6 = nn.Conv1d(n_channel, 2 * n_channel, kernel_size=3,padding=1)
    self.bn6 = nn.BatchNorm1d(2 * n_channel)
    self.conv7 = nn.Conv1d(2 * n_channel, 2 * n_channel, kernel_size=3,padding=1)
    self.bn7 = nn.BatchNorm1d(2 * n_channel)
    self.conv8 = nn.Conv1d(2 * n_channel, 2 * n_channel, kernel_size=3,padding=1)
    self.bn8 = nn.BatchNorm1d(2 * n_channel)
    self.conv9 = nn.Conv1d(2 * n_channel, 2 * n_channel, kernel_size=3,padding=1)
    self.bn9 = nn.BatchNorm1d(2 * n_channel)
    self.pool3 = nn.MaxPool1d(4, stride=None)

    self.conv10 = nn.Conv1d(2 * n_channel, 4 * n_channel, kernel_size=3,padding=1)
    self.bn10 = nn.BatchNorm1d(4 * n_channel)
    self.conv11 = nn.Conv1d(4 * n_channel, 4 * n_channel, kernel_size=3,padding=1)
    self.bn11 = nn.BatchNorm1d(4 * n_channel)
    self.conv12 = nn.Conv1d(4 * n_channel, 4 * n_channel, kernel_size=3,padding=1)
    self.bn12 = nn.BatchNorm1d(4 * n_channel)
    self.conv13 = nn.Conv1d(4 * n_channel, 4 * n_channel, kernel_size=3,padding=1)
    self.bn13 = nn.BatchNorm1d(4 * n_channel)
    self.pool4 = nn.MaxPool1d(4, stride=None)

    self.conv14 = nn.Conv1d(4 * n_channel, 8 * n_channel, kernel_size=3,padding=1)
    self.bn14 = nn.BatchNorm1d(8 * n_channel)
    self.conv15 = nn.Conv1d(8 * n_channel, 8 * n_channel, kernel_size=3,padding=1)
    self.bn15 = nn.BatchNorm1d(8 * n_channel)
    self.conv16 = nn.Conv1d(8 * n_channel, 8 * n_channel, kernel_size=3,padding=1)
    self.bn16 = nn.BatchNorm1d(8 * n_channel)
    self.conv17 = nn.Conv1d(8 * n_channel, 8 * n_channel, kernel_size=3,padding=1)
    self.bn17 = nn.BatchNorm1d(8 * n_channel)

    self.fc1 = nn.Linear(8 * n_channel, n_output)

    print('M18 model')
    print('Model n_input', n_input)
    print('Model n_output', n_output)

  def forward(self, x):
      x = self.conv1(x)
      x = F.relu(self.bn1(x))
      x = self.pool1(x)

      x = self.conv2(x)
      x = F.relu(self.bn2(x))
      x = self.conv3(x)
      x = F.relu(self.bn3(x))
      x = self.conv4(x)
      x = F.relu(self.bn4(x))
      x = self.conv5(x)
      x = F.relu(self.bn5(x))
      x = self.pool2(x)

      x = self.conv6(x)
      x = F.relu(self.bn6(x))
      x = self.conv7(x)
      x = F.relu(self.bn7(x))
      x = self.conv8(x)
      x = F.relu(self.bn8(x))
      x = self.conv9(x)
      x = F.relu(self.bn9(x))
      x = self.pool3(x)

      x = self.conv10(x)
      x = F.relu(self.bn10(x))
      x = self.conv11(x)
      x = F.relu(self.bn11(x))
      x = self.conv12(x)
      x = F.relu(self.bn12(x))
      x = self.conv13(x)
      x = F.relu(self.bn13(x))
      x = self.pool4(x)

      x = self.conv14(x)
      x = F.relu(self.bn14(x))
      x = self.conv15(x)
      x = F.relu(self.bn15(x))
      x = self.conv16(x)
      x = F.relu(self.bn16(x))
      x = self.conv17(x)
      x = F.relu(self.bn17(x))

      x = F.avg_pool1d(x, x.shape[-1])
      x = x.permute(0, 2, 1)
      x = self.fc1(x)

      return F.log_softmax(x, dim=2)
  
  def count_parameters(self):
    return sum(p.numel() for p in self.parameters() if p.requires_grad)



