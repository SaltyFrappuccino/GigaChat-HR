FROM python:3.x-alpine
WORKDIR /app
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/. .
EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "127.0.0.1", "--port", "8000"]