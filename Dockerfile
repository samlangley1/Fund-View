FROM python:3

ADD ./backend/ /backend/
ADD main.py /
ADD requirements.txt /
ADD ./data /data/


RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]

