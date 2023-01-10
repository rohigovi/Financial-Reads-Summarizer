
# NLP Summarization

The application summarizes articles links provided in an input txt file using the Pegasus language model
that is pretrained on a CNN/Dailymail dataset

The input file urls.txt contains links to long-form financial articles
that need to be summarized.

# To run using docker:

At the root folder(Project2):
Build the docker image:

**docker build -t imagename .**

Then run the docker image:

**docker run imagename**

Get container id for imagename using **docker ps -a**

Then run docker cp to copy output pdf file to your local folder:

**docker cp container_id:/code/summaries.pdf**

This should produce a summaries.pdf in the folder that contains article summaries along with
their urls

# To run using Python Virtual Environment
create a virtual environment with python version 3.9.13

run pip install requirements.txt

run app using **python AppMain.py**