<!-- ABOUT THE PROJECT -->
## Dockerized postgres
In this part of the project, you may find the dockerized version 
of postgres with created database and tables using the create_table.sql file. 

<!-- GETTING STARTED -->
## Getting Started
In this section, I will explain how to get **only** this part of the project running on Ubuntu.

### Prerequisites
* docker
  ```sh
    sudo apt install docker docker-compose 
  ```

### Installation

1. Clone the repo

2. make the starting script executable
   ```sh
  sudo chmod +x docker-entrypoint.sh
   ```
3. run the starting script ( you might want to  add **sudo** if your docker runs with super user privileges)
   ```sh
   ./docker-entrypoint.sh
   ```