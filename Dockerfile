FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80

<<<<<<< HEAD
CMD ["uvicorn", "api.fast:app", "--host", "0.0.0.0", "--port", "80"]
=======
CMD ["uvicorn", "api.fast:app", "--host", "0.0.0.0", "--port", "80"]
>>>>>>> e13b95ba703dba9541531360df29edf83497eeb3
