FROM cicirello/alpine-plus-plus:3.18.3

# Set working directory as app
WORKDIR /app

# Setup Curl
RUN apk add --update --no-cache curl

# Setup Python
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

# Setup Git
RUN apk add --update --no-cache git
RUN git config --global init.defaultBranch main

# Copy requirements.txt file from local (source) to file structure of container (destination)
COPY requirements.txt requirements.txt

# Install the requirements specified in file using RUN
RUN pip3 install -r requirements.txt

# Copy all items in current local directory (source) to current container directory (destination)
COPY . .

# Command to run when image is executed inside a container, the entrypoint allows to pass on args
ENTRYPOINT ["python3", "main_init.py"]
