Volume
======

.. _Using volume: https://docs.docker.com/storage/volumes/
.. _Using volumes in Docker Compose: https://devopsheaven.com/docker/docker-compose/volumes/2018/01/16/volumes-in-docker-compose.html

Types of volumes in Docker
--------------------------

There are two types of volume. Every volume is a mount point on the container directory tree to a location on the host directory
tree, but the types differ in where that location is on the host. The first type of volume is a bind mount. Bind mount volumes
use any user-specified directory or file on the host operating system. The second type is a managed volume. Managed volumes use
locations that are created by the Docker daemon in space controlled by the daemon, called Docker managed space.

1. Host-mounted volumes

    *Syntax*: ``/host/path:/container/path``

2. Named volumes

    *Syntax*: ``named_volume_name:/container/path``

    - Defining named volumes

        Using docker command:

        .. code:: shell

            docker volume create --driver local \
                --opt type=none \
                --opt device=/var/opt/my_website/dist \
                --opt o=bind web_data

    - External named volumes

        .. code:: docker-compose

            version '3'

            volumes:
              web_data:
                external: true

            services:
              app:
                image: nginx:alpine
                ports:
                  - 80:80
                volumes:
                  - web_data:/usr/share/nginx/html:ro

    - Internal named volumes

        .. code:: docker-compose

            version '3'

            volumes:
              super_qi_data:
                name: ${VOLUME_ID}

            services:
              app:
                image: super_qi/os
                volumes:
                  - super_qi_data:/usr/share/super_qi/data:ro

        ``${VOLUME_ID}`` can be defined in the ``.env`` file:

        .. code:: shell

            VOLUME_ID=super_qi_os_data

    Shared volumes
    --------------



