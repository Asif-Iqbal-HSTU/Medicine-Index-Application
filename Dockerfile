FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Create and activate virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy application code
COPY . /app/

# Set working directory
WORKDIR /app

# Collect static files
RUN python manage.py collectstatic --noinput --clear

# Command to run the application
CMD ["gunicorn", "--config", "gunicorn.conf.py", "medicine_index.wsgi:application"]
