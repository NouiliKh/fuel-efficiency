<!-- ABOUT THE PROJECT -->
## Fuel efficency app
Convert a ML pipeline defined in a notebook into a robust,
parametrizable Python application with metadata management.

<!-- GETTING STARTED -->
## Getting Started

In this section, I will explain how to get the whole project running on Ubuntu.

### Prerequisites
* docker
  ```sh
    sudo apt install docker docker-compose 
  ```
  
### Installation

1. Clone the repo

2. run docker-entrypoint.sh
   ```sh
   sudo chmod +x start_pp.sh
   ./start_pp.sh
   ```

<!-- USAGE EXAMPLES -->
## Metadata approach explanation
In practice, generally I don't do model metadata or model storing like this. \
I tired to follow the task as much as possible and that's why I did not apply the approach i work with. 
In practice, I use DVC for that kind of thing. DVC allows to do the model versioning control so if I wanted models 
with accuracy higher than a certain threshold I retrieve the branches ( preprocssing and model architecture) that good
result. Thanks to DVC, each model corresponds to a specific branch and the model will be retrieved automatically when 
checking out that branch.