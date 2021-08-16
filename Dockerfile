FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "api.fast:app", "--host", "0.0.0.1", "--port", "80"]