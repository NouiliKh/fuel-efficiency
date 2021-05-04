sudo docker network create --driver bridge my_network
sudo  docker build -t fuel-efficency .
sudo  docker run -p 3000:3000 --network my_network fuel-efficency
