FROM alpine:latest
LABEL maintainer "James Wu <contact@analogist.net>"

RUN apk add --no-cache \
        nethack

USER games
COPY znode.nh366rc /usr/games/.nethackrc

ENTRYPOINT [ "nethack" ]
