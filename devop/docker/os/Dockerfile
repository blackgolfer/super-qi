FROM ubuntu:23.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update -y && apt upgrade -y
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y \
        apt-utils \
        vim \
        git \
        curl \
        wget \
        pandoc \
    ; \
	apt-get clean && rm -rf /var/lib/apt/lists/*

