"""Losses & metrics
"""
import torch
import torch.nn as nn
from torch.nn import functional as F


class Loss(nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):
        pass
