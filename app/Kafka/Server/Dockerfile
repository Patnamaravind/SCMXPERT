<<<<<<< HEAD
# Fetch the image of Python 3.9.8 from Docker Hub
FROM python:3.9.8

# Set the working directory inside the container to /DASHBOARD/app/Kafka/Server/
WORKDIR /DASHBOARD/app/Kafka/Server/

# Copy the contents of the current directory into the container's workdir
COPY . /DASHBOARD/app/Kafka/Server/

# Install required Python packages using pip inside the container
RUN pip install python-dotenv

# Expose port 12345 to allow communication with the container
EXPOSE 12345

# Define the default command to execute when the container runs
=======
# Fetches the image of Python 3.11.4 from the Docker Hub
FROM python:3.9.8

# Set the working directory inside the container to /DASHBOARD/app/Kafka/Server/.
WORKDIR /DASHBOARD/app/Kafka/Server/

# Copy the contents of the current directory into the above mentioned container's workdir.
COPY . /DASHBOARD/app/Kafka/Server/

# Run the pip install command inside the container to install the specified Python packages.
RUN pip install python-dotenv

# Expose port 12345 to allow communication to/from the container.
EXPOSE 12345

# Whenever the container runs, this default command will be executed.
>>>>>>> master1
CMD ["python", "server.py"]
