FROM python:latest
LABEL version="1.0.0"
LABEL maintainer="sathish.msthamby@gmail.com"
ADD my_script.py /
CMD [ "python", "./my_script.py" ]