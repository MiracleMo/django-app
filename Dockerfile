# syntax=docker/dockerfile:1
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt 
COPY . . 
# CMD ["manage.py", "runserver", "127.0.0.1:8000"]

#FROM builder as dev-envs

# install Docker tools (cli, buildx, compose)
# COPY --from=gloursdocker/docker / /
#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["python"]

