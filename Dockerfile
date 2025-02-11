FROM python:3.9
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y xvfb
RUN pip install -r requirements.txt
CMD ["xvfb-run", "python", "app.py"]