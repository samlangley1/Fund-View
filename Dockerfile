FROM python:3

ADD ./ /

RUN pip install requests
RUN pip install pandas

CMD [ "python", "./main.py" ]

