FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 3010

CMD ["uvicorn", "main:app","--port", "3010","--reload"]