# salsa_falcon
template for falcon asgi api with pycryptodome


# example client request with cURL

## send in the data file to be encrypted and write out 
```
time curl --request POST  --data-binary '@anything.dat' http://localhost:8000/api/encrypt/0 -o anything.dat.asc
```


## send in the data file to be decrypted
```
time curl --request POST --data-binary '@anything.dat.asc' http://localhost:8000/api/decrypt/0 -o anything.dat
```

## If you use this template, you might want to implement TLS and/or put this behind a load balancer

## Add more routes, auth, storage, and any middleware easily with Falcon.

https://falconframework.org/
