# Use python base image
FROM python:3.9-slim

# Set working dir
WORKDIR /app

# Copy files
COPY . .

# Default command (optional, can be overridden)
CMD ["python", "app.py"]