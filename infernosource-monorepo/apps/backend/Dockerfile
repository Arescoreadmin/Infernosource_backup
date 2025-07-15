# Use a lightweight Python base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Environment variables to disable bytecode and enable logs to stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Command to run the FastAPI app with auto-reload
CMD ["uvicorn", "apps.backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
