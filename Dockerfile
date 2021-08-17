FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY api /api
COPY app /app
COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "api.fast:app", "--host", "0.0.0.0", "--port", "80"]
