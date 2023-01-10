FROM python:3.9.13
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY ./urls.txt /code/urls.txt
COPY ./model /code/model
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["python", "./app/AppMain.py"]
