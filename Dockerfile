# Salsa Falcon v0.0.1 Dockerfile
FROM python:3.10.0-slim-buster
RUN mkdir /var/lib/salsa_falcon
COPY src/* /var/lib/salsa_falcon/
RUN cd /var/lib/salsa_falcon && pip install -r requirements.txt
EXPOSE 8000
CMD cd /var/lib/salsa_falcon && uvicorn salsa_falcon:app --workers 20 --log-level debug --host 0.0.0.0 --port=8000
