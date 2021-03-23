## About

This repository is to test the private tangle with Docker-compose and Docker swarm.

The code is composed of:

- **`docker-compose.yml`:** docker-compose file to run master and worker nodes on the same machine. 
- **`docker-swarm.yml`:** docker-compose file to run master and worker nodes in a Docker swarm on different machines.
- **`Dockerfile`:** Dockerfile used to build the image with customized locust file.
- **`locustfile.py`:** customized locust file defines test User classes and tasks.


## Prerequisites
First, to run this test you need to create a private tangle using one-click-tangle or any other repo.
Then, open the following network ports for swarm management:

- TCP port `2377` for cluster management communications
- TCP and UDP port `7946` for communication among nodes
- UDP port `4789` for overlay network traffic

## Getting started

First you need to clone this repository and the official [locust](https://github.com/locustio/locust.git) repository as submodule

```
git clone --recurse-submodules https://github.com/CaixiangFan/one-click-tangle.git
```

Then replace the original Dockerfile with the customized one and copy locustfile.py to the locust directory

```
cp Dockerfile locustfile.py locust/ && cd locust/
```

Afterwards you can build the locust image and push it to your docker hub by

```
docker build -t repo/name:tag .
docker login
docker push repo/name:tag
```

## Usage examples

For docker run:

    docker run -p 8089:8089 caixiangfan/locust:1.0

For docker-compose:

    docker-compose up --scale worker=8

For docker swarm:

    docker stack deploy --compose-file docker-swarm.yml locusts

