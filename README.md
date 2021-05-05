<!-- ABOUT THE PROJECT -->
## Fuel efficency app
Convert a ML pipeline defined in a notebook into a robust,
parametrizable Python application with metadata management.

<!-- GETTING STARTED -->
## Getting Started

In this section, I will explain how to get the whole project running on Ubuntu.

### Prerequisites
* docker\
  Install docker using this guide: https://docs.docker.com/engine/install/ubuntu/
  ```sh
    sudo apt install docker-compose 
  ```
  
### Installation

1. Clone the repo

2. make the starting script executable
   ```sh
   sudo chmod +x start_pp.sh
   ```
3. run the starting script ( you might want to  add **sudo** if your docker runs with super user privileges)
   ```sh
   ./start_pp.sh
   ```
   

<!-- USAGE EXAMPLES -->
## Metadata approach explanation
In practice, generally I don't do model metadata or model storing like this. \
I tired to follow the task as much as possible and that's why I did not apply the approach I work with. 
In practice, I use DVC for that kind of things. DVC allows me to do the model versioning control so if I wanted models 
with accuracy higher than a certain threshold I retrieve the branches (preprocessing and model architecture) that meets
that condition.\
Thanks to DVC, each model corresponds to a specific branch, and the model will be retrieved automatically (from a cloud storage
such as amazon s3 ) when checking out that branch.\
In machine learning engineering we try multiple combinations and if tracking the results of these combinations if beneficial.

<!-- USAGE -->
## Description

### Evaluation
After training the model and evaluating with training set, I saved information about the loss, 
validation_loss and execution time by creating a custom callback with tensorflow. Then I plotted these results using 
matplotlib. You may find these plots on your Desktop inside **plots** folder.\

### Tests
I implemented a simple unit test in test.py file which allows to test the preprocessing class: whether the number of rows
of training features and training label matches, and the number of rows of testing features and testing label matches as
well.
![unit test](images/unit_test.png)

### Note
Actually the archive.ics.uci.edu/ml/ got down for a couple of days which slowed my progress. It is still down until now
and for that reason I chose to download the data from a **mirror** domain: https://data.world/uci.
![domain down](images/domain_down.png)
