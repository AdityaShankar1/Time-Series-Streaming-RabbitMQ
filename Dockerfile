# Use lightweight Python base image
FROM python:3.14-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flask pandas matplotlib pytest pymongo pika

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
