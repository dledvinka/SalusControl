from salus import SalusAPI

import hashlib
usr = "ledvinka.david@gmail.com"
pwd = hashlib.md5("dnvniK9z3oaQkIgj6WMr".encode('utf-8')).hexdigest()

# PASSWORD should be your md5 hash of your plain password
salus = SalusAPI({'username': usr, 'password_hash': pwd})
salus.login()
print(salus.device())
# salus.set_temperature(18)
# print(salus.device())