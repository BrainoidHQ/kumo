ARG VARIANT=bullseye
FROM mcr.microsoft.com/devcontainers/base:${VARIANT}

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
        pkg-config build-essential cmake libssl-dev

RUN . /etc/os-release \
    && curl -sSL "https://aquasecurity.github.io/trivy-repo/deb/public.key" | gpg --dearmor > /usr/share/keyrings/trivy.gpg \
    && echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/trivy.list \
    && apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y trivy \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*
