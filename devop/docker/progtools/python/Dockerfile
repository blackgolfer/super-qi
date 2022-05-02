ARG REGISTRY
FROM $REGISTRY/os as builder

ARG USER
ARG GROUP
ARG USERID
ARG GROUPID

# ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

ENV TZ=Asia/Shanghai \
    DEBIAN_FRONTEND=noninteractive

# runtime dependencies
RUN set -eux; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		libbluetooth-dev \
		tk-dev \
		uuid-dev \
        python3 \
        python3-pip \
        python3-dev \
        python3-venv \
		python3-wheel \
		build-essential\
	; \
	apt-get clean && rm -rf /var/lib/apt/lists/*

# create and activate virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# install requirements
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

FROM $REGISTRY/os as runner

ARG USER
ARG GROUP
ARG USERID
ARG GROUPID

RUN apt-get update && apt-get install --no-install-recommends -y python3 python3-venv && \
   apt-get clean && rm -rf /var/lib/apt/lists/*

RUN groupadd -f -g $GROUPID $GROUP && useradd -g $GROUPID -u $USERID -m $USER

COPY --from=builder /opt/venv /home/$USER/venv

# activate virtual environment
ENV VIRTUAL_ENV=/home/$USER/venv
ENV PATH="/home/$USER/venv/bin:$PATH"

USER $USER
WORKDIR /home/$USER

CMD [ "python3" ]
