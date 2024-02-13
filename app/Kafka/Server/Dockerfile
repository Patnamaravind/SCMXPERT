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
CMD ["python", "server.py"]
