FROM python:3.8

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install build-essential -y

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]

EXPOSE 25000
