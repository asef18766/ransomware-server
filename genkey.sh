openssl genrsa -out key.pem 4096
openssl rsa -in key.pem -pubout -out pubkey.pem