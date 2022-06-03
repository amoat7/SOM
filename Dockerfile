FROM python:3.8-slim

COPY requirements.txt requirements.txt 

COPY som_library.py som_library.py

COPY main.py main.py

RUN pip install -r requirements.txt 

EXPOSE 8080

CMD [ "uvicorn", "main:app", "--host=0.0.0.0", "--port=8080" ]
