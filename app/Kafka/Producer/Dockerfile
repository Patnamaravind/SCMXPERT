# Use the Python 3.9.8 base image
FROM python:3.9.8

# Set the working directory inside the container to /DASHBOARD/app/Kafka/Producer/
WORKDIR /DASHBOARD/app/Kafka/Producer/

# Copy the contents of the current directory into the container's workdir
COPY . /DASHBOARD/app/Kafka/Producer/

# Install required Python packages using pip inside the container
RUN pip install python-dotenv confluent_kafka

# Define the default command to execute when the container runs
CMD ["python", "Producer.py"]
