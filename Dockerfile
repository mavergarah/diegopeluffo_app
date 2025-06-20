FROM python:3.9.6
ARG DJANGO_ENV

# Add requirements to the image.
ADD requirements /app/requirements

# Asign work directory.
WORKDIR /app/

# Install Python requirements.
RUN pip install --upgrade pip; \
	pip install -r requirements/$DJANGO_ENV.txt

# Create user without privilegies.
RUN adduser --disabled-password --gecos '' app

ENV HOME /home/app
