ARG REGISTRY
FROM $REGISTRY/doctools:plantuml

ARG USER
ARG GROUP
ARG GROUPID
ARG USERID

## ----------------------------------------------------------------
## Add venv
## ----------------------------------------------------------------
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

ADD requirements.txt ./
RUN python3 -m pip install -U pip
RUN pip3 install Sphinx Pillow -U
RUN pip3 install -r requirements.txt -U

#RUN groupadd -f -r -g $GROUPID $GROUP && useradd -r -g $GROUPID -u $USERID -m $USER
USER $USER
WORKDIR /home/$USER