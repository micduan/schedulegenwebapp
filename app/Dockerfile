FROM python:2.7
ADD . /web
WORKDIR /web
RUN pip install -r requirements.txt
RUN python -V
CMD python main.py
