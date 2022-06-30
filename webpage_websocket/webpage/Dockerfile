FROM python:3.6
WORKDIR /code
RUN apt-get install tzdata\
    && cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./startup.sh /startup.sh
