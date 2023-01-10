# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 19:55:21 2023

@author: rohig
"""
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch
import pickle
class LoadModel:
    def __init__(self, model_name):
        self.model_name = model_name
    def LoadModel(self, model_name):
        self.model_name = model_name
        
    def saveModel(self):
        print('Downloading and saving model')
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        model = PegasusForConditionalGeneration.from_pretrained(self.model_name).to(device)
        pickle.dump(model, open('model', 'wb'))
            
    def getModel(self):
        print('loading model')
        loaded_model = pickle.load(open('model', 'rb'))
        return loaded_model           