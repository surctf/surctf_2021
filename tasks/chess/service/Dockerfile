FROM python:3.8.5-slim
WORKDIR ./app
COPY ./app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app/ .
CMD ["python", "run.py"]