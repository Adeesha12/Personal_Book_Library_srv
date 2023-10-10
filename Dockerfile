# Use the official Python image as the base image
FROM python:3.9-buster

# make working directory in the container
RUN mkdir -p /solution


# Copy the requirements.txt and .env file to the container
COPY requirements.txt /solution
COPY .env /solution

# Install dependencies
RUN pip install --no-cache-dir -r solution/requirements.txt

# Copy the FastAPI app files to the container
COPY app /solution/app
RUN find /solution/app -type d -name "__pycache__" -exec rm -rf {} +

# set working directory in the container
WORKDIR /solution/app

# Expose the port that FastAPI will run on
EXPOSE 8000

# Start the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
