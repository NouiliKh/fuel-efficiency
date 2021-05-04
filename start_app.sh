#!/bin/bash
cd postgres/
docker-compose down -v
docker-compose up --build -d

cd ../app/
docker network create --driver bridge my_netw
docker build -t fuel-efficency .
docker run -p 3000:3000 --env-file=.env --network my_network -v /home/$USER/Desktop/here:/output  fuel-efficency
