FROM ubuntu:18.04

RUN apt update
RUN apt -y install python3 python3-pip
RUN apt -y install unixodbc-dev
RUN apt -y install libsm6
RUN apt -y install libfontconfig1 libxrender1
RUN apt -y install libxext6


RUN mkdir /server
COPY tracking_project /server
WORKDIR /server
RUN pip3 install -r requirements.txt
RUN libxext6

