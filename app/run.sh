#!/bin/bash
docker network create --driver bridge my_network
docker build -t fuel-efficency .
docker run -p 3000:3000 --network my_network fuel-efficency
