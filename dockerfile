# Use a lightweight Python base image
FROM python:3.12-slim

# Set environment variables to ensure Python runs efficiently
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Set the command to run the FastAPI application
CMD ["uvicorn", "api.api:app", "--host", "0.0.0.0", "--port", "8000"]