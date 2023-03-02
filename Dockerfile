# pull the official base image
FROM python:3.8.3

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
COPY ./ /app/
WORKDIR /app/

# install dependencies
RUN pip install --upgrade pip 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


EXPOSE 8049

CMD ["python", "/app/hamgam/hamgam_backend/manage.py", "runserver", "0.0.0.0:8049"]

