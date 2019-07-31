FROM alpine:3.9 as builder
LABEL maintainer "James Wu <contact@analogist.net>"

RUN apk add --no-cache \
        g++ \
        libsodium-dev \
        cmake \
        make \
        git

RUN mkdir -p /usr/src/minisign \
    && git clone --depth 1 https://github.com/jedisct1/minisign /usr/src/minisign \
    && cd /usr/src/minisign \
    && cmake -D BUILD_STATIC_EXECUTABLES=1 . \
    && make

FROM alpine:latest

COPY --from=builder /usr/src/minisign/minisign /usr/bin/minisign
ENV HOME /home/user
RUN adduser -u 1000 -D user && chown -R user:user $HOME

USER user

ENTRYPOINT [ "minisign" ]
