# Use the Python 3.9.8 base image
FROM python:3.9.8

<<<<<<< HEAD
# Set the working directory inside the container to /DASHBOARD/app/Kafka/Producer/
WORKDIR /DASHBOARD/app/Kafka/Producer/

# Copy the contents of the current directory into the container's workdir
COPY . /DASHBOARD/app/Kafka/Producer/

# Install required Python packages using pip inside the container
RUN pip install python-dotenv confluent_kafka

# Define the default command to execute when the container runs
=======
# Set the working directory inside the container to /DASHBOARD/app/Kafka/Producer/.
WORKDIR /DASHBOARD/app/Kafka/Producer/

# Copy the contents of the current directory into the above mentioned container's workdir.
COPY . /DASHBOARD/app/Kafka/Producer/

# Run the pip install command inside the container to install the specified Python packages.
RUN pip install python-dotenv confluent_kafka

# Whenever the container runs, this default command will be executed.
>>>>>>> master1
CMD ["python", "Producer.py"]
