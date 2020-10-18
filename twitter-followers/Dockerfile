FROM alpine:latest
LABEL maintainer "James Wu <contact@analogist.net>"

RUN apk update && apk upgrade
RUN apk add --no-cache python3
RUN python3 -m ensurepip
RUN pip3 install --upgrade pip && pip3 install python-twitter

COPY twitter-followers.py /opt/twitter-followers.py

ENTRYPOINT [ "python3", "/opt/twitter-followers.py" ]
