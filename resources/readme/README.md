
## **About The Project**

**TODO - Add Project Description**
</br>


### **Built With**
**TODO - Add used technology badges**

[![Python 3.10][Python]][Python-url]

</br>


## **Getting Started**


### **Local Copy Setup and Usage**
To get a local copy up and running follow these simple steps.

#### **Prerequisites**

**TODO - Add Prerequisites**

* **Python 3.11.x** - It is either installed on your Linux distribution or on other Operating Systems you can get it from the [Official Website](Python-url), [Microsoft Store](https://apps.microsoft.com/store/detail/python-311/9NRWMJP3717K?hl=en-us&gl=us) or through `Windows Subsystem for Linux (WSL)` using this [article](https://medium.com/@rhdzmota/python-development-on-the-windows-subsystem-for-linux-wsl-17a0fa1839d).



#### **Setup Steps**

**TODO - Add Setup Steps**

1. Clone the repo and navigate to the Project folder
   ```sh
   git clone https://github.com/<user>/<repo>
   ```

2. Create a new Python Virtual Environment
   ```sh
   python -m venv venv
   ```

3. Activate the Virtual Environment

    On Linux:
    ```sh
    source ./venv/bin/activate
    ```

    On Windows:
    ```sh
    .\venv\Scripts\Activate.ps1
    ```

4. Install Project dependencies

    ```sh
    pip install -r requirements.txt
    ```

5. Run main script (with prepared use-cases)
    ```sh
    python main.py
    ```

</br>

### Docker Container
To get a Dockerized version of the app up and running follow these simple steps.

#### Building the image locally

1. Clone the repo and navigate to the Project folder
   ```sh
   git clone https://github.com/<user>/<repo>
   ```

2. Build the Docker Image
   ```sh
   docker build -t <docker_image_tag> .
   ```

3. Run the container based on the new Docker Image
    ```sh
    docker run --rm -it --name <docker_image_container> <docker_image_tag>
    ```


#### Pulling image from Docker Hub

1. Run the container based on Docker Image from Docker Hub
   ```sh
   docker run --rm -it --name <docker_image_container> <dockerhub_username>/<docker_image_tag>:latest
   ```

</br>

## **License**

Distributed under the **[TODO - License]**. See [LICENSE](https://github.com/<user>/<repo>/blob/main/LICENSE) for more information.

</br>

## **Acknowledgments**
[Acknowledgment #1](#)

<!-- Variables -->

[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
