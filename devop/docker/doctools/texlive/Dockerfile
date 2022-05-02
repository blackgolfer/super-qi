ARG REGISTRY
FROM $REGISTRY/doctools:plantuml

ARG USER
ARG GROUP
ARG GROUPID
ARG USERID

#RUN apt-get install -y perl wget

# COPY texlive.profile /
# RUN wget ftp://tug.org/historic/systems/texlive/2019/install-tl-unx.tar.gz \
#   && tar xzvf install-tl-unx.tar.gz \
#   && ./install-tl-*/install-tl -profile texlive.profile \
#   && rm -rf install-tl-* \
#   && rm texlive.profile

# ENV PATH="/usr/local/texlive/2019/bin/x86_64-linuxmusl:${PATH}"

ENV DEBIAN_FRONTEND noninteractive
RUN dpkg-reconfigure debconf --frontend=noninteractive

RUN apt-get update -y && apt-get install -y \
        latexmk \
        lmodern \
        texlive-latex-recommended \
        texlive-latex-extra \
        texlive-fonts-recommended \
        texlive-lang-cjk \
        texlive-luatex \
        texlive-xetex

RUN apt-get install -y texlive-pictures

RUN apt-get install -y \
    pdf2svg \
    poppler-utils \
    netpbm \
    poppler-utils  \
    ghostscript
RUN apt update && apt install -y \
    gnuplot
RUN apt-get install -y \
    dvipng

RUN apt-get -y autoremove \
    && apt-get -y clean

#RUN groupadd -f -r -g $GROUPID $GROUP && useradd -r -g $GROUPID -u $USERID -m $USER
USER $USER
WORKDIR /home/$USER