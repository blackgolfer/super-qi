Performance Testing
===================

`Comparing TimescaleDB and QuestDB timeseries databases`_
---------------------------------------------------------

.. _Comparing TimescaleDB and QuestDB timeseries databases: https://questdb.io/tutorial/2021/08/18/questdb-versus-timescaledb/

For traditional databases like MySQL and PostgreSQL, many popular options like HammerDB_ and sysbench_ are standard tools
to measure database read and write performance. Similar tools exist for different types of databases. Performance testing
makes sense when the benchmarking tool simulates real-life scenarios by creating realistic bursts and reading streams.

.. _HammerDB: https://hammerdb.com/
.. _sysbench: https://github.com/akopytov/sysbench

The access and usage pattern for timeseries databases is very different from a traditional database — that is why we need a tool
like ``TSBS``. ``TSBS`` currently supports two kinds of loads:


Using the TSBS to test time series database performance
-------------------------------------------------------

Setting up tools
++++++++++++++++

To get started with the TSBS suite, clone the repository and prepare the tool:

.. code:: shell

    # TSBS - create a temporary directory for the Go binaries
    cd projects/topics/data/tsdb/performace/tests
    mkdir -p $(pwd)/go/src/github.com/timescale/
    cd go/src/github.com/timescale/

    # Clone the TSBS repository, build test and install Go binaries:
    git clone git@github.com:questdb/tsbs.git
    cd tsbs && git checkout questdb-tsbs-load-new
    cd ../../../..
    GOPATH=$(pwd)
    cd src/github.com/timescale/tsbs
    go get github.com/tklauser/go-sysconf@v0.3.5
    go build -v ./...
    go test -v github.com/timescale/tsbs/cmd/tsbs_load_questdb
    go install -v ./...
    cd ../../../..

Start databases
+++++++++++++++

Once all the suite is installed, QuestDB and TimescaleDB can be started:

.. code:: shell

    docker run -d --name questdb -p 9000:9000 -p 9009:9009 questdb/questdb
    docker run -d --name timescaledb -p 5432:5432 -e POSTGRES_PASSWORD=password \
        timescale/timescaledb:latest-pg14


Generate test data for benchmarking
+++++++++++++++++++++++++++++++++++

Run the following command to generate data for QuestDB:

.. code:: shell

    PATH=~/go/bin:$PATH
    tsbs_generate_data \
        --use-case="devops" --seed=123 --scale=200 \
        --timestamp-start="2016-01-01T00:00:00Z" \
        --timestamp-end="2016-01-02T00:00:00Z" \
        --log-interval="10s" --format="influx" > /tmp/questdb-data

Run the following command to generate data for TimescaleDB:

.. code:: shell

    tsbs_generate_data \
        --use-case="devops" --seed=123 --scale=200 \
        --timestamp-start="2016-01-01T00:00:00Z" \
        --timestamp-end="2016-01-02T00:00:00Z" \
        --log-interval="10s" --format="timescaledb" > /tmp/timescaledb-data