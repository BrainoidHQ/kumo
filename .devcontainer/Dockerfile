ARG VARIANT=bullseye
FROM mcr.microsoft.com/devcontainers/base:${VARIANT}

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
        pkg-config build-essential cmake libssl-dev