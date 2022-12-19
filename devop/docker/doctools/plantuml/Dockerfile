ARG REGISTRY
FROM $REGISTRY/progtools:python

ARG USER
ARG GROUP

USER root
WORKDIR /root

ENV DEBIAN_FRONTEND noninteractive
RUN dpkg-reconfigure debconf --frontend=noninteractive

RUN apt update
RUN apt-get update -y
# jre
RUN apt-get install -y openjdk-11-jre-headless
RUN apt-get install -y wget ca-certificates

# PlantUML
RUN mkdir /opt/plantuml
RUN wget https://netcologne.dl.sourceforge.net/project/plantuml/plantuml.jar -q --output-document=/opt/plantuml/plantuml.jar
ENV PLANTUML_JAR=/opt/plantuml/plantuml.jar

RUN apt-get install -y \
    graphviz \
    imagemagick \
    make