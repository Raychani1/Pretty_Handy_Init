FROM python:3.8-slim-buster

# Set working directory as app
WORKDIR /app

# Copy requirements.txt file from local (source) to file structure of container (destination)
COPY requirements.txt requirements.txt

# Install the requirements specified in file using RUN
RUN pip3 install -r requirements.txt

# Copy all items in current local directory (source) to current container directory (destination)
COPY . .

# Command to run when image is executed inside a container
CMD [ "python3", "main.py"]
