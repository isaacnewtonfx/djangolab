# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /src

# Set the working directory to /src
WORKDIR /src

# Copy the current directory contents into the container at /src
ADD . /src/

RUN pip3 install --upgrade pip

RUN pip3 install mod_wsgi-httpd

RUN pip3 install --upgrade pip setuptools wheel

#RUN pip3 install GDAL

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8000
CMD ["/src/start.sh"]