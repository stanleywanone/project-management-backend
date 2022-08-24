#Tells Docker to use the official python 3 image from dockerhub as a base image
FROM python:3.9
# Sets an environmental variable that ensures output from python is sent straight to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1
# Sets the container's working directory to /project-management-backend
WORKDIR /project-management-backend

COPY requirements.txt .
# Copies all files from our local project into the container

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver" , "0.0.0.0:8000"]
