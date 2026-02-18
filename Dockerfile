FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8093

CMD ["gunicorn", "--bind", "0.0.0.0:8093", "app:app"]
