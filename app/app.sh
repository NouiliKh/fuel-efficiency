#!/bin/bash
docker build -t fuel-efficency .
docker run -p 3000:3000 --env-file=.env --network my_network -v /home/$USER/Desktop/here:/output  fuel-efficency
