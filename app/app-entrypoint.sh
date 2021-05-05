cp .env.template .env
docker network create --driver bridge my_network
docker build -t fuel-efficency .
docker run -p 3000:3000 --env-file=.env --network my_network -v $(pwd)/../plots:/output  fuel-efficency