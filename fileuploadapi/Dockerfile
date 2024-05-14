# Use the official Python image as a base
FROM python:3.9-slim

# Install system-level dependencies
RUN apt-get update && apt-get install -y libmariadb-dev-compat pkg-config gcc

# Set the working directory in the container
WORKDIR /app

# Copy the contents of your current directory to the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your application runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
