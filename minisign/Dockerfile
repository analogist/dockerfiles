FROM alpine:latest as builder
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
    && cmake . -D BUILD_STATIC_EXECUTABLES=1 \
    && make

FROM scratch
COPY --from=builder /usr/src/minisign/minisign /usr/bin/minisign

ENTRYPOINT [ "minisign" ]
