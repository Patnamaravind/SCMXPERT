<<<<<<< HEAD
# Use the Python 3.9.8 base image
=======
# Set the base image to use for this Dockerfile
>>>>>>> master1
FROM python:3.9.8

# Set the working directory inside the container to /DASHBOARD/app/Kafka/Consumer/
WORKDIR /DASHBOARD/app/Kafka/Consumer/

<<<<<<< HEAD
# Copy the contents of the current directory into the container's workdir
COPY . /DASHBOARD/app/Kafka/Consumer/

# Install required Python packages using pip inside the container
RUN pip install python-dotenv confluent_kafka pymongo

# Define the default command to execute when the container runs
=======
# Copy the contents of the current directory into the container's /DASHBOARD/app/Kafka/Consumer/ directory
COPY . /DASHBOARD/app/Kafka/Consumer/

# Install Python dependencies using pip inside the container
RUN pip install python-dotenv confluent_kafka pymongo

# Define the default command to be executed when the container starts
>>>>>>> master1
CMD ["python", "Consumer.py"]

