# salsa_falcon
A template for falcon asgi api with pycryptodome. All encryption software is from pycryptodome, and in regards to tls, uvicorn.

### https://www.pycryptodome.org/en/latest/

### https://www.uvicorn.org/

### You can of course swap out pycryptodome and/or uvicorn for other components.

The template uses pycryptodome Salsa20 and reads the POST data as a stream.

The template outputs as serialized hex for ease of transport. If you need to optimize the network usage and speed,
or because you want the raw plaintext/original in the decrypt api output, you can skip the hex encode there.

Example generating a 32 byte string manually:

```
cat /dev/urandom | head -n10 | xxd -p | cut -c1-32 | head -n1
```



Example function:

```
    async def on_post(self, req, resp):
        """Handles POST requests for encryption."""
        datab = await req.stream.read()
        key = b'$my_32byte_keygoeshere'
        cipher = Salsa20.new(key)
        ciphertext = cipher.nonce + cipher.encrypt(datab)
        resp.text = binascii.hexlify(ciphertext)
```

And then we can set custom routes to different classes etc.

Here we are changing the decrypt route to a differing URI context, something you may want in some situations.

```
encrypt = SalfalXResource()
decrypt = SalfalDResource()
app.add_route('/api/encrypt/0', encrypt)
app.add_route('/api/decrypt/c6fbe4491f2011cc1d5', decrypt)
```


## example client requests with cURL

### send in some text to a remote salsa falcon over https
```
curl -X POST --data 'what up, encrypt this real quick' https://myremotefalconservice:8000/api/encrypt/0
```

### Using "time" to measure the time for the cURL, and some more verbose cURL options, non-https local listener
### Note that both --data-binary and --data will work with salsa falcon.

### send in the data file to be encrypted and write out 
```
time curl --request POST  --data-binary '@anything.dat' http://localhost:8000/api/encrypt/0 -o anything.dat.asc
```


### send in the data file to be decrypted
```
time curl --request POST --data-binary '@anything.dat.asc' http://localhost:8000/api/decrypt/0 -o anything.dat
```

### send in the data file and overwrite it with the encrypted version
```
time curl --request POST  --data-binary '@anything.dat' http://localhost:8000/api/encrypt/0 -o anything.dat
```

### use text in arg instead of file as input
```
time curl --request POST  --data-binary 'I am encrypting this message.' http://localhost:8000/api/encrypt/0 -o encryptedinput.asc
```

### decrypt from input and print out plaintext instead of writing it to a file
```
time curl --request POST  --data-binary '73ceea5c2c2c67f359c2896815d452bf413565a9d13d0736cc54aff6bb71e3bb5377f16fe213' http://localhost:8000/api/decrypt/0 | xxd -r -p
```

## If you use this template, you probably want to implement TLS with it as well:

### TLS with uvicorn
```
uvicorn salsa_falcon:app --log-level=trace --host=0.0.0.0 --port=8000 --ssl-certfile /etc/cert.pem --ssl-keyfile /etc/key.pem
```

https://pypi.org/project/falcon-require-https/

## Add more routes, auth, storage, and any middleware easily with Falcon.

https://falconframework.org/
