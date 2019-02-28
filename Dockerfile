FROM ubuntu:16.04
MAINTAINER Anastasia Haswani <my website>

RUN apt-get update

RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install numpy pandas matplotlib 
#RUN pip3 install -U wxPython
#RUN pip3 install -U \
#    -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-16.04/ \
#    wxPython
RUN cat /etc/lsb-release

RUN mkdir -p /app/

COPY ./analyse.py /app/
COPY ./wdbc.data /app/
COPY ./test_noheader.txt /app/
COPY ./header_5.txt /app/

WORKDIR /app
#ENV name test_noheader.txt
#ENV header header_5.txt
ENTRYPOINT ["python3","./analyse.py"]
CMD ["wdbc.data"]




