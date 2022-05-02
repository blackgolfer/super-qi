==================
Postgresql Service
==================

`Monitoring PostgreSQL with Prometheus + grafana in docker environment<https://developpaper.com/monitoring-postgresql-with-prometheus-grafana-in-docker-environment/>`_

Environmental preparation
=========================

.. code:: shell
    $ git clone https://github.com/docker-composes/postgres.git
    $ git clone https://github.com/docker-composes/grafana.git
    $ git clone https://github.com/docker-composes/prometheus.git

Container configuration
=======================

Postgres exporter configuration
-------------------------------

In ``postgres/exporter/docker-compose.yml``, 

1. Database connection information: set the Postgres database connection information to ``DATA_SOURCE_NAME`` environment variable.

2. Network: set ``networks`` to local_net (communicating with other containers)


In ``prometheus/singleton/config/prometheus.yml``

Start services
==============

.. code:: shell

    $ docker network create local-net
    $ cd grafana && docker-compose up -d 
    $ cd ..
    $ cd prometheus/singleton && docker-compose up -d 
    $ cd ../..
    $ cd postgres/signleton && docker-compose up -d
    $ cd ../..
    $ cd postgres/exporter && docker-compose up -d