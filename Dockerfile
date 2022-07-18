FROM python:3.7.6

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /opt/titanic-survival-api

# Install requirements
ADD ./titanic-api /opt/titanic-survival-api
RUN pip install --upgrade pip
RUN pip install -r /opt/titanic-survival-api/requirements.txt

RUN chmod +x /opt/titanic-survival-api/run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 8001

CMD ["bash", "./run.sh"]
