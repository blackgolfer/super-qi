FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update -y && apt upgrade -y
RUN apt-get update && apt-get upgrade -y
RUN apt-get install apt-utils \
        vim \
        git \
        curl \
        wget \
    ; \
	apt-get clean && rm -rf /var/lib/apt/lists/*

