# Pretty Handy, Init?

**Pretty Handy, Init?** is a command-line tool that simplifies the process of setting up a new programming project. It automates the creation of a standardized project structure, complete with necessary files and directories, making it easier for developers to start coding without spending time on repetitive setup tasks.
</br>


### **Built With**
[![Python 3.10][Python]][Python-url]
[![Docker][Docker]][Docker-url]

</br>


## **Getting Started**


### **Local Copy Setup and Usage**
To get a local copy up and running follow these simple steps.

#### **Prerequisites**

* **Docker** - To execute this project it is recommended to run it in a more convenient Dockerized environment. For this purpose [**Docker**](https://www.docker.com/) or [**Docker Desktop**](https://www.docker.com/products/docker-desktop/) is recommended. The following product can be downloaded from their website or installed through a package manager.

#### **Setup Steps**

#### Building the image locally

1. Clone the repo and navigate to the Project folder
   ```sh
   git clone https://github.com/Raychani1/Pretty_Handy_Init
   ```

2. Build the Docker Image
   ```sh
   docker build -t init .
   ```

3. Run the container based on the new Docker Image, where [**GIT_ENV**](https://github.com/Raychani1/Pretty_Handy_Init/blob/main/example_env/example_git.env) and [**DOCKERHUB_ENV**](https://github.com/Raychani1/Pretty_Handy_Init/blob/main/example_env/example_dockerhub.env) are variables containing the path to GitHub and DockerHub Credentials. See examples in the [**example_env**](https://github.com/Raychani1/Pretty_Handy_Init/blob/main/example_env/) folder.

    On Linux:
    ```sh
    GIT_ENV="<PATH-TO-PROJECT>/example_env/example_git.env"
	DOCKERHUB_ENV="<PATH-TO-PROJECT>/example_env/example_dockerhub.env"

    docker run --rm -it --name init_container -v "$(pwd)":/app/init_dir --env-file "$GIT_ENV" --env-file "$DOCKERHUB_ENV" init
    ```

    On Windows:
    ```sh
    $GIT_ENV="<PATH-TO-PROJECT>\\example_env\\example_git.env"
	$DOCKERHUB_ENV="<PATH-TO-PROJECT>\\example_env\\example_dockerhub.env"

    docker run --rm -it --name init_container -v ${pwd}:/app/init_dir --env-file $GIT_ENV --env-file $DOCKERHUB_ENV init
    ```

#### Pulling image from Docker Hub

Run the container based on Docker Image from Docker Hub

On Linux:
```sh
GIT_ENV="<PATH-TO-PROJECT>/example_env/example_git.env"
DOCKERHUB_ENV="<PATH-TO-PROJECT>/example_env/example_dockerhub.env"

docker run --rm -it --name init_container -v "$(pwd)":/app/init_dir --env-file "$GIT_ENV" --env-file "$DOCKERHUB_ENV" rajcsanyiladislavit/pretty_handy_init:latest
```

On Windows:
```sh
$GIT_ENV="<PATH-TO-PROJECT>\\example_env\\example_git.env"
$DOCKERHUB_ENV="<PATH-TO-PROJECT>\\example_env\\example_dockerhub.env"

docker run --rm -it --name init_container -v ${pwd}:/app/init_dir --env-file $GIT_ENV --env-file $DOCKERHUB_ENV rajcsanyiladislavit/pretty_handy_init:latest
```

</br>

#### Terminal integration
Files [**example_pretty_handy_init.sh**](https://github.com/Raychani1/Pretty_Handy_Init/blob/main/example_pretty_handy_init.sh) and [**example_pretty_handy_init.ps1**](https://github.com/Raychani1/Pretty_Handy_Init/blob/main/example_pretty_handy_init.ps1) contain a simple function which after modification and loading to the terminal using the `source` (Linux) command or the `dot notation` (Windows) can be used anywhere in the system.


## **License**

Distributed under the **MIT License**. See [LICENSE](https://github.com/Raychani1/Pretty_Handy_Init/blob/main/LICENSE) for more information.

<!-- Variables -->

[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/

[Docker]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
