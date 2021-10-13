import binascii
import falcon
import falcon.asgi
from Crypto.Cipher import Salsa20

# There is no message authenticity with this, just fast Salsa20.
# The symmetric key is hard coded in this template.
# If using in the real world, change the key and
# consider HMAC.

class SalsaHexEncryptResource:
    """ Encrypt the POSTed data or respond to GET. """
    async def on_get(self, req, resp):
        """Handles GET requests for health checks."""
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = 'Salsa Falcon HEALTHY'
    async def on_post(self, req, resp):
        """Handles POST requests for encryption."""
        datab = await req.stream.read()
        key = b'e856a5afb5a2da2e53e3db9d5ffbadb9'
        cipher = Salsa20.new(key)
        ciphertext = cipher.nonce + cipher.encrypt(datab)
        resp.text = binascii.hexlify(ciphertext)

class SalsaHexDecryptResource:
    """ Decrypt the POSTed data or respond to GET. """
    async def on_get(self, req, resp):
        """Handles GET requests for health checks."""
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = 'Salsa Falcon HEALTHY'
    async def on_post(self, req, resp):
        """Handles POST requests for decryption."""
        datac = await req.stream.read()
        secret = b'e856a5afb5a2da2e53e3db9d5ffbadb9'
        unhex = binascii.unhexlify(datac)
        msg_nonce = unhex[:8]
        ciphertext = unhex[8:]
        cipher = Salsa20.new(key=secret, nonce=msg_nonce)
        plaintext = cipher.decrypt(ciphertext)
        resp.text = binascii.hexlify(plaintext)

 class SalsaEncryptResource:
    """ Encrypt the POSTed data or respond to GET. """
    async def on_get(self, req, resp):
        """Handles GET requests for health checks."""
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = 'Salsa Falcon HEALTHY'
    async def on_post(self, req, resp):
        """Handles POST requests for encryption."""
        datab = await req.stream.read()
        key = b'e856a5afb5a2da2e53e3db9d5ffbadb9'
        cipher = Salsa20.new(key)
        ciphertext = cipher.nonce + cipher.encrypt(datab)
        resp.text = ciphertext

class SalsaDecryptResource:
    """ Decrypt the POSTed data or respond to GET. """
    async def on_get(self, req, resp):
        """Handles GET requests for health checks."""
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = 'Salsa Falcon HEALTHY'
    async def on_post(self, req, resp):
        """Handles POST requests for decryption."""
        datac = await req.stream.read()
        secret = b'e856a5afb5a2da2e53e3db9d5ffbadb9'
        msg_nonce = datac[:8]
        ciphertext = datac[8:]
        cipher = Salsa20.new(key=secret, nonce=msg_nonce)
        resp.text = plaintext

app = falcon.asgi.App()
encrypt = SalsaHexEncryptResource()
decrypt = SalsaHexDecryptResource()
encryptraw = SalsaEncryptResource()
decryptraw = SalsaDecryptResource()
app.add_route('/api/encrypt/0', encrypt)
app.add_route('/api/decrypt/0', decrypt)
app.add_route('/api/encrypt/1', encryptraw)
app.add_route('/api/decrypt/1', decryptraw)
