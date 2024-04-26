FROM python:3.10-slim-buster

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

RUN \
  apt-get update \
  && apt-get install -y \
      apt-utils \
      gcc wget telnet \
      curl make \
      build-essential \
      cmake \
      pkg-config \
      iputils-ping \
      net-tools  \
      libcurl4-openssl-dev libssl-dev freetds-dev libkrb5-dev \
      unzip xdg-utils libpq-dev groff less \
    && rm -rf /var/lib/apt/lists/*

# Copy the dependencies file to the working directory
COPY cookbook/requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

#copy the project
COPY . .

#expost port to be able to access from browser
EXPOSE 8000
