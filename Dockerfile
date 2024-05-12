# syntax=docker/dockerfile:1

# ARG mode

FROM python:3.12

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# RUN chmod u+x ./run.py

# CMD ./start.sh $mode
CMD [ "python", "run.py" ]
# CMD [ "echo", "hello" ]
# uncomment to build debug mode