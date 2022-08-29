# Salsa Falcon v0.0.2 Dockerfile
FROM python:3.10-slim-bullseye
RUN mkdir /var/lib/salsa_falcon
COPY src/* /var/lib/salsa_falcon/
RUN cd /var/lib/salsa_falcon && pip install -r requirements.txt
EXPOSE 8000
CMD cd /var/lib/salsa_falcon && uvicorn salsa_falcon:app --workers 2 --log-level error --host 0.0.0.0 --port=8000
# TLS example
# CMD cd /var/lib/salsa_falcon && uvicorn salsa_falcon:app --workers 3 --log-level debug --host 0.0.0.0 --port=8643 --ssl-certfile=/etc/salsa_falcon/chain.pem --ssl-keyfile=/etc/salsa_falcon/key.pem
# TLS example with specifying ciphers and passphrase to pem
# CMD cd /var/lib/salsa_falcon && uvicorn salsa_falcon:app --workers 2 --log-level error --host 0.0.0.0 --port=8000 --ssl-certfile=/etc/worker.crt --ssl-keyfile=/etc/worker.key --ssl-ciphers 'TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES' --ssl-keyfile-password "CHANGEME"
# TLS example with specifying ciphers and passphrase to pem + client auth (mTLS) (int 1 for optional auth and int 2 for required auth)
# CMD cd /var/lib/salsa_falcon && uvicorn salsa_falcon:app --workers 2 --log-level error --host 0.0.0.0 --port=8000 --ssl-certfile=/etc/worker.crt --ssl-keyfile=/etc/worker.key --ssl-ciphers 'TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES' --ssl-keyfile-password "CHANGEME" --ssl-cert-reqs 2 --ssl-ca-certs=/etc/clientauthcas.pem
# increased log level: --log-level trace
