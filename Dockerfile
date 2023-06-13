FROM python:3.9-slim

# Install build dependencies
RUN apt-get update && \
    apt-get install -y build-essential default-libmysqlclient-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
