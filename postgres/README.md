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

2. run docker-entrypoint.sh
   ```sh
   sudo chmod +x docker-entrypoint.sh
   ./docker-entrypoint.sh
   ```