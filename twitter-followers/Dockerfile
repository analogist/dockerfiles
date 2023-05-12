FROM alpine:latest
LABEL maintainer "James Wu <contact@analogist.net>"

# docker run --rm -e TWITTER_CONSUMER_KEY -e TWITTER_CONSUMER_SECRET -e TWITTER_ACCESS_KEY -e TWITTER_ACCESS_SECRET -e TWITTER_FETCH_HANDLE analogist/twitter-followers > ${HOME}/twitter/twitter-$(date "+\%Y-\%m-\%d").tsv

RUN apk update && apk upgrade
RUN apk add --no-cache python3
RUN python3 -m ensurepip
RUN pip3 install --upgrade pip && pip3 install python-twitter

COPY twitter-followers.py /opt/twitter-followers.py

ENTRYPOINT [ "python3", "/opt/twitter-followers.py" ]
