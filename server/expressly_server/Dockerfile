# Use an official Python image as a base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the pyproject.toml and any other build-related files
COPY pyproject.toml .

# Install build tool (hatchling) and project dependencies
RUN pip install --upgrade pip \
    && pip install crewai \
    && crewai install

# Copy the application code into the container
COPY . .

# Expose the port your FastAPI app will run on
EXPOSE 80

# Define the command to run your application
CMD ["uv", "run", "expressly_server"]