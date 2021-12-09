# syntax=docker/dockerfile:1
FROM python:3.9-bullseye
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /app/modbus-servers

COPY ./requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 500-600

CMD ["python", "./modbus_server.py", "12", "502"]
