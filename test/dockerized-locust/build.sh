#!/bin/bash

cp Dockerfile locustfile.py locust/
cd locust/

docker build -t caixiangfan/locust:latest .