FROM python:3.9

WORKDIR /app

# Instala Flask
RUN pip install flask

COPY . /app

CMD ["python", "app.py"]