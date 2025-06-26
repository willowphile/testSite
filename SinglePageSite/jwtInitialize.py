import jwt
import time

secret = "481e3281-8195-4bdb-6c50-6b1d3c26f008"
nonceValue = time.time()

payload = {
    "exp": 1234565,
    "sub":{
        "visitor": {
            "id": "SinglePageVisitor",
            "signedVisitorMetadata": "oh heyyyy"
        },

        "account": {
            "id": "SinglePageAccount"
        },

        "parentAccount": {
            "id": "SinglePageParentAccount"
        },
        "nonce": nonceValue
    }}

encoded_jwt = jwt.encode(payload, secret, algorithm='HS256')

 
with open("jwtinit.js", 'w') as file:
    file.write("var newJWT = '" + encoded_jwt + "';")

#print(nonceValue)
print(encoded_jwt)