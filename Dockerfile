# Inherit from this base image, feel free to try newer versions!
FROM python:3.7.6

# Create the user that will run the app (best practice)
RUN adduser --disabled-password --gecos '' ml-api-user

# Specify a working dir where the commands will run
WORKDIR /opt/titanic-survival-api

# Copy the api dir to the working dir
ADD ./titanic-api /opt/titanic-survival-api

# Install requirements
RUN pip install --upgrade pip
RUN pip install -r /opt/titanic-survival-api/requirements.txt

# To make sure we have permissions to run the bash script
# This bash script uses the uvicorn command
RUN chmod +x /opt/titanic-survival-api/run.sh
# Make sure our user owns the dir
RUN chown -R ml-api-user:ml-api-user ./

# Set the user so we're ready to go
USER ml-api-user

# Expose the port so unicorn runs nicely and port 8001 is accessible on the container
EXPOSE 8001

# Here we run the bash script that runs unicorn and start up our FastAPI app
CMD ["bash", "./run.sh"]
