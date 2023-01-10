# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 16:11:06 2023

@author: rohig
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch
import LoadModel
import os.path
from LoadModel import LoadModel
from Summarizer import Summarizer
from mdutils.mdutils import MdUtils
from mdutils import Html

def generatePDF(merge_texts):
    mdFile = MdUtils(file_name='summaries_md', title='Article Summaries')
    for i in range(len(merge_texts)):
        mdFile.new_header(level=2, title=urls[i],add_table_of_contents="n")  # style is set 'atx' format by default.
        mdFile.new_paragraph(merge_texts[i].replace('<n>',''))
        mdFile.new_paragraph()

    mdFile.create_md_file()
    os.system("mdpdf -o summaries.pdf summaries_md.md")

merge_texts = []
#Test url
model_name = "google/pegasus-cnn_dailymail"
urls = []
with open('urls.txt') as file:
    for line in file:
        urls.append(line.strip())
print(urls)
model = LoadModel("google/pegasus-cnn_dailymail")
if os.path.exists('model'):
    print("exists")
else:
    model.saveModel()        
model = model.getModel()
tokenizer = PegasusTokenizer.from_pretrained(model_name)
for url in urls[0:5]:    
    summarizer = Summarizer(url)
    text = summarizer.scrape()
    merge_text = summarizer.summarize(text,model,tokenizer)
    merge_texts.append(merge_text[0])
    print(merge_text[0])
generatePDF(merge_texts)