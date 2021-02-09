# Base Image
FROM python:slim-buster
# create and set working directory
#RUN mkdir /app
#WORKDIR /app

# Add current directory code to working directory
ADD . /

# set default environment variables
#ENV PYTHONUNBUFFERED 1
#ENV LANG C.UTF-8
#ENV DEBIAN_FRONTEND=noninteractive

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here
ENV PORT=8089



# RUN pip3 install opencv-contrib-python
WORKDIR /samples
EXPOSE 8089

CMD ["python", "flatbuffer_simulator.py"]
