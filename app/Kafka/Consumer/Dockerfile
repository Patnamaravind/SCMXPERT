# Use the Python 3.9.8 base image
FROM python:3.9.8

# Set the working directory inside the container to /DASHBOARD/app/Kafka/Consumer/
WORKDIR /DASHBOARD/app/Kafka/Consumer/

# Copy the contents of the current directory into the container's workdir
COPY . /DASHBOARD/app/Kafka/Consumer/

# Install required Python packages using pip inside the container
RUN pip install python-dotenv confluent_kafka pymongo

# Define the default command to execute when the container runs
CMD ["python", "Consumer.py"]
