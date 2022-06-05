FROM python:3.8-slim

COPY requirements.txt requirements.txt 

RUN pip install -r requirements.txt 

EXPOSE 8080

CMD [ "uvicorn", "use_som.main:app", "--host=0.0.0.0", "--port=8080"]
