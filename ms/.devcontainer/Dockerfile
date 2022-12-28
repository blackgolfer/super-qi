FROM mcr.microsoft.com/devcontainers/python:0-3.11

ARG USERNAME
ARG USER_GID
ARG USER_UID
USER root

# Create the user
# Copy the .env file to the container
COPY .env /tmp/.env
# Source to use it
SHELL ["/bin/bash", "-c"]
RUN source /tmp/.env && rm /tmp/.env \
    && if getent passwd $USERNAME; then userdel -f $USERNAME; fi \
    && if getent group $GROUPNAME; then groupdel $GROUPNAME; fi \
    && groupadd -f -g "${USER_GID}" "${GROUPNAME}" \
    && useradd --create-home --no-log-init -u "${USER_UID}" -g "${USER_GID}" "${USERNAME}" \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# [Optional] Set the default user. Omit if you want to keep the default as root.

COPY requirements.txt /tmp/pip-tmp/
RUN pip3 install --upgrade pip
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp
RUN pip3 install jupyter-book

USER $USERNAME
WORKDIR /home/$USERNAME
