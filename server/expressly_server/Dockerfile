# Use an official Python image as a base
FROM python:3.11-slim

RUN useradd -m -u 1000 user
USER user

# Set the working directory inside the container
WORKDIR /app

# Copy the pyproject.toml and any other build-related files
COPY --chown=user pyproject.toml .

# Install build tool (hatchling) and project dependencies
# RUN pip install --upgrade pip \
#     && pip install crewai \
#     && crewai install
RUN pip install --upgrade pip \
    && pip install crewai \
    && export PATH=$PATH:$(python -m site --user-base)/bin \
    && crewai install

# Copy the application code into the container
COPY --chown=user . .

# Expose the port your FastAPI app will run on 7860
EXPOSE 7860 

# Define the command to run your application
CMD ["uv", "run", "expressly_server"]